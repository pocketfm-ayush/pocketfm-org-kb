# Ads and Offerwall

Aliases: fm-ads-client, offerwall, instream ads

Product context: `android-client/pfm-kb/modules/ads.md`

## What it is
FM Ads client integration for offerwall/incentive ads and related ad UI; instream/ad player pieces may also touch player surfaces.

## Graph anchors
| `fm-ads-client` | `aural/fm-ads-client/` |
| `OFFERWALL_ARCHITECTURE` | `aural/fm-ads-client/docs/` |

## Risks
- Confusing client offerwall with Airflow reward-credit jobs.
- Editing pocket-ads/dynamicAdsDependencies without confirming aural fm-ads-client ownership.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Ads and Offerwall" --graph $GRAPH
```
