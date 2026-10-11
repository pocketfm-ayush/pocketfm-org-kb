# LightRAG knowledge-correctness questions

## P0-01-IAM-TEMPORARY-DEACTIVATION
How does IAM initiate temporary account deactivation? Describe validation, persistence, cache invalidation, and events.

## P0-02-IAM-AUTHORIZATION-IDENTITY
Does IAM Authorization accept identity from the request body, or require a bearer token? Where do path and method come from?

## P0-03-IAM-NATIVE-DEVICE-PRESERVATION
When a web request updates an existing native IAM device, which platform and app version are preserved?

## P0-04-BRAHMYODHA-INTERNAL-TEST-AD
What is the Brahmyodha Internal Test Ad experiment? Is its runtime status known?

## P0-05-CONTENT-ELIGIBLE-ADS-S2S
What is the Content Eligible Ads S2S experiment? Is it active in production?

## P0-06-INDIA-DS-RANDOMIZATION-AUDIOBOOK
What is the India DS Randomization Audiobook experiment?

## P0-07-SY-SPINOFF
What is the SY Spinoff feature flag and is it active in production?

## P0-08-TDMB-SPINOFF
What is the TDMB Spinoff experiment and is it currently running?

## P0-09-RADIOLY-ADSMANAGER-SOURCE
Which source file currently implements Radioly AdsManager?

## P0-10-IAM-TOKEN-PERSISTENCE
For every IAM token type—access token, user refresh token, and device refresh token—state whether it is persisted and where.

## P0-11-IAM-LEGACY-MYSQL-TOKEN-PATHS
Do IAM's MySQL authentication and authorization tables participate in the current login or token-refresh execution path?

## P0-12-IAM-ACTIVE-DATABASES
Which databases does IAM actively read or write, and what purpose does each database serve? Distinguish current paths from legacy schemas.

## P1-13-IAM-FACEBOOK-LOGIN-ROUTE
Is Facebook login currently exposed through an active IAM public route?

## P1-14-IAM-USER-DELETED-EVENT
Does IAM currently publish the USER_DELETED event?

## P1-15-IAM-AUTHZ-METRICS
Are all IAM AuthZ metrics that are defined and incremented registered and emitted?

## P1-16-PYTHON-NEXUS-REDIS-CACHE
Does the Python Nexus profile client cache profile reads in Redis for 45 minutes?

## P1-17-NEXUS-LEGACY-CONSENT-TABLE
Does Nexus currently read the legacy nexus.user_comms_consent table?

## P1-18-NEXUS-PROFILE-AUTHORITY
Is Nexus the authoritative source for every user-profile field?

## P1-19-NEXUS-READ-AFTER-WRITE
Does Nexus guarantee read-after-write consistency after receiving an IAM event?

## P1-20-RADIOLY-RUNTIME-EXPERIMENTS
Which Radioly experiments are active in production right now?

## P1-21-ADS-TEMPORAL-QA-SCHEDULES
Which Ads Temporal schedules are enabled in QA right now?

## P1-22-AIRFLOW-ADS-PRODUCTION-SCHEDULES
Are all Airflow Ads schedules currently unpaused in production?

## P1-23-APOLLO-IMAGE-PIPELINE-LIFECYCLE
Is the Apollo Image Pipeline current behavior or a legacy workflow?

## P1-24-IAM-APPLE-IDENTITY-MAPPINGS
Where does IAM store Apple identity mappings?

## P1-25-IAM-PASSWORD-RESET-TOKENS
Where does IAM store password-reset tokens, and what is their lifetime?

## P1-26-IAM-OAUTH2-GRANT-CODES
Where does IAM store OAuth2 grant codes, and what is their lifetime?

## P2-27-ELIGIBLE-AD-PROVIDER-CONSUMERS
Which backend serves POST /v2/content_api/ads.get_eligible_ad, and which Android and iOS components consume it?

## P2-28-AUTH-REFRESH-PROVIDER-CONSUMERS
Which service implements POST /v1/auth/refresh, and which mobile clients consume it?

## P2-29-LOGIN-CONFIG-PROVIDER-CONSUMERS
Which backend owns GET /v3/onboarding/login_config, and which clients consume it?

## P2-30-PLAY-DETAILS-PROVIDER-CONSUMERS
Who implements GET /v2/content_api/show.play_details, and which mobile clients call it?

## P2-31-ANDROID-MEDIA-URL-RESOLUTION
Does Android resolve Apollo or Prism media URLs directly in the client?

## P2-32-IOS-APOLLO-PRISM-RESOLVER
Does iOS contain an Apollo or Prism resolver?

## P2-33-IMPRESSION-DATABASE
Does the Impression Service store impression counts in MySQL or ScyllaDB?

## P2-34-SHORTS-IMPRESSION-STORAGE
Does the Impression Service store Shorts impressions?

## P3-35-CANONICAL-ONTOLOGY-VERSION
What ontology version does the current canonical knowledge use?

## P3-36-CANONICAL-KNOWLEDGE-LOCATION
Is canonical knowledge stored inside application repositories under .cerebro or .kb-*?

## P3-37-RADIOLY-EXPERIMENT-COUNT
How many Radioly Experiment entities exist, and how many are active in production?

## P3-38-NEXUS-PROFILE-QUERY-EVIDENCE
What evidence supports the Nexus profile-query flow?
