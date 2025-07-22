# Kafka Docker Examples

This repository provides a simple and easy-to-understand example of how to use Kafka with Docker. It includes a Kafka broker, a Zookeeper instance, a Python producer, and a Python consumer, all running in separate Docker containers.

## Overview

This project demonstrates a basic Kafka setup using Docker Compose. It consists of four main services:

*   **Zookeeper**: Manages the Kafka brokers and keeps track of their status.
*   **Kafka**: The message broker that facilitates communication between the producer and consumer.
*   **Python Producer**: A simple Python script that sends messages to a Kafka topic.
*   **Python Consumer**: A simple Python script that receives messages from a Kafka topic.

The services are orchestrated using `docker-compose.yml`, which makes it easy to start, stop, and manage the entire application stack.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

To get started with this example, follow these simple steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/kafka-docker-examples.git
    cd kafka-docker-examples
    ```

2.  **Start the application:**
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images for the producer and consumer and start all the services defined in the `docker-compose.yml` file.

3.  **View the output:**
    You will see the producer sending messages and the consumer receiving them in your terminal.

4.  **Stop the application:**
    To stop the application, press `Ctrl+C` in the terminal where `docker-compose` is running, or run the following command in a separate terminal:
    ```bash
    docker-compose down
    ```

## Components

### Zookeeper

Zookeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. In this setup, Zookeeper is used by Kafka to manage the cluster.

*   **Image**: `confluentinc/cp-zookeeper:latest`
*   **Port**: `2181`

### Kafka

Kafka is a distributed streaming platform that is used for building real-time data pipelines and streaming apps.

*   **Image**: `confluentinc/cp-kafka:latest`
*   **Ports**: `9092` (for internal communication within the Docker network) and `29092` (for external communication from the host machine).
*   **Dependencies**: Depends on Zookeeper.
*   **Environment Variables**:
    *   `KAFKA_BROKER_ID`: The unique ID for the Kafka broker.
    *   `KAFKA_ZOOKEEPER_CONNECT`: The address of the Zookeeper instance.
    *   `KAFKA_ADVERTISED_LISTENERS`: The listeners that are advertised to clients.
    *   `KAFKA_LISTENER_SECURITY_PROTOCOL_MAP`: The security protocol map for the listeners.
    *   `KAFKA_INTER_BROKER_LISTENER_NAME`: The listener name for inter-broker communication.
    *   `KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR`: The replication factor for the offsets topic.

### Python Producer

The producer is a simple Python script that sends messages to the `my-topic` Kafka topic.

*   **Build Context**: `./python/producer`
*   **Dependencies**: Depends on Kafka.
*   **Functionality**:
    *   Connects to the Kafka broker at `kafka:9092`.
    *   Sends messages "Message 0" to "Message 99" to the `my-topic` topic.
    *   Pauses for 1 second between each message.

### Python Consumer

The consumer is a simple Python script that receives messages from the `my-topic` Kafka topic.

*   **Build Context**: `./python/consumer`
*   **Dependencies**: Depends on Kafka.
*   **Functionality**:
    *   Connects to the Kafka broker at `kafka:9092`.
    *   Subscribes to the `my-topic` topic.
    *   Prints the received messages to the console.

## How it Works

1.  `docker-compose up` starts all the services.
2.  The Zookeeper service starts and becomes available.
3.  The Kafka service starts and connects to Zookeeper.
4.  The Python producer connects to the Kafka broker and starts sending messages to the `my-topic` topic.
5.  The Python consumer connects to the Kafka broker, subscribes to the `my-topic` topic, and starts receiving messages.
6.  The received messages are printed to the console.

## Customization

You can easily customize the producer and consumer to suit your needs.

### Producer

To change the messages being sent, edit the `python/producer/producer.py` file. For example, you can change the number of messages or the content of the messages.

```python
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka:9092')

for i in range(10):  # Change the number of messages
    message = f"This is a custom message: {i}"  # Change the message content
    producer.send('my-topic', message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(2)  # Change the sleep interval

producer.flush()
```

### Consumer

To change how the messages are processed, edit the `python/consumer/consumer.py` file. For example, you can add logic to process the messages in a different way.

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest'
)

for message in consumer:
    # Add your custom message processing logic here
    processed_message = message.value.decode('utf-8').upper()
    print(f"Processed and received: {processed_message}")
```

After making changes, remember to rebuild the images using `docker-compose up --build`.
