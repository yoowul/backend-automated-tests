import simplejson as json

from scenario_tester.helpers.send_requests               import send_post_request_to_synthia_backend


def get_molecular_strain(url, scenario_args):

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/strain-report'.format(url, scenario_args['port']),
        data = json.dumps({
                "host": "172.17.0.1",
                "port": 8181,
                "smiles": scenario_args.get("smiles", "C1CCCCC1"),
            }),
    )}
