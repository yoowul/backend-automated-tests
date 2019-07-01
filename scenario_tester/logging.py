import logging

LOG_LEVEL = {
    'DEBUG':    logging.DEBUG,
    'INFO':     logging.INFO,
    'WARNING':  logging.WARNING,
    'ERROR':    logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}


def set_logger():

    logger_object = logging.getLogger(__name__)
    logger_object.setLevel(logging.INFO)

    return logger_object


def set_formatter(user):

    return logging.Formatter('%(asctime)s %(levelname)s | {} | %(message)s'.format(user), datefmt='%H:%M:%S')

'''
example entry:

14:26:28 INFO     | Time elapsed for scenario 'run-manual-retro-and-wait-for-success': 0:00:10

'''

def set_level(logger_object, log_level):

    return logger_object.setLevel(LOG_LEVEL[log_level])


SCENARIO_LOGGER    = set_logger()
SCENARIO_FORMATTER = set_formatter


def set_console_handler(formatter_object, logger_object):

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    console_handler.setFormatter(formatter_object)
    logger_object.addHandler(console_handler)

    return logger_object


def set_file_handler(log_path, formatter_object, logger_object):

    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter_object)

    logger_object.addHandler(file_handler)
    logger_object.debug(file_handler)

    return logger_object
