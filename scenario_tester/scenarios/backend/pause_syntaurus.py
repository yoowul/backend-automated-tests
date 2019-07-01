import simplejson as json

from scenario_tester.helpers.send_requests        import send_post_request_to_synthia_backend


def pause_syntaurus(url, scenario_args):

    return {'response': send_post_request_to_synthia_backend(
        url = 'https://{}:{}/auto-retro/control'.format(url, scenario_args['port']),
        data = json.dumps({
                "uid": scenario_args.get("uid", None),
                "command": json.dumps({
                    "control": "STOP",
                }),
            }),
    )}
