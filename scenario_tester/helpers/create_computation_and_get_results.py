import time

import simplejson as json

from datetime   import datetime, timedelta
from simplejson import JSONDecodeError

from scenario_tester.scenarios.backend.create_cost_and_popularity            import create_cost_and_popularity as create_cost_and_popularity_on_backend
from scenario_tester.scenarios.backend.create_greedy_popularity              import create_greedy_popularity as create_greedy_popularity_on_backend
from scenario_tester.scenarios.backend.create_manual_retro                   import create_manual_retro as create_manual_retro_on_backend
from scenario_tester.scenarios.backend.create_minimal_cost                   import create_minimal_cost as create_minimal_cost_on_backend
from scenario_tester.scenarios.backend.create_travel_as_product              import create_travel_as_product
from scenario_tester.scenarios.backend.create_travel_as_reactant             import create_travel_as_reactant
from scenario_tester.scenarios.backend.create_syntaurus                      import create_syntaurus as create_syntaurus_on_backend

from scenario_tester.scenarios.backend.stop_syntaurus import stop_syntaurus as stop_syntaurus_on_backend
from scenario_tester.scenarios.backend.pause_syntaurus import pause_syntaurus
from scenario_tester.scenarios.backend.check_syntaurus_state import check_syntaurus_state

from scenario_tester.helpers.kwargs_check import kwargs_check
from scenario_tester.helpers.json_parser  import parse_json_from_response
from scenario_tester.helpers.models import CommandError

from scenario_tester.logging import SCENARIO_LOGGER as logger


SCENARIOS = {
        "create-cost-and-popularity":                    create_cost_and_popularity_on_backend,
        "create-greedy-popularity":                      create_greedy_popularity_on_backend,
        "create-manual-retro":                           create_manual_retro_on_backend,
        "create-minimal-cost":                           create_minimal_cost_on_backend,
        "create-travel-as-product":                      create_travel_as_product,
        "create-travel-as-reactant":                     create_travel_as_reactant,
        "create-syntaurus":                              create_syntaurus_on_backend,
        "stop-syntaurus":                                stop_syntaurus_on_backend,
        "pause-syntaurus":                               pause_syntaurus,
        "check-syntaurus-state":                         check_syntaurus_state,
}

REQUIRED_PARAMS = {'timeout': 'digit', 'steps': 'digit', 'polling_interval': 'digit', 'snapshot_time': 'digit'}

