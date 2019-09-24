from kafka import KafkaConsumer
import json
import signal
from modelserving import logger
from modelserving import config
_logger = logger.get_logger(__name__)


class RequestConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(bootstrap_servers=config.get("kafka.bootstrap_servers"),
                                      auto_offset_reset='earliest',
                                      group_id=config.get("kafka.group_id"),
                                      value_deserializer=self._message_deserializer,
                                      consumer_timeout_ms=1000)
        self.consumer.subscribe([config.get("kafka.topic")])

        self._subscribe_sigterm()
        self.is_running = True
        _logger.info("Attached to topic graduate-admission-requests")

    def poll(self):
        if self.is_running:
            for message in self.consumer:
                if message is not None:
                    _logger.info("Got message: " + str(message.value))

    @staticmethod
    def _message_deserializer(value):
        if value is None:
            return

        try:
            return json.loads(value.decode('utf-8'))
        except json.decoder.JSONDecodeError:
            _logger.warn('Unable to decode: %s', value)
            return None

    def _subscribe_sigterm(self):
        signal.signal(signal.SIGINT, self._exit_gracefully)
        signal.signal(signal.SIGTERM, self._exit_gracefully)

    def _exit_gracefully(self, signum, frame):
        self.is_running = False
