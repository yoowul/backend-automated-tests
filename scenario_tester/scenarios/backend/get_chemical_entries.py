import simplejson as json

from scenario_tester.helpers.send_requests               import send_post_request_to_synthia_backend


def get_chemical_entries(url, scenario_args):

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/get-data'.format(url, scenario_args['port']),
        data = json.dumps({
                "method": "get_chemical_entries",
                "field": "_id",
                "values": scenario_args.get("values", [953730, 953731, 632268, 300367]),
            }),
    )}
