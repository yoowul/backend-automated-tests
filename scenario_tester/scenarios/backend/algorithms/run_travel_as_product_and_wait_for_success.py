from scenario_tester.helpers.create_computation_and_get_results import create_computation_and_get_results


def run_travel_as_product_and_wait_for_success(url, scenario_args):

    return create_computation_and_get_results('create-travel-as-product', url, scenario_args)
