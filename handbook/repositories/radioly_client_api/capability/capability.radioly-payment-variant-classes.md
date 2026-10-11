---
id: capability.radioly-payment-variant-classes
type: capability
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/experiments/coin_pricing_exp/base_exp.py#ShowDiscountingBase
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/experiments/coin_pricing_exp/coin_pack_base_discount_exp.py#CoinPackBaseDiscountExp
---

**Aliases:** payment variant classes

**When to use:** Locate a variant class in this package. Not the live allocation table and not percentages. Class names: ShowDiscountingBase, CoinPackBaseDiscountExp, EnglishShowPricingExp, DiscountOnESShowExp, SpanishExperimentUsers, FirstEpPricingExpIndia, FirstEpPricingExpUS, AllocateHandler, CoinPricingHandler, DiscountFactorEnum, CoinSubscriptionExperiment, DailyUnlockUXExp, normalize_hours, DSPavoResult, DSPavoSaleResult, DSPavoExperiment, _parse_json_dict, _is_valid_ranked_section, _is_empty_ranked_section, _ranked_plan_ids, _offer_plan_ids_from_entries, _normalize_offer_plan_dict, _normalize_offer_plan, _parse_ranking_plan_ranks, _parse_sale_plan_ranks, DSPavoFetcher, push_pre_pavo_log, fetch_pavo_extra_plans, _add_plans_to_lookup, _build_plan_lookup, _update_ranked_section, apply_pavo_override, _section_has_plans, rebuild_coins_module_order, _apply_ranking_pavo_override, apply_pavo_to_response, _InertSubscriptionImpressions, _DSSaleAssetHost, resolve_ds_sale_asset_config, _plan_from_config, _creative_plan, bind_ds_sale_asset_host, dispatch_ds_sale_asset, is_ds_sale_asset_function, is_ds_sale_plan_function, DSPavoSaleExperiment, get_ds_sale_state, _apply_sale_pack_timer_helpers, attach_ds_sale_offer_plans, ds_sale_popup_feature, ds_sale_popup_capped_frequency_data, ds_sale_popup_frequency_data, increment_ds_sale_popup_impression, resolve_ds_sale_surface, _plan_with_highest_bonus, serialize_frozen_plans, deserialize_frozen_plans, DSPavoSaleWindowState, _format_utc_iso, _parse_iso_datetime. Plus 34 more classes in the same package.

**Required inputs:** the class name or the listener surface. Cohort rules stay on capability.radioly-experiment-allocation.
