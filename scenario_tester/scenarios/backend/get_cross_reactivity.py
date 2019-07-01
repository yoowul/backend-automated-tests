import simplejson as json

from scenario_tester.helpers.send_requests               import send_post_request_to_synthia_backend


def get_cross_reactivity(url, scenario_args):

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/manual-forward'.format(url, scenario_args['port']),
        data = json.dumps({
            'rxid': 10970,
            'target': 'Cn1c(=O)c2c(ncn2C)n(C)c1=O',
            'substrates': 'C=O.CNc1c(N)n(C)c(=O)n(C)c1=O'

            }),
    )}
