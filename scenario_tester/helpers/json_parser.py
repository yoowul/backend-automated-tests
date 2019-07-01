import simplejson as json
from simplejson                 import JSONDecodeError
from scenario_tester.logging    import SCENARIO_LOGGER as logger


def parse_json_from_response(response_content):

    if isinstance(response_content, dict) or isinstance(response_content, list):
        return response_content

    try:
        response_json = json.loads(response_content)

    except (
        JSONDecodeError,
        ValueError,
    ) as exception:
        message = "Server response is not a valid JSON"
        logger.error(message)
        logger.debug(exception)
        raise exception

    return response_json
