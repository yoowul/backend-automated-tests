import pytz
import time
import argparse

import logging as python_logging

from datetime   import datetime, timedelta
from simplejson import JSONDecodeError

from scenario_tester import logging

from scenario_tester.logging import SCENARIO_FORMATTER as formatter
from scenario_tester.logging import SCENARIO_LOGGER    as logger
from scenario_tester.logging import LOG_LEVEL

from scenario_tester.scenarios.backend.algorithms.run_minimal_cost_and_wait_for_success                   import run_minimal_cost_and_wait_for_success as run_minimal_cost_and_wait_for_success_on_backend
from scenario_tester.scenarios.backend.algorithms.run_cost_and_popularity_and_wait_for_success            import run_cost_and_popularity_and_wait_for_success as run_cost_and_popularity_and_wait_for_success_on_backend
from scenario_tester.scenarios.backend.algorithms.run_greedy_popularity_and_wait_for_success              import run_greedy_popularity_and_wait_for_success as run_greedy_popularity_and_wait_for_success_on_backend
from scenario_tester.scenarios.backend.algorithms.run_manual_retro_and_wait_for_success                   import run_manual_retro_and_wait_for_success as run_manual_retro_and_wait_for_success_on_backend
from scenario_tester.scenarios.backend.algorithms.run_travel_as_product_and_wait_for_success              import run_travel_as_product_and_wait_for_success
from scenario_tester.scenarios.backend.algorithms.run_travel_as_reactant_and_wait_for_success             import run_travel_as_reactant_and_wait_for_success
from scenario_tester.scenarios.backend.algorithms.run_syntaurus_and_wait_for_success                      import run_syntaurus_and_wait_for_success as run_syntaurus_and_wait_for_success_on_backend

from scenario_tester.scenarios.backend.get_chemical_entries    import get_chemical_entries
from scenario_tester.scenarios.backend.get_molecular_strain    import get_molecular_strain
from scenario_tester.scenarios.backend.get_cross_reactivity    import get_cross_reactivity
from scenario_tester.scenarios.backend.get_similar_molecules   import get_similar_molecules
from scenario_tester.scenarios.backend.get_similar_reactions   import get_similar_reactions

from scenario_tester.scenarios.backend.stop_syntaurus import stop_syntaurus as stop_syntaurus_on_backend
from scenario_tester.scenarios.backend.pause_syntaurus import pause_syntaurus
from scenario_tester.scenarios.backend.check_syntaurus_state import check_syntaurus_state

# Helper imports
from scenario_tester.helpers.render_results import render_results
from scenario_tester.helpers.json_parser import parse_json_from_response
from scenario_tester.helpers.models import CommandError


SCENARIOS = {
        "run-minimal-cost-and-wait-for-success":                           run_minimal_cost_and_wait_for_success_on_backend,
        "run-cost-and-popularity-and-wait-for-success":                    run_cost_and_popularity_and_wait_for_success_on_backend,
        "run-greedy-popularity-and-wait-for-success":                      run_greedy_popularity_and_wait_for_success_on_backend,
        "run-manual-retro-and-wait-for-success":                           run_manual_retro_and_wait_for_success_on_backend,
        "run-travel-as-product-and-wait-for-success":                      run_travel_as_product_and_wait_for_success,
        "run-travel-as-reactant-and-wait-for-success":                     run_travel_as_reactant_and_wait_for_success,
        "run-syntaurus-and-wait-for-success":                              run_syntaurus_and_wait_for_success_on_backend,
        "get-chemical-entries":                                            get_chemical_entries,
        "get-molecular-strain":                                            get_molecular_strain,
        "get-cross-reactivity":                                            get_cross_reactivity,
        "get-similar-molecules":                                           get_similar_molecules,
        "get-similar-reactions":                                           get_similar_reactions,
        "stop-syntaurus":                                                  stop_syntaurus_on_backend,
        "pause-syntaurus":                                                 pause_syntaurus,
        "check-syntaurus-state":                                           check_syntaurus_state,
}

REQUIRED_RESPONSE = {'response'}


def convert_list_of_strings_into_list_of_dicts(str_list, scenario_list):

    dict_list = []

    for string in str_list:

        arg_dict = {}

        for split_string in string.split(','):
            split_list  = split_string.split('=', 1)
            key         = split_list[0]

            if '=' in split_string:
                value = split_list[1]
            else:
                value = None

            if key in arg_dict:
                if not isinstance(arg_dict[key], list):
                    previous_value = []
                    previous_value.append(arg_dict[key])
                    previous_value.append(value)
                    arg_dict.update({key: previous_value})
                else:
                    previous_value = arg_dict[key]
                    previous_value.append(value)
                    arg_dict.update({key: previous_value})
            else:
                arg_dict.update({key: value})

        dict_list.append(arg_dict)

    while len(dict_list) < len(scenario_list):
        dict_list.append({})

    return dict_list


