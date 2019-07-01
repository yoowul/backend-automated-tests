from scenario_tester.helpers.create_computation_and_get_results import create_computation_and_get_results


def run_reverse_reaction_network_and_wait_for_success(url, token, scenario_args):

    return create_computation_and_get_results('create-reverse-reaction-network', url, token, scenario_args)
