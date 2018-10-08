import logging
import logging.handlers as handlers

def set_logger(name):
    """
    Set lambda logger and define log structure
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(asctime)s] - [%(name)s] - [%(levelname)s] : %(message)s')

    error_handler = handlers.TimedRotatingFileHandler('logs/error_timed_app.log', when='M', interval=60)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    info_handler = handlers.TimedRotatingFileHandler('logs/info_timed_app.log', when='M', interval=60)
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    #debug_handler = logging.StreamHandler()
    #debug_handler.setLevel(logging.DEBUG)
    #debug_handler.setFormatter(formatter)

    logger.addHandler(error_handler)
    logger.addHandler(info_handler)
    #logger.addHandler(debug_handler)

    return logger
