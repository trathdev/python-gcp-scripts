import pulumi
from pulumi_gcp import pubsub

topic = pubsub.Topic('pubsub-topic')

pulumi.export('topic_name', topic)