# Allowlist Event Config

## What It Is
Product/ops-controlled list of which events Relay accepts and where they may route.

## Actors
Ops via private config APIs; gateway validators; router.

## Journey
Config stored → workers refresh cache → ingest/routing honor current rules.

## Product Source Of Truth
Event allowlist and destinations in Relay config store — not this KB.

## Gaps
Exact event→destination matrix is live DB; never invent it here.
