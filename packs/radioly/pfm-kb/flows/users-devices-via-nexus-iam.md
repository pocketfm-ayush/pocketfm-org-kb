# Users and devices via Nexus and IAM

## Journey
1. A Radioly path needs user/device data (feed, ads, payments, profile, device list).
2. **Non-PII / segments / create times** → Nexus.
3. **Identity / PII / device↔user accounts / OTP & profile mutations** → IAM.
4. Response caching may still protect high-QPS paths; invalidation must stay correct.
5. Goal (FMF-4712): no direct MySQL `users`/`devices` for these reads/writes.

## Modules
- [nexus-user-profile](../modules/nexus-user-profile.md)
- [iam-identity](../modules/iam-identity.md)
- [listener-profile](../modules/listener-profile.md)
- [device-login-limit](../modules/device-login-limit.md)
- [otp-login](../modules/otp-login.md)

## Failure modes
- Calling Nexus for PII or IAM for segments → wrong service boundary.
- Shadow mismatch during migration → log/metric only until ramp complete.
- Dropping cache invalidation → stale profile/device list after edits.
