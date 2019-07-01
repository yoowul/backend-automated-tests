import requests
import urllib3

def send_request_to_backend(request_function, url, **kwargs):
    # Suppress warnings caused by verify=False. There's tons of them and they're obscuring other, much more important warnings.
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        return request_function(url, **kwargs)
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.MissingSchema,
        requests.exceptions.InvalidSchema,
    ) as exception:
        raise ConnectionError("Cannot connect to {}: {}".format(url, exception))

def send_post_request_to_synthia_backend(url, data, **kwargs):
    return send_request_to_backend(
        request_function    = requests.post,
        url                 = url,
        data = data,
        #json = data,
        verify = False,
    )
