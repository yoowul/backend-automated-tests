from scenario_tester.helpers.create_computation_and_get_results import create_computation_and_get_results


def run_cost_and_popularity_and_wait_for_success(url, scenario_args):

    return create_computation_and_get_results('create-cost-and-popularity', url, scenario_args)
