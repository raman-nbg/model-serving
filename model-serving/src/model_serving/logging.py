import logging


def get_logger(module_name: str):
    suffix = ""
    if module_name != "__main__":
        suffix = "." + module_name

    return logging.getLogger("serving.model-server" + suffix)
