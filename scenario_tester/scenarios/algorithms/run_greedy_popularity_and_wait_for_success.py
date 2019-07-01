from scenario_tester.helpers.create_computation_and_get_results import create_computation_and_get_results


def run_greedy_popularity_and_wait_for_success(url, token, scenario_args):

    return create_computation_and_get_results('create-greedy-popularity', url, token, scenario_args)
