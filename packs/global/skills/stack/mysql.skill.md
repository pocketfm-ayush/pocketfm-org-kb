---
name: mysql
description: MySQL access patterns, migrations, EXPLAIN, and safe DML.
triggers: [mysql, mariadb, innodb, slow query]
intent: implement
priority: 70
---

# MySQL

## Do
- Prefer indexed predicates; EXPLAIN before heavy queries.
- Migrations expand-contract; avoid long locks on hot tables.
- Use transactions for multi-row integrity; keep them short.
- Read replicas for heavy analytics when available.

## Do not
- `SELECT *` on wide/hot tables in app paths.
- Ship unreviewed destructive DDL to prod.

## Related
`database-sql`, `performance-review`, `security-review`, `docker`, `kubernetes` as applicable.
