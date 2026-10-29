# Assumptions

Every guessed number in riftroute is listed here. Each one is a placeholder to
replace with a measurement; when that happens, move it to "Measured" with its
date and source.

## Open

Values in `src/riftroute/data/scenarios/peak_day.json`, taken from the project
plan on 29 October 2026. None has been measured.

| Key | Value | Unit | Why this guess | Replace with |
|---|---|---|---|---|
| `decay_k_per_hour` | 0.08 | 1/h | Placeholder; no source gives a decay rate for green leaf | A measured rate, or a source |
| `clerk_setup_min` | 5.0 | min | Placeholder setup time per stop | Timed at a buying centre |
| `clerk_weigh_rate_kg_per_min` | 28.0 | kg/min | Placeholder weighing rate | Timed at a buying centre |
| `factory_offload_kg_per_hour` | 12000 | kg/h | Placeholder offloading rate | Field question 3 |
| `fleet[L1].capacity_kg` | 10000 | kg | Placeholder lorry capacity | Factory or driver |
| `fleet[L1].speed_tarmac_kmh` | 50 | km/h | Placeholder lorry speed on tarmac | Timed trips, or Phase 2 OSM speeds checked against Google Maps |
| `fleet[L1].speed_murram_kmh` | 22 | km/h | Placeholder lorry speed on murram | As above |
| `centres[1].normal_leaf_kg` | 650 | kg | Placeholder normal-day leaf | Field question 4 |
| `centres[1].peak_leaf_kg` | 1450 | kg | Placeholder peak-day leaf | Field question 4 |
| `centres[1].mean_pluck_hour` | 8.0 | hour of day | Placeholder mean plucking time | Clerk or farmers |
| `centres[1].eta_window` | [10.5, 12.0] | hours of day | Placeholder arrival window | Field question 2 |

The scenario has one lorry and one centre. The v0.1 scope is 3 lorries and
10 centres; add their entries here before adding them to the scenario file.

Phase 2 adds another assumption: OSMnx edge speeds come from OpenStreetMap tags
or road-type averages, not from lorries.

## Measured

None yet.
