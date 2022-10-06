import random
import unittest
from itertools import chain

from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming.tests import PySparkStreamingTestCase

class KafkaStreamTests(PySparkStreamingTestCase):
    timeout = 20  # seconds
    duration = 1

    def setUp(self):
        super(KafkaStreamTests, self).setUp()

        kafkaTestUtilsClz = self.ssc._jvm.java.lang.Thread.currentThread().getContextClassLoader()\
            .loadClass("org.apache.spark.streaming.kafka.KafkaTestUtils")
        self._kafkaTestUtils = kafkaTestUtilsClz.newInstance()
        self._kafkaTestUtils.setup()

    def tearDown(self):
        if self._kafkaTestUtils is not None:
            self._kafkaTestUtils.teardown()
            self._kafkaTestUtils = None

        super(KafkaStreamTests, self).tearDown()

    def _randomTopic(self):
        return "topic-%d" % random.randint(0, 10000)

    def _validateStreamResult(self, sendData, stream):
        result = {}
        for i in chain.from_iterable(self._collect(stream.map(lambda x: x[1]),
                                                   sum(sendData.values()))):
            result[i] = result.get(i, 0) + 1

        self.assertEqual(sendData, result)

    def test_kafka_stream(self):
        """Test the Python Kafka stream API."""
        topic = self._randomTopic()
        sendData = {"a": 3, "b": 5, "c": 10}

        self._kafkaTestUtils.createTopic(topic)
        self._kafkaTestUtils.sendMessages(topic, sendData)

        stream = KafkaUtils.createStream(self.ssc, self._kafkaTestUtils.zkAddress(),
                                         "test-streaming-consumer", {topic: 1},
                                         {"auto.offset.reset": "smallest"})
        self._validateStreamResult(sendData, stream)