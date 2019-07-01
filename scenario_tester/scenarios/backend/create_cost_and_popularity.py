import simplejson as json

from scenario_tester.helpers.send_requests        import send_post_request_to_synthia_backend


def create_cost_and_popularity(url, scenario_args):

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/noc'.format(url, scenario_args['port']),
        data = json.dumps({
                "method": "run_pop_cost_algorithm",
                "mushroom":                      scenario_args.get("mushroom", 300367),
                "depth":                         scenario_args.get("max-depth", 10),
                "alpha":                         scenario_args.get("relative-labor-cost", 0.1209999871),
                "filters":     {
                    "mlogP":                     scenario_args.get("min-logP", -22.2025681023333),
                    "MlogP":                     scenario_args.get("max-logP", 25.7974318976667),
                    "max_products":              scenario_args.get("max-products", 4),
                    "min_year":                  scenario_args.get("min-year", 2000),
                    "max_year":                  scenario_args.get("max-year", 2016),
                    "npaths":                    scenario_args.get("max-paths", 1),
                    "seed":                      scenario_args.get("random-seed", 1),
                    "yield_type":                scenario_args.get("yield-type", "Chemicals yield"),
                    "blacklist":                 scenario_args.get("molecule-blacklist", []),
                    "prob":                      scenario_args.get("probability", 0.0),
                    "labor_cost":                scenario_args.get("labor-cost", 0.1209999871),
                    "known_popularity":          scenario_args.get("known-popularity", 2),
                    "buyable_cost":              scenario_args.get("buyable-cost", 1000),
                    "buyable_mass":              scenario_args.get("buyable-mass", 1000),
                    "known_mass":                scenario_args.get("known-mass", 1000),
                    "popcost_ratio":             scenario_args.get("popcost-ratio", 0.803),
                }
            }),
    )}
