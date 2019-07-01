import simplejson as json

from scenario_tester.helpers.send_requests               import send_post_request_to_synthia_backend


def get_similar_molecules(url, scenario_args):

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/get-data'.format(url, scenario_args['port']),
        data = json.dumps({
                "method": "get_similar_chemical_entries",
                "smiles": "C1CCCCC1",
                "tanimoto": scenario_args.get("tanimoto", 1),
            }),
    )}
