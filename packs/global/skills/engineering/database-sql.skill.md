---
name: database-sql
description: Schema and query work — keys, indexes, migrations, safe SQL, explain plans.
triggers: [sql, schema, migration, query, index, database design]
intent: implement
priority: 87
---

# 12 · Database / SQL

**Job:** change data safely. Pair with stack skills (`mysql`, and Scylla guidance via ops docs). See `agents-database`.

## Do
1. Know the engine (MySQL vs Scylla vs other) before writing DDL/DML.
2. Migrations expandable/rollback-aware; no destructive prod steps unreviewed.
3. Indexes match access patterns; avoid unbounded scans.
4. Transactions and isolation only as wide as needed.
5. Parameterize queries — never string-build user input.

## Do not
- Run exploratory heavy queries on prod primaries.
- “Fix” with SELECT * into app memory for large sets.

## Output
Engine · Change · Migration plan · Query/index rationale · Risk · Verify (EXPLAIN / tests)