def run_scenario(scenario, url, scenario_args):

    print('\n')
    logger.info("Current scenario: {}".format(scenario))

    if scenario not in SCENARIOS:
        raise CommandError("Input error: unable to find the specified scenario: {}".format(scenario))

    time_start   = datetime.now()

    scenario_response = SCENARIOS[scenario](url, scenario_args)

    time_stop          = datetime.now()
    time_elapsed       = time_stop - time_start
    time_elapsed       -= timedelta(microseconds=time_elapsed.microseconds)

    assert REQUIRED_RESPONSE.issubset(set(scenario_response))

    time_start = pytz.utc.localize(time_start).astimezone(pytz.timezone("Europe/Warsaw")).replace(tzinfo=None)
    scenario_response['time_start'] = time_start - timedelta(microseconds=time_start.microsecond)
    scenario_response['response_time'] = time_elapsed
    logger.info("Time elapsed for scenario '{}': {}".format(scenario, time_elapsed))
    json_is_valid = True

    try:
        response_json = parse_json_from_response(scenario_response['response'].content)
    except JSONDecodeError:
        # We want to report that a given scenario returned an invalid JSON
        # and continue, instead of halting the whole script
        scenario_response['response_errors'] = "Response is not a valid JSON"
        response_json = None
        json_is_valid = False
        logger.error('Response is not a valid json: {}'.format(scenario_response['response'].content))

    scenario_response['response_json'] = response_json

    if not 200 <= scenario_response['response'].status_code <= 300:
        generic_message = "Invalid backend response: {}".format(scenario_response['response'].content)
        scenario_response['response_errors'] = generic_message

    return scenario_response

def add_arguments(parser):

    # Required arguments
    parser.add_argument('scenarios',          nargs = '+', type = str)

    # Optional arguments
    #parser.add_argument('--test-type',        nargs = '?', type = str, default = 'consecutive', choices = ['consecutive', 'simultaneous'])
    parser.add_argument('--worker-url',       nargs = '?', type = str, default = 'munechem02.chematica.net')
    parser.add_argument('--worker-port',      nargs = '?', type = str, default = '443')
    parser.add_argument('--worker-user',      nargs = '?', type = str, default = 'WebApp')
    parser.add_argument('--worker-password',  nargs = '?', type = str, default = '7VsFdcHq')
    parser.add_argument('--log-level',        nargs = '?', type = str, default = 'INFO', choices = LOG_LEVEL.keys())
    parser.add_argument('--log-file',         nargs = '?', type = str)
    parser.add_argument('--summary-log-file', nargs = '?', type = str)
    parser.add_argument('--summary-format',   nargs = '?', type = str)
    parser.add_argument('--name',             nargs = '?', type = str, default = 'anonymous_tester')
    parser.add_argument('--repeat',           nargs = '?', type = int, default = 1)
    parser.add_argument('--scenario-args',    nargs = '*', type = str)

    args = parser.parse_args()

    return args

def handle():

    description = 'Logs in and runs specified test scenarios for a specified user a specified number of times'
    parser = argparse.ArgumentParser(description=description)

    kwargs = vars(add_arguments(parser))

    logging.set_console_handler(formatter(user = kwargs['name']), logger)

    logging.set_level(logger, kwargs['log_level'])
    summary_logger = python_logging.getLogger(__name__)
    summary_logger.setLevel(python_logging.INFO)
    summary_formatter = python_logging.Formatter('%(message)s')
    logging.set_console_handler(summary_formatter, summary_logger)

    if kwargs['scenario_args'] is not None and kwargs['scenario_args']:
        scenario_args = convert_list_of_strings_into_list_of_dicts(kwargs['scenario_args'], kwargs['scenarios'])
    else:
        scenario_args = [{}]

    if kwargs['log_file'] is not None:

        log_path = kwargs['log_file']
        if kwargs.get('summary_log_file', None) is not None:
            summary_log_path = kwargs['summary_log_file']
        else:
            summary_log_path = log_path

        logging.set_file_handler(log_path, formatter(user = kwargs['name']), logger)
        logging.set_file_handler(summary_log_path, summary_formatter, summary_logger)

    total_time = timedelta(seconds=0)
    summary = []
    url = kwargs['worker_url']

    for scenario in scenario_args:
        scenario['user'] = kwargs['worker_user']
        scenario['password'] = kwargs['worker_password']
        scenario['port'] = kwargs['worker_port']
    logger.debug("Scenario args: {}".format(scenario_args))
    logger.info('Test initiator: {}\n        Site: {}'.format(kwargs['name'], url))

    for iteration in range(kwargs['repeat']):

        iteration_summary = []

        scenario_list = list(kwargs['scenarios'])

        for scenario_index, scenario in enumerate(scenario_list):

            scenario_list[scenario_index] = 'pending'
            if scenario_index > len(scenario_args) - 1:
                extracted_args_dict = {}
            else:
                extracted_args_dict = scenario_args[scenario_index]

            try:
                scenario_results = run_scenario(scenario, url, extracted_args_dict)
            except ConnectionError as exception:
                raise CommandError(exception)

            total_time += scenario_results['response_time']
            logger.info('Total time elapsed: {}'.format(total_time))

            if scenario_results.get('response_errors', None) is None:
                logger.info("Scenario: '{}' has been successfully run".format(scenario))
            else:
                logger.error("Scenario: '{}' has encountered an error:\n         {}".format(scenario, scenario_results['response_errors']))

            if  scenario_results.get('additional_info', None) is not None:
                additional_info_summary = ''
                additional_info_summary += "Additional information for scenario {} - iteration {}:\n".format(
                    scenario, iteration + 1)
                for key in scenario_results['additional_info']:
                    additional_info_summary += "        {}\n".format(scenario_results['additional_info'][key])
                    logger.info(additional_info_summary)

            if scenario_results['response_json'] is not None:
                logger.debug("Scenario response:\n         {}".format(scenario_results['response_json']))
            else:
                logger.debug("Scenario response:\n         Response is not a valid JSON")

            scenario_results['iteration']       = iteration + 1
            scenario_results['scenario_name']   = scenario

            iteration_summary.append(scenario_results)

        summary.append(iteration_summary)

    render_results(summary, kwargs, total_time, summary_logger)

if __name__ == "__main__":
    handle()
