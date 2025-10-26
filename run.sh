#!/usr/bin/env bash
docker-compose up -d
sleep 8
echo "Kafka iniciado. Abra dois terminais:"
echo "1️⃣ python3 consumer.py"
echo "2️⃣ python3 producer.py"
