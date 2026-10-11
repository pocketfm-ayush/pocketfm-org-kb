# LightRAG P0 knowledge-correctness questions

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
