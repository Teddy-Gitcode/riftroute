# riftroute

An open-source discrete-time simulator for green leaf tea collection routing at
Kenyan tea factories. A factory catchment is modelled from its real road
network; one example catchment is included.

**Status:** pre-alpha (v0.0.x). The package installs and the input data files
exist. The road graph, routing and simulation are not implemented yet, and the
project has produced no results.

## Research question

Green leaf loses quality between plucking and processing. For a given factory
catchment, fleet and day:

> Which buying centres deliver leaf to the factory outside the regulatory time
> limit, and does a dynamic dispatch rule reduce this compared with the fixed
> collection schedule?

## Regulatory constraints

These limits are taken from the *Green Leaf Quality Requirements for the Kenya
Tea Industry* (Ministry of Agriculture) and are treated as fixed inputs.

| Constraint | Limit | Section |
|---|---|---|
| Buying centre to factory | 2 hours | 1.2.4(a) |
| Vehicle turnaround | 3 hours | 1.2.5(a) |
| Weight per bag | 12 kg | 1.2.4(d) |

## Planned method

1. **Road network.** Build a directed graph of the catchment's roads from
   OpenStreetMap and snap the factory and buying centres to it.
2. **Travel times.** Compute a travel-time matrix between all sites by shortest
   path.
3. **Simulation.** Step through a collection day at a fixed time step. Each
   lorry moves through the states depart, travel, load, travel, queue, offload.
4. **Baseline and comparison.** Run the fixed schedule and a dynamic dispatch
   rule on the same inputs and report the difference.

Every formula is derived in `docs/maths.md` before it is implemented.

## Data provenance

Each input value belongs to exactly one class, and the classes are stored in
separate files so that any result can state what it rests on.

| Class | Meaning | Location |
|---|---|---|
| Verified | Checked against a cited source | `src/riftroute/data/rules.json` |
| Observed | Site locations, with the date each was confirmed | `src/riftroute/data/catchments/<name>/nodes.json` |
| Assumed | Placeholder until measured | `src/riftroute/data/catchments/<name>/scenarios/`, listed in `docs/assumptions.md` |

## Catchments

The code contains no site-specific logic. A catchment is a data folder:

```
src/riftroute/data/
├── rules.json              national rules, shared by all catchments
└── catchments/
    └── example/
        ├── nodes.json      factory and buying-centre locations
        └── scenarios/      fleet, leaf volumes and rates for a modelled day
```

Modelling another factory means adding a folder with the same structure.

## Limitations

- All scenario parameters (leaf weights, decay rate, vehicle speeds, weighing
  and offloading rates) are currently assumptions. None has been measured.
- Site coordinates in the example catchment have not yet been confirmed on
  satellite imagery or on the ground.
- Road speeds will come from OpenStreetMap tags and road-type averages, not
  from observed lorry speeds.
- The model has not been validated against factory records. Validation against
  field data and review by a tea collection worker are planned before v1.0.

## Roadmap

| Phase | Work | State |
|---|---|---|
| 0 | Package and repository | Done |
| 1 | Site locations and input data files | In progress |
| 2 | Road graph and travel-time matrix | Not started |
| 3 | Shortest paths and fixed-schedule baseline | Not started |
| 4 | Simulation engine | Not started |
| 5 | Dispatch rule and benchmark | Not started |
| 6 | Map output | Not started |
| 7 | Rust implementation of the inner loop, if profiling shows a need | Not started |
| 8 | Release v0.1.0 | Not started |
| 9 | Validation and external review | Not started |

## Installation

```
pip install riftroute
```

## Development

Requires [uv](https://docs.astral.sh/uv/) and a Rust toolchain.

```
git clone https://github.com/Teddy-Gitcode/riftroute
cd riftroute
uv run pytest
uv run ruff check .
```

## Licence and data sources

Code is released under Apache-2.0. Road data is from OpenStreetMap
contributors under the ODbL.
