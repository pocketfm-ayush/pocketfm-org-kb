# Comments and Reviews

Aliases: PFMCommentView, PFMReviewView, user reviews

Product context: `ios-client/pfm-kb/modules/comments-and-reviews.md`

## What it is
Show comments and reviews writing/reading, including reply and report options.

## Graph anchors
| `PFMCommentView` | `Pocket FM/Presentation/Features/PFMCommentView` |
| `PFMReviewView` | `Pocket FM/Presentation/Features/PFMReviewView` |
| `showComments route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Shipping moderation UI that bypasses report APIs.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Comments and Reviews" --graph $GRAPH
```
