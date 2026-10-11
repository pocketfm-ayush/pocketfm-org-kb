# Purchase Comms (Email / WhatsApp)

Aliases: purchase email, transaction whatsapp, payment receipt message

Product context: `radioly/pfm-kb/modules/purchase-comms.md`

## What it is
Outbound transactional messaging after purchases (and related verification
emails). India WhatsApp purchase-success path and email queue — not the
in-app notification inbox.

## Graph anchors
| Symbol | Source |
|---|---|
| `TransactionSuccessWhatsappService` | `v2/whatsapp_notification/` |
| `EmailService` / transaction email helpers | `v2/email/` |

## Key edges
- Distinct from `notification-inbox` and `notification-permission`.
- Password-reset email remains under `email-password-reset`.

## Risks
- Claiming global WhatsApp coverage — purchase WhatsApp is locale-gated (India).
- Inventing template copy.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "TransactionSuccessWhatsappService EmailService" --graph $GRAPH
```
