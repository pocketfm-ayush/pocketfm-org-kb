# Multi-Tenant Apps

## What It Is
One Relay codebase, multiple product tenants with separate buses and sometimes different handler rules.

## Actors
FM / Comics / Novels / TV clients; router; exporters.

## Client Behavior
Clients send tenant/app identity in headers; routing depends on it.

## Gaps
Novels/TV route parity vs FM must be verified in router source — do not assume identical.
