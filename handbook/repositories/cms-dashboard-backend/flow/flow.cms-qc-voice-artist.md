---
id: flow.cms-qc-voice-artist
type: flow
repository: cms-dashboard-backend
status: established
evidence:
  - cms-dashboard-backend@97dae77fe95ee18e2db75e93166b3f94e7e6a390:v2/content_api/views.py#get_qc_details
---

CMS content ops: Raw QC stage, voice artist name visible then disappearing after
master upload, creator ID missing on show pages (`cms.pocketfm.com`). Start at
`get_qc_details` / cms-dashboard-backend — not radioly. Writer profile creation
on partner.pocketfm.com stays on writers-backend `create_creator_account`.
