from scenario_tester.helpers.models import CommandError


def kwargs_check(required_params, received_params):

    assert isinstance(required_params, dict), "Internal error: required_parameters \
    defined in scenario are not a dict"
    assert isinstance(received_params, dict), "Internal error: received_parameters \
    passed into scenario are not a dict"

    if not set(required_params).issubset(set(received_params)):
        raise CommandError("No argument(s) given for scenario: {}".format(set(required_params)))

    for _ in set(required_params):
        value  = received_params[_]

        data_type = required_params.get(_, None)

        if data_type == 'digit':
            if isinstance(value, int):
                return value
            if isinstance(value, str):
                if value.isdigit():
                    return int(value)
                else:
                    raise CommandError("Value for argument {} should be a digit".format(_))
            else:
                raise AssertionError('Value passed into argument {} is neither string nor int,\
                 cannot convert into digit'.format(_))
        else:
            for item in value:
                assert isinstance(item, str), 'Value passed into argument {} is not a string'
