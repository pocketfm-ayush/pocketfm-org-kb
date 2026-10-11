---
name: mcp
description: Use MCP servers/tools correctly — discover schema, least privilege, evidence-rich calls.
triggers: [mcp, mcp tool, model context protocol, tool calling]
intent: implement
priority: 88
---

# MCP

**Job:** call external tools safely and usefully.

## Do
1. Discover tool schema before calling (parameters, required fields).
2. Prefer the narrowest tool that answers the question.
3. Treat tool output as evidence — quote IDs/timestamps in the answer.
4. On auth errors, authenticate once; do not spin.
5. For monitoring stacks, prefer exhaustive checks (`monitoring-deploy`) over silent skips.

## Do not
- Invent tool names or args.
- Send secrets to logs or chat transcripts unnecessarily.

## Related
`agent-builder`, `monitoring-deploy`, host-specific MCP docs
