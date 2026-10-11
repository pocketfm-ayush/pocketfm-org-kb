# S2S health check

## Journey
1. Attribution/S2S exporters deliver events (Relay and/or kafka workers and/or Airflow jobs).
2. S2S mismatch validation jobs compare expected vs observed signals.
3. Marketing reports/insights jobs may surface related campaign health.
4. Operators fix the owning pipeline (confirm Airflow vs Relay vs kafka).

## Modules
- [s2s-attribution-jobs](../modules/s2s-attribution-jobs.md)
- [s2s-mismatch-validation](../modules/s2s-mismatch-validation.md)
- [facebook-campaign-insights](../modules/facebook-campaign-insights.md)
- [appsflyer-audience-export](../modules/appsflyer-audience-export.md)

## Failure modes
- False alarms when ownership is the wrong service.
- Fixing Airflow when Relay exporter is the actual drop.
