from kafka import KafkaConsumer
from common import configuration, logging
import json

_config_template = {
    'kafka': {
        'topic': str,
        'group_id': str,
        'bootstrap_servers': str
    }
}
_config = configuration.get_configuration(__name__).get(_config_template)

_logger = logging.get_logger(__name__)


class RequestConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(bootstrap_servers=_config.kafka.bootstrap_servers,
                                      auto_offset_reset='earliest',
                                      group_id=_config.kafka.group_id,
                                      value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        self.consumer.subscribe([_config.kafka.topic])
        _logger.info("Attached to topic graduate-admission-requests")

    def poll(self):
        for message in self.consumer:
            yield message
