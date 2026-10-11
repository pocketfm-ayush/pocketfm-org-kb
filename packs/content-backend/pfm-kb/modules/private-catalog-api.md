# Private Catalog API Auth

## What It Is
Service-to-service access control for catalog reads and admin-ish helpers.

## Actors
CMS, experience, payments, and other trusted callers.

## Security / PII / Compliance
Tokens/roles are security-sensitive; never log secrets.

## Gaps
Exact role→route matrix is code/config — verify before documenting permissions.
