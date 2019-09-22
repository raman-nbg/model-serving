from .request import request
from . import logger

_logger = logger.get_logger(__name__)


def main():
    _logger.setLevel("INFO")
    _logger.info("Starting model server for graduate admissions with Linear Regression")

    request_consumer = request.RequestConsumer()
    while request_consumer.is_running:
        request_consumer.poll()

    _logger.info("Terminated application graceful")


if __name__ == '__main__':
    main()
