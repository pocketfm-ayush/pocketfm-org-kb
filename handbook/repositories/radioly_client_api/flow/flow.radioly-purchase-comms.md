---
id: flow.radioly-purchase-comms
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/whatsapp_notification/dto/transaction_notification_base_dto.py#TransactionBaseDTO
---

**Aliases:** purchase email, transaction whatsapp, payment receipt message

**When to use:** Purchase Comms (Email / WhatsApp) for a Pocket FM listener. First stop `TransactionBaseDTO` in `v2/whatsapp_notification/dto/transaction_notification_base_dto.py`.

**Required inputs:** screen and symptom.
