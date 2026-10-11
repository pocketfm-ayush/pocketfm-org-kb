# Catalog Cache & Warmup

## What It Is
Performance layer so catalog reads stay fast without becoming the product source of truth.

## Actors
Catalog services; CMS/ops invalidation callers.

## User-Visible Invariants
Stale cache may briefly delay CMS edits until invalidation/TTL.

## Gaps
Exact TTL/allowlist of in-memory show ids is operational — verify config/source.
