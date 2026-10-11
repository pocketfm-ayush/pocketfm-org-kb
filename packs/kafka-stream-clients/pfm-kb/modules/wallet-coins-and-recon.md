# Wallet Coins and Payment Recon

## What It Is
Async money correctness: coins land, recon heals mismatches, mandates notify.

## Actors
Payment gateways; wallet stores; listeners expecting credited balances.

## Security / PII / Compliance
Payment identifiers are sensitive.

## Gaps
Airflow gateway-recon jobs may overlap — confirm which runtime is live per flow.
