import logging

def get_logger(name, level = "INFO"):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(format)
    logger.addHandler(handler)
    log_level = logging.getLevelName(level)
    logger.setLevel(log_level)
    return logger
