# Author Profile and Gifting

Aliases: AuthorProfile, author gifting, author note

Product context: `ios-client/pfm-kb/modules/author-and-gifting.md`

## What it is
Author profile surfaces plus gifting and author-note experiences.

## Graph anchors
| `AuthorProfile` | `Pocket FM/Presentation/Features/AuthorProfile` |
| `PFMAuthorGifting` | `Pocket FM/Presentation/Features/PFMAuthorGifting` |
| `PFMAuthorNote` | `Pocket FM/Presentation/Features/PFMAuthorNote` |

## Risks
- Hardcoding gift prices or author ids.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Author Profile and Gifting" --graph $GRAPH
```
