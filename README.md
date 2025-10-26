# Detec-o-de-fraude-Kafka
Detecção de Fraudes com Apache Kafka: Este projeto simula um sistema de detecção de fraudes em transações financeiras utilizando Apache Kafka, com produtor, consumidor e banco de dados.

docker-composer.yml

```yaml
version: '3.8'
services:
zookeeper:
image: bitnami/zookeeper:latest
environment:
- ALLOW_ANONYMOUS_LOGIN=yes
ports:
- '2181:2181'
kafka:
image: bitnami/kafka:latest
environment:
- KAFKA_BROKER_ID=1
- KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
- KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092
- ALLOW_PLAINTEXT_LISTENER=yes
ports:
- '9092:9092'
depends_on:
- zookeeper
