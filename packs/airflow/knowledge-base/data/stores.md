# Stores touched by scheduled jobs

Jobs commonly read/write MySQL, Redis, S3, and warehouse extracts depending on
domain. Treat store names as domain-specific — verify in the DAG/workflow before
changing queries. No invented schemas here.
