import json
import os

from google.cloud import pubsub_v1

# set gcp project ID
PROJECT_ID = "tomrathdev-project1-391802"

# Instantiates a Pub/Sub client
publisher = pubsub_v1.PublisherClient()


def publish():
    topic_name = "pubsub-topic-de7a5ce"
    message = "test"

    if not topic_name or not message:
        return ('Missing "topic" and/or "message" parameter.', 400)

    print(f"Publishing message to topic {topic_name}")

    topic_path = publisher.topic_path(PROJECT_ID, topic_name)

    message_json = json.dumps(
        {
            "data": {"message": message},
        }
    )
    message_bytes = message_json.encode("utf-8")

    # Publishes a message
    try:
        publish_future = publisher.publish(topic_path, data=message_bytes)
        publish_future.result()  # Verify the publish succeeded
        return "Message published."
    except Exception as e:
        print(e)
        return (e, 500)
    
publish()


