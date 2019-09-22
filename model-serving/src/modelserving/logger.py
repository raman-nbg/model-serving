import logging


def get_logger(module_name: str):
    suffix = ""
    if module_name != "__main__":
        suffix = "." + module_name

    # logger = logging.getLogger("serving.model-server" + suffix)
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()
    logger.setLevel("INFO")

    return logger
