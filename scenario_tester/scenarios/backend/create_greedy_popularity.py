import simplejson as json

from scenario_tester.helpers.send_requests        import send_post_request_to_synthia_backend


def create_greedy_popularity(url, scenario_args):

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/noc'.format(url, scenario_args['port']),
        data = json.dumps({
                "method": "run_greedy_popularity_algorithm",
                "mushroom":                      scenario_args.get("mushroom", 300367),
                "depth":                         scenario_args.get("max-depth", 5),
                "alpha":                         scenario_args.get("relative-labor-cost", 1000.0),
                "filters":     {
                    "mlogP":                     scenario_args.get("min-logP", -22.2025681023333),
                    "MlogP":                     scenario_args.get("max-logP", 25.7974318976667),
                    "max_products":              scenario_args.get("max-products", 4),
                    "min_year":                  scenario_args.get("min-year", 2000),
                    "max_year":                  scenario_args.get("max-year", 2017),
                    "npaths":                    scenario_args.get("max-paths", 1),
                    "seed":                      scenario_args.get("random-seed", 1),
                    "yield_type":                scenario_args.get("yield-type", "Chemicals yield"),
                    "blacklist":                 scenario_args.get("molecule-blacklist", []),
                    "popularity_flag":           scenario_args.get("popularity_flag", 0),
                    "prob":                      scenario_args.get("probability", 0.0),
                }
            }),
    )}
