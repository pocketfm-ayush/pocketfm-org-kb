# Show Catalog Read

## What It Is
Authoritative show metadata reads for internal consumers assembling show pages and modules.

## Actors
Radioly/BFF, CMS/experience services, catalog service.

## Client Behavior
Listeners rarely call this directly; apps usually go through Radioly.

## User-Visible Invariants
Missing optional device metadata should not break internal show reads when allowed.

## Gaps
Which Radioly surfaces already proxy here must be confirmed per endpoint.
