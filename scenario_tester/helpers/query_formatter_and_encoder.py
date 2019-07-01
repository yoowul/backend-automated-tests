import urllib


def query_formatter_and_encoder(data, query_param):

    query_param_list = [(query_param, item) for item in data]

    return '?' + urllib.parse.urlencode(query_param_list)
