import logging


def set_logger(name):
    """
    Set lambda logger and define log structure
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s] - [%(name)s] - [%(levelname)s] : %(message)s')

    error_handler = logging.FileHandler('error_out.csv')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    info_handler = logging.FileHandler('info_out.csv')
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    debug_handler = logging.StreamHandler()
    #debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)

    logger.addHandler(error_handler)
    logger.addHandler(info_handler)
    logger.addHandler(debug_handler)

    return logger
