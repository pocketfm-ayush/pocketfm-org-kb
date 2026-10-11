# Shared Context Builder

Every stage must build context in this order. Do not dump the whole repository or graph into
the prompt. Collect only evidence relevant to the PRD, eval, failure, or diff.

When sources disagree:

1. Approved PRD plus recorded product answers define intended behavior.
2. `knowledge-base/contract.json` defines enforceable paths, commands, and limits.
3. `knowledge-base/CONTRACT.md` defines architecture, conventions, and current public contract.
4. Current source and tests define implemented behavior.
5. `knowledge-base/` explains feature intent and prior decisions.
6. Graphify supplies discovery; verify uncertain or INFERRED edges against source.

GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify query "<question>" --graph "$GRAPH" --budget 4000
graphify explain "<symbol>" --graph "$GRAPH"
graphify path "<A>" "<B>" --graph "$GRAPH"
