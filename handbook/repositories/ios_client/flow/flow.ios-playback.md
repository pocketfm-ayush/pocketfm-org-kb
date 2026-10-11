---
id: flow.ios-playback
type: flow
repository: ios_client
status: established
evidence:
  - ios_client@edf2c101853a9f0cdef2706111c2072dd51b45d6:Pocket FM/Presentation/Features/PFMPlayerView/ViewModel/PFMPlaybackManager.swift#PFMPlaybackManager
  - ios_client@edf2c101853a9f0cdef2706111c2072dd51b45d6:Pocket FM/Presentation/Features/PFMShowDetail/ViewModel/PFMShowDetailViewModel.swift#PFMShowDetailViewModel
---

`PFMPlaybackManager` + `PFMShowDetailViewModel` own selecting another episode
from show details after player navigation. Wrong-episode playback after
show-details selection starts here (ios_client).