def create_computation_and_get_results(scenario, url, scenario_args):
    print("SCENARIO_ARGS: {}".format(scenario_args))

    scenario_response = {}
    default_timeout = 1500
    timeout           = scenario_args.get('timeout', default_timeout)
    timeout = kwargs_check({'timeout': REQUIRED_PARAMS['timeout']}, {'timeout': timeout})
    polling_interval  = scenario_args.get('poll_interval', 3)
    polling_interval = kwargs_check({'polling_interval': REQUIRED_PARAMS['polling_interval']}, {'polling_interval': polling_interval})
    snapshot_time     = scenario_args.get('snapshot', 0)
    snapshot_time = kwargs_check({'snapshot_time': REQUIRED_PARAMS['snapshot_time']}, {'snapshot_time': snapshot_time})
    steps_required    = scenario_args.get('steps', 300)
    steps_required = kwargs_check({'steps': REQUIRED_PARAMS['steps']}, {'steps': steps_required})
    steps = 0
    paths = "0"

    scenario_result = SCENARIOS[scenario](url, scenario_args)

    try:
        scenario_result_json = parse_json_from_response(scenario_result['response'].content)
    except JSONDecodeError:
        logger.error('Response is not a valid json: {}'.format(scenario_result))
        return scenario_result

    if scenario != 'create-syntaurus' or not 200 <= scenario_result['response'].status_code <= 300:
        return scenario_result

    request_syntaurus_time = datetime.now()
    scenario_args['uid'] = scenario_result_json['uid']
    scenario_response['syntaurus_statistics'] = []
    logger.info("Syntaurus task {} started!".format(scenario_args['uid']))

    continue_polling = True

    time_start = datetime.now()

    scenario_args['last_polling_time'] = time_start

    while continue_polling:
        request_current_time = datetime.now()

        if not (request_current_time - scenario_args['last_polling_time']).total_seconds() >= polling_interval:
            continue
        computation_id = scenario_args['uid']
        scenario_args['uids'] = [computation_id]
        scenario_args['last_polling_time'] = request_current_time

        computation_status_response = check_syntaurus_state(url, scenario_args)

        try:
            computation_status_json = parse_json_from_response(computation_status_response['response'].content)
        except JSONDecodeError:
            logger.error('An error has occured during computation status check: \n {}'.format(computation_status_response['response'].content))
            computation_status_json = None

        message = None

        if computation_status_json:
            message = computation_status_json[-1].get('message', None)
            computation_state = computation_status_json[-1].get('status', "computation state is missing")
        else:
            computation_state = "STOPPED"

        if message:
            try:
                message_json = parse_json_from_response(message)
            except JSONDecodeError:
                logger.error('Computation status message cannot be parsed: \n {}'.format(message))
                message_json = None

            if message_json:
                step = message_json.get("step", None)
                if step:
                    steps = step
                paths_num = message_json.get("paths_num", None)
                if paths_num:
                    paths = paths_num

        if steps >= 30:

            if len(scenario_response['syntaurus_statistics']) == 0:
                request_new_time = datetime.now()
                time_elapsed = request_new_time - request_syntaurus_time
                time_elapsed -= timedelta(microseconds=time_elapsed.microseconds)
                scenario_response['syntaurus_statistics'].append(({"Time to 30 iterations": time_elapsed}, {"Paths": paths}))

                logger.info('Time to 30 iterations: {}'.format(scenario_response['syntaurus_statistics'][0][0]['Time to 30 iterations']))

        if steps >= 100:

            if len(scenario_response['syntaurus_statistics']) == 1:
                request_new_time = datetime.now()
                time_elapsed = request_new_time - request_syntaurus_time
                time_elapsed -= timedelta(microseconds=time_elapsed.microseconds)
                scenario_response['syntaurus_statistics'].append(({"Time to 100 iterations": time_elapsed}, {"Paths": paths}))

                logger.info('Time to 100 iterations: {}'.format(scenario_response['syntaurus_statistics'][1][0]['Time to 100 iterations']))

        if steps >= 300:

            if len(scenario_response['syntaurus_statistics']) == 2:
                request_new_time = datetime.now()
                time_elapsed = request_new_time - request_syntaurus_time
                time_elapsed -= timedelta(microseconds=time_elapsed.microseconds)
                scenario_response['syntaurus_statistics'].append(({"Time to 300 iterations": time_elapsed}, {"Paths": paths}))

                logger.info('Time to 300 iterations: {}'.format(scenario_response['syntaurus_statistics'][2][0]['Time to 300 iterations']))

        if snapshot_time != 0 and (request_current_time - time_start).total_seconds() >= snapshot_time and 'snapshot_time_results' not in scenario_response:
            scenario_response['snapshot_time_results'] = {"Description": "After {} minutes from the start".format(snapshot_time / 60), "Iterations": steps, "Paths": paths}
            logger.info("After {:0f} minutes from the start, the computation has reached: {} iterations and {} paths".format(snapshot_time / 60, steps, paths))

        if steps >= steps_required and snapshot_time == 0: #test_type != "simultaneous":
            print('Computation has reached or exceeded the required amount of iterations: {} out of {} in total.'.format(steps_required, steps))
            continue_polling = False

        elif computation_state == "STOPPED":
            print('Computation {} has been stopped! {:15}\n'.format(computation_id, computation_state))
            continue_polling = False

        elif computation_state not in {"RUNNING", "STOPPED"}:
            print('{:15}'.format('Unknown computation state\n'))
            scenario_response['additional_info'] = {
                "computation_state": "Computation {} has an unknown state: {}".format(computation_id, computation_state)
            }
            continue_polling = False

        elif (request_current_time - time_start).total_seconds() > timeout:
            logger.warning('Computation {} has timed out after {} s\n'.format(computation_id, timeout))
            scenario_response['additional_info'] = {
                'computation_state': 'Computation {} has timed out after {} s'.format(computation_id, timeout)
            }
            continue_polling = False

        else:
            print('Computation {} state: {}, iterations: {}, paths: {:15}'.format(computation_id, computation_state, steps, paths), end = '\r')

    logger.debug("STATISTICS: {}".format(scenario_response['syntaurus_statistics']))

    if scenario == 'create-syntaurus':
        if computation_state != "STOPPED":
            logger.info("Sending stop signal to syntaurus computation.")
            stop_response = SCENARIOS['stop-syntaurus'](url, scenario_args)

            if 200 <= stop_response['response'].status_code <= 300 :
                logger.info("Syntaurus computation stopped!")
            else:
                logger.error('An error has occured during stopping!')

            scenario_response['response'] = stop_response['response']
        else:
            scenario_response['response'] = computation_status_response['response']

        time.sleep(5)

        return scenario_response

    return scenario_response
