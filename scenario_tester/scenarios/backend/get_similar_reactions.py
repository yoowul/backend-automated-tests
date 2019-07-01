import simplejson as json

from scenario_tester.helpers.send_requests               import send_post_request_to_synthia_backend


def get_similar_reactions(url, scenario_args):

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/similar-reactions'.format(url, scenario_args['port']),
        data = json.dumps({
                "host": "localhost",
                "rxid": 28547,
                "port": 8181,
                "target": scenario_args.get("target", "CC(=O)O[C@@H]1C2=C(C)[C@@H](OC(=O)[C@H](O)[C@@H](NC(=O)c3ccccc3)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](O)[C@@]3(C)C1=O)C2(C)C"),
            }),
    )}
