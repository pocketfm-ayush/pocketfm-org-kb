# Kafka Workers

## What It Is
Async completion layer for product state after request-time APIs ACK.

## Actors
Kafka producers (Radioly/clients/payments/ads); worker pods; durable stores.

## Journey
Event on topic → worker updates MySQL/Redis/Scylla/S3/CRM → next app read sees durable state.

## Gaps
Exact topic→worker map lives in the K8s worker entry scripts — verify before claiming ownership.
