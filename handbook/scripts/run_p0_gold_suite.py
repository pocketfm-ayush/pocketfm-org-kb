#!/usr/bin/env python3
"""Score P0/P1 Slack-gold + coverage probes against a LightRAG-shaped /query URL.

Usage:
  python org-handbook/scripts/run_p0_gold_suite.py \
    --base-url http://127.0.0.1:9621 \
    --out org-handbook/lightrag/slots/live/p0-gold-report.md
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

CASES = [
    {
        "id": "SLACK-GOLD-01",
        "q": "iOS: selecting another episode from show details after player navigation plays wrong episode. Which client repo owns this?",
        "repos": ["ios_client"],
        "must": ["ios_client", "show", "episode"],
    },
    {
        "id": "SLACK-GOLD-02",
        "q": "Where was the production episode seq_number bug fixed (repo + PR lineage) and which TG owns verification?",
        "repos": ["radioly_client_api"],
        "must": ["radioly_client_api", "seq_number"],
    },
    {
        "id": "SLACK-GOLD-05",
        "q": "Show details shows Resume Episode 273 but user unlocked only 263. Which repo/file/function owns the resume pointer vs unlocked count?",
        "repos": ["radioly_client_api"],
        "must": ["radioly_client_api", "models.py", "resume"],
        "path_sub": "v2/content_api/models.py",
    },
    {
        "id": "SLACK-GOLD-07",
        "q": "Spanish shows appear for users who selected English. Which radioly feed/cache path is the primary suspect and what should be checked about the cache key?",
        "repos": ["radioly_client_api"],
        "must": ["radioly_client_api", "feed", "language", "cache"],
    },
    {
        "id": "SLACK-GOLD-09",
        "q": "Continue Playing module unexpectedly changes ranking/contents. Which repo owns Continue Playing construction vs DS ranking?",
        "repos": ["radioly_client_api"],
        "must": ["radioly_client_api", "continue"],
    },
    {
        "id": "SLACK-GOLD-10",
        "q": "WhatsApp notifications toggle does not persist. Which client API and IAM endpoint/field own this preference?",
        "repos": ["radioly_client_api", "iam"],
        "must": ["iam", "is_whatsapp"],
    },
    {
        "id": "COV-01-RADIOLY_CLIENT_API",
        "q": "Across the org KB, locate repo radioly_client_api: primary module paths and top handlers for a production bug.",
        "repos": ["radioly_client_api"],
        "must": ["radioly_client_api"],
    },
    {
        "id": "COV-02-IAM",
        "q": "Across the org KB, locate repo iam: primary module paths and top handlers for a production bug.",
        "repos": ["iam"],
        "must": ["iam"],
    },
    {
        "id": "COV-03-NEXUS",
        "q": "Across the org KB, locate repo nexus: primary module paths and top handlers for a production bug.",
        "repos": ["nexus"],
        "must": ["nexus"],
    },
    {
        "id": "COV-04-ANDROID_CLIENT",
        "q": "Across the org KB, locate repo android_client: primary module paths and top handlers for a production bug.",
        "repos": ["android_client"],
        "must": ["android_client"],
    },
    {
        "id": "COV-05-IOS_CLIENT",
        "q": "Across the org KB, locate repo ios_client: primary module paths and top handlers for a production bug.",
        "repos": ["ios_client"],
        "must": ["ios_client"],
    },
    {
        "id": "SLACK-GOLD-06",
        "q": "content-fm ServerError / connection failures — which repo and data store path should on-call inspect first?",
        "repos": ["content-backend"],
        "must": ["content-backend", "HandleHTTPError"],
    },
    {
        "id": "SLACK-GOLD-08",
        "q": "content-fm OperationTimedOut against Scylla — which service owns the client and what evidence pointer should KB return?",
        "repos": ["content-backend"],
        "must": ["content-backend", "Scylla"],
    },
    {
        "id": "SLACK-GOLD-04",
        "q": "Italy Popular module shows English titles. Which service owns feed module composition for LATAM/Italian Popular?",
        "repos": ["radioly_client_api"],
        "must": ["radioly", "Popular"],
    },
    {
        "id": "SLACK-GOLD-11",
        "q": "Release 9.3.0 (2030) is ready for qa sanity on branch release/DROID-7761. Which client repo owns Android FM versionCode/versionName?",
        "repos": ["android_client"],
        "must": ["android_client", "ConfigData"],
    },
    {
        "id": "SLACK-GOLD-12",
        "q": "Home module title shows Pocketfm instead of Pocket FM. Which radioly function owns localized module titles like Popular on Pocket FM?",
        "repos": ["radioly_client_api"],
        "must": ["radioly", "get_localized_module_title"],
    },
    {
        "id": "COV-06-APOLLO",
        "q": "Across the org KB, locate repo apollo: primary module paths and top handlers for a production bug.",
        "repos": ["apollo"],
        "must": ["apollo"],
    },
    {
        "id": "COV-07-IMPRESSION",
        "q": "Across the org KB, locate repo impression: primary module paths and top handlers for a production bug.",
        "repos": ["impression"],
        "must": ["impression"],
    },
    {
        "id": "COV-08-AIRFLOW",
        "q": "Across the org KB, locate repo airflow: primary module paths and top handlers for a production bug.",
        "repos": ["airflow"],
        "must": ["airflow"],
    },
    {
        "id": "COV-09-KAFKA_STREAM_CLIENTS",
        "q": "Across the org KB, locate repo kafka-stream-clients: primary module paths and top handlers for a production bug.",
        "repos": ["kafka-stream-clients"],
        "must": ["kafka-stream-clients"],
    },
    {
        "id": "COV-10-GO_COMMON",
        "q": "Across the org KB, locate repo go-common: primary module paths and top handlers for a production bug.",
        "repos": ["go-common"],
        "must": ["go-common"],
    },
    {
        "id": "COV-11-PYTHON_COMMON",
        "q": "Across the org KB, locate repo python-common: primary module paths and top handlers for a production bug.",
        "repos": ["python-common"],
        "must": ["python-common"],
    },
    {
        "id": "COV-12-EXPERIENCE",
        "q": "Across the org KB, locate repo experience: primary module paths and top handlers for a production bug.",
        "repos": ["experience"],
        "must": ["experience"],
    },
    {
        "id": "COV-13-CONTENT_BACKEND",
        "q": "Across the org KB, locate repo content-backend: primary module paths and top handlers for a production bug.",
        "repos": ["content-backend"],
        "must": ["content-backend"],
    },
    {
        "id": "COV-14-ADS",
        "q": "Across the org KB, locate repo ads: primary module paths and top handlers for a production bug.",
        "repos": ["ads"],
        "must": ["ads"],
    },
    {
        "id": "COV-17-WRITERS_BACKEND",
        "q": "Across the org KB, locate repo writers-backend: primary module paths and top handlers for a production bug.",
        "repos": ["writers-backend"],
        "must": ["writers-backend"],
    },
    {
        "id": "COV-18-CMS_DASHBOARD_BACKEND",
        "q": "Across the org KB, locate repo cms-dashboard-backend: primary module paths and top handlers for a production bug.",
        "repos": ["cms-dashboard-backend"],
        "must": ["cms-dashboard-backend"],
    },
    {
        "id": "COV-22-RAVEN",
        "q": "Across the org KB, locate repo raven: primary module paths and top handlers for a production bug.",
        "repos": ["raven"],
        "must": ["raven"],
    },
    {
        "id": "COV-23-FABRIC",
        "q": "Across the org KB, locate repo fabric: primary module paths and top handlers for a production bug.",
        "repos": ["fabric"],
        "must": ["fabric"],
    },
    {
        "id": "COV-24-GO_RADIOLY",
        "q": "Across the org KB, locate repo go-radioly: primary module paths and top handlers for a production bug.",
        "repos": ["go-radioly"],
        "must": ["go-radioly"],
    },
    {
        "id": "COV-P2-POCKET_SEARCH",
        "q": "Across the org KB, locate repo pocket_search: primary module paths and top handlers for a production bug.",
        "repos": ["pocket_search"],
        "must": ["pocket_search"],
    },
    {
        "id": "COV-P2-LITEFM",
        "q": "Across the org KB, locate repo litefm-backend: primary module paths and top handlers for a production bug.",
        "repos": ["litefm-backend"],
        "must": ["litefm-backend"],
    },
    {
        "id": "COV-P2-NOVELS_KAFKA",
        "q": "Across the org KB, locate repo novels-kafka-stream-client: primary module paths for a production bug.",
        "repos": ["novels-kafka-stream-client"],
        "must": ["novels-kafka"],
    },
    {
        "id": "COV-19-INFRA_DEPLOYMENTS_K8S",
        "q": "Across the org KB, locate repo infra-deployments-k8s / Infra_deployments_k8s: service onboarding docs and overlay layout.",
        "repos": ["infra-deployments-k8s"],
        "must": ["SERVICE_ONBOARDING", "overlay"],
    },
    {
        "id": "COV-20-INFRA_K8S",
        "q": "Across the org KB, locate repo infra-k8s / Infra_k8s: ArgoCD Root Apps ownership.",
        "repos": ["infra-k8s"],
        "must": ["Root Apps", "Argo"],
    },
    {
        "id": "COV-P3-INFRA_DOCS",
        "q": "Across the org KB, locate repo infra-docs: kubernetes docs and EKS migration notes.",
        "repos": ["infra-docs"],
        "must": ["infra-docs", "kubernetes"],
    },
    {
        "id": "COV-P2-MEDIA_FORGE",
        "q": "Across the org KB, locate media-forge: CDN image delivery and deploy overlays.",
        "repos": ["media-forge"],
        "must": ["media-forge", "cdn"],
    },
    {
        "id": "COV-P2-UGC_BACKEND",
        "q": "Across the org KB, locate ugc-backend: creator backend deploy overlays (not writers-backend).",
        "repos": ["ugc-backend"],
        "must": ["ugc-backend"],
    },
    {
        "id": "COV-P2-UGC_UI",
        "q": "Across the org KB, locate ugc-ui: creator web UI deploy overlays.",
        "repos": ["ugc-ui"],
        "must": ["ugc-ui"],
    },
    {
        "id": "COV-P2-UGC_TTS",
        "q": "Across the org KB, locate ugc-tts-worker / ugc-tts-audio-generation Temporal worker overlays.",
        "repos": ["ugc-tts-worker"],
        "must": ["ugc-tts", "temporal"],
    },
]


@dataclass
class Result:
    case_id: str
    pass_: bool
    misses: list[str]
    answer: str
    repos_hit: list[str]


def query(base: str, ask: str) -> dict:
    req = urllib.request.Request(
        f"{base.rstrip('/')}/query",
        data=json.dumps({"query": ask, "mode": "hybrid", "top_k": 8}).encode(),
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def score(case: dict, payload: dict) -> Result:
    answer = str(payload.get("response") or "")
    blob_parts = [answer]
    data = payload.get("data") or {}
    for ent in data.get("entities") or []:
        blob_parts.append(json.dumps(ent))
    for ref in payload.get("references") or []:
        blob_parts.append(json.dumps(ref))
    blob = "\n".join(blob_parts).lower()
    misses: list[str] = []
    repos_hit = []
    for repo in case["repos"]:
        if repo.lower() in blob:
            repos_hit.append(repo)
        else:
            misses.append(f"repo:{repo}")
    for token in case.get("must") or []:
        if token.lower() not in blob:
            misses.append(f"must:{token}")
    path_sub = case.get("path_sub")
    if path_sub and path_sub.lower() not in blob:
        misses.append(f"path:{path_sub}")
    return Result(
        case_id=case["id"],
        pass_=not misses,
        misses=misses,
        answer=answer[:500],
        repos_hit=repos_hit,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:9621")
    parser.add_argument(
        "--out",
        default="org-handbook/lightrag/slots/live/p0-gold-report.md",
    )
    args = parser.parse_args()
    results: list[Result] = []
    for case in CASES:
        try:
            payload = query(args.base_url, case["q"])
            results.append(score(case, payload))
        except Exception as exc:  # noqa: BLE001
            results.append(
                Result(
                    case_id=case["id"],
                    pass_=False,
                    misses=[f"error:{exc}"],
                    answer="",
                    repos_hit=[],
                )
            )
    passed = sum(1 for r in results if r.pass_)
    lines = [
        "# P0 gold suite report",
        "",
        f"Base URL: `{args.base_url}`",
        f"Score: **{passed}/{len(results)}** passed",
        "",
        "| Case | Pass | Misses | Repos hit |",
        "|---|---|---|---|",
    ]
    for r in results:
        lines.append(
            f"| {r.case_id} | {'yes' if r.pass_ else 'no'} | "
            f"{', '.join(r.misses) or '—'} | {', '.join(r.repos_hit) or '—'} |"
        )
    lines.append("")
    lines.append("## Miss detail")
    for r in results:
        if r.pass_:
            continue
        lines.append(f"### {r.case_id}")
        lines.append(f"- Misses: {', '.join(r.misses)}")
        lines.append(f"- Answer excerpt: {r.answer[:300] or '(empty)'}")
        lines.append("")
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{passed}/{len(results)} passed → {out}")
    for r in results:
        flag = "PASS" if r.pass_ else "MISS"
        print(f"  {flag} {r.case_id} {';'.join(r.misses)}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
