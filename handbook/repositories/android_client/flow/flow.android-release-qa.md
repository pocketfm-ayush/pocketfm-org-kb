---
id: flow.android-release-qa
type: flow
repository: android_client
status: established
evidence:
  - android_client@f7e1318769a62f83901b7a4accfed287310f4621:buildSrc/src/main/kotlin/ConfigData.kt#ConfigData
---

Android FM release / QA sanity ownership. `ConfigData.appVersion` /
`appVersionCode` (and `app/build.gradle.kts` `versionName`/`versionCode`) are
the source of truth for messages like "Release 9.3.0 (2030) is ready for qa
sanity", `release/DROID-*` branches, and Android Jira board bug-bash cuts.
Do not route those to airflow or Infra_k8s first — start at `android_client`.
