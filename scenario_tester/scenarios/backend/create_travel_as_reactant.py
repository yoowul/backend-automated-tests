import simplejson as json

from scenario_tester.helpers.send_requests        import send_post_request_to_synthia_backend


def create_travel_as_reactant(url, scenario_args):

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/noc'.format(url, scenario_args['port']),
        data = json.dumps({
                "method": "travel_to_reactants",
                "sort_reactions_by": scenario_args.get("sort-reactions-by", []),
                "offset": scenario_args.get("offset", 0),
                "limit": scenario_args.get("limit", 5),
                "mushroom": scenario_args.get("mushroom", 300367),
            }),
    )}
