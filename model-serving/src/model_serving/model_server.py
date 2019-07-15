from request import request
from common import logging

_logger = logging.get_logger(__name__)


def _setup_logger():
    _logger.setLevel("DEBUG")
    _logger.info("Starting model server for graduate admissions with Linear Regression")


def main():
    _setup_logger()
    request_consumer = request.RequestConsumer()

    while True:
        for message in request_consumer.poll():
            print(message.value["foo"])


if __name__ == '__main__':
    main()
