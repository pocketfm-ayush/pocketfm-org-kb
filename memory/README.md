# Engineering memory

Durable human knowledge that Org Brain indexes alongside code evidence.

| Folder | Use for |
|---|---|
| `incidents/` | Redacted RCA write-ups, recurring failure modes |
| `decisions/` | ADRs (infra, KB layout, data stores) |
| `lessons/` | Short “what we learned” notes after launches / outages |

Rules:

- Redact UIDs, tokens, phone numbers, internal URLs with credentials
- Date every note (`date: YYYY-MM-DD` in frontmatter)
- Link evidence when claims touch code (`repo@sha:path#symbol`)
- Prefer linking CKB / handbook entities over rewriting them
