from datetime import datetime, timedelta
from statistics import stdev

def render_results(summary, kwargs, total_time, summary_logger):

    summary_string = ''

    if kwargs.get('summary_format', None) == 'concise':

        for iteration_index, iteration in enumerate(summary):
            iteration_time = timedelta(seconds=0)

            for scenario in iteration:
                summary_string += " - {}: {}".format(scenario['scenario_name'], scenario['response_time'])
                iteration_time += scenario['response_time']
            summary_string += ' | Time of repetition {}: {} |'.format(iteration_index + 1, iteration_time)

        for iteration in summary:

            for scenario in iteration:
                response_errors = scenario.get('response_errors', None)
                additional_info = scenario.get('additional_info', None)

                if response_errors is not None or additional_info is not None:
                    summary_string += " | Additional information for scenario {} - repetition {}: ".format(
                        scenario['scenario_name'], scenario['iteration'])

                if response_errors is not None:
                    summary_string += "- {} ".format(response_errors)

                if additional_info is not None:
                    for _ in scenario['additional_info']:
                        summary_string += "- {} ".format(additional_info[_])

    else:

        summary_string += '''
        ------------------------------------------------------------------------------------------
                             SUMMARY FOR {}
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''.format(kwargs['name'].upper())

        time_to_x = []
        time_to_y = []
        time_to_z = []
        response_times = []

        scenario_run_data = []

        if 'syntaurus' in summary[0][0]['scenario_name']:
            summary_string += \
            '\n                                 Results\n'

        elif 'manual' in summary[0][0]['scenario_name']:
            summary_string += \
            '\n                                 First fireworks received\n'
        else:
            summary_string += \
            '\n                                 \n'

        summary_string += \
        '            Repetition:'
        for iteration in summary:
            summary_string += \
            ',                {}     '.format(summary.index(iteration) + 1)

        summary_string += \
        "\n            Time and date:            "
        for iteration in summary:
            for scenario in iteration:
                summary_string += \
                ", {}  ".format(scenario['time_start'])

        if 'syntaurus' in summary[0][0]['scenario_name']:

            for iteration_number in ['30', '100', '300']:

                if iteration_number == ['30', '100', '300'][0]:
                    summary_string += \
                    '\n            Time to {} iterations: '.format(iteration_number)
                else:
                    summary_string += \
                    '\n            Time to {} iterations:'.format(iteration_number)
                for iteration in summary:
                    for scenario in iteration:
                        syntaurus_statistics = scenario.get("syntaurus_statistics", None)
                        if syntaurus_statistics:
                            for pair in scenario['syntaurus_statistics']:
                                for dictionary in pair:
                                    for key in dictionary:
                                        if ' {} '.format(iteration_number) in key:
                                            summary_string += ",    {}           ".format(dictionary[key])
                                            if iteration_number == ['30', '100', '300'][0]:
                                                time_to_x.append(dictionary[key])
                                            elif iteration_number == ['30', '100', '300'][1]:
                                                time_to_y.append(dictionary[key])
                                            elif iteration_number == ['30', '100', '300'][2]:
                                                time_to_z.append(dictionary[key])

                summary_string += \
                '\n            Paths:  '
                for iteration in summary:
                    for scenario in iteration:
                        syntaurus_statistics = scenario.get("syntaurus_statistics", None)
                        if syntaurus_statistics:
                            for pair in scenario['syntaurus_statistics']:

                                for dictionary in pair:
                                    for key in dictionary:
                                        if ' {} '.format(iteration_number) in key:
                                            summary_string += ",                   {}".format(pair[1]["Paths"])

        if not 'syntaurus' in summary[0][0]['scenario_name']:
            summary_string += \
            '\n            Time after clicking "run":'

        for iteration in summary:
            for scenario in iteration:
                if not 'syntaurus' in scenario['scenario_name']:
                    summary_string += \
                    ', {}              '.format(scenario['response_time'])
                    response_times.append(scenario['response_time'])

        summary_string += \
        "\n            Notes:"

        for iteration in summary:
            for scenario in iteration:

                response_errors = scenario.get('response_errors', None)
                additional_info = scenario.get('additional_info', None)
                snapshot_results = scenario.get('snapshot_time_results', None)

                if snapshot_results is not None:
                    summary_string += \
                    "\n            {}\nIterations:            {}\nPaths:            {}".format(snapshot_results['Description'], snapshot_results['Iterations'], snapshot_results['Paths'])

                if response_errors is not None or additional_info is not None:
                    summary_string += "\n            {} - repetition {}:".format(scenario['scenario_name'], summary.index(iteration) + 1)
                if response_errors is not None:
                    summary_string += "\n            {}".format(response_errors)

                if additional_info is not None:
                    for _ in scenario['additional_info']:
                        summary_string += "\n            {}".format(additional_info[_])

        summary_string += \
        "\n                                 ,Average values              ,standard deviation"

        if 'syntaurus' in summary[0][0]['scenario_name']:
            list_of_times = [time_to_x, time_to_y, time_to_z]

            for list_item in list_of_times:
                total_time = timedelta(seconds=0)
                for item in list_item:
                    total_time += item

                if total_time.total_seconds() > 0:
                    if list_of_times.index(list_item) == 0:
                        summary_string += \
                        "\n            Time to 30 iterations:     "
                    elif list_of_times.index(list_item) == 1:
                        summary_string += \
                        "\n            Time to 100 iterations:    "
                    elif list_of_times.index(list_item) == 2:
                        summary_string += \
                        "\n            Time to 300 iterations:    "
                    average_time = total_time / len(summary)
                    summary_string += \
                    ",{}".format(average_time - timedelta(microseconds=average_time.microseconds))
                    if len(summary) >= 2:
                        standard_deviation_seconds = stdev([response_time.total_seconds() for response_time in time_to_x])
                        standard_deviation_timedelta = timedelta(seconds=standard_deviation_seconds)
                        standard_deviation_timedelta -= timedelta(microseconds=standard_deviation_timedelta.microseconds)
                        summary_string += \
                        ",               {}".format(standard_deviation_timedelta)

        else:
            summary_string += \
            '\n            Time after clicking "run": ,'
            average_time = total_time / len(summary)
            summary_string += \
            "{},".format(average_time - timedelta(microseconds=average_time.microseconds))

            if len(summary) >= 2:
                standard_deviation_seconds = stdev([response_time.total_seconds() for response_time in response_times])
                standard_deviation_timedelta = timedelta(seconds=standard_deviation_seconds)
                standard_deviation_timedelta -= timedelta(microseconds=standard_deviation_timedelta.microseconds)
                summary_string += \
                "               {},".format(standard_deviation_timedelta)

    summary_logger.info(summary_string)
