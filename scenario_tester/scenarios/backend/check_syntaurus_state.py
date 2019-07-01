import simplejson as json

from scenario_tester.helpers.send_requests        import send_post_request_to_synthia_backend


def check_syntaurus_state(url, scenario_args):

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/auto-retro/get-status'.format(url, scenario_args['port']),
        data = json.dumps({
                "uids": [scenario_args.get("uid", None)],
            }),
    )}
