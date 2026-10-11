---
name: docker
description: Docker images, local compose, and immutable tags for deploy.
triggers: [docker, Dockerfile, compose, container image]
intent: implement
priority: 70
---

# Docker

## Do
- Multi-stage builds; small runtime images; non-root when possible.
- Pin base digests/tags — never rely on `:latest` in prod.
- Pass secrets at runtime, not `ENV` baked with values.
- Match local compose to CI assumptions where practical.

## Do not
- Commit secrets into image layers.
- Use mutable tags for production rollouts.

## Related
`database-sql`, `performance-review`, `security-review`, `docker`, `kubernetes` as applicable.
