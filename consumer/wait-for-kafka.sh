#!/bin/sh

echo "Attente de Kafka sur $KAFKA_BOOTSTRAP_SERVERS..."
while ! nc -z broker 29092; do
  sleep 1
done

echo "Kafka est prêt ! Démarrage du service..."
exec "$@"
