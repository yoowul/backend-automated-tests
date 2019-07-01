from scenario_tester.helpers.create_computation_and_get_results import create_computation_and_get_results


def run_manual_retro_and_wait_for_success(url, token, scenario_args):

    return create_computation_and_get_results('create-manual-retro', url, token, scenario_args)
