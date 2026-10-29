# riftroute

Open-source simulator for green leaf tea collection routing at Kenyan tea factories.
Litein is the first example catchment.

## Stack
- Python (uv), Rust core via PyO3 + maturin (src/lib.rs -> riftroute._core)
- OSMnx + NetworkX for roads, NumPy/SciPy for numbers

## Commands
- Tests: `uv run pytest`
- Lint: `uv run ruff check .`

## Rules
- No formula in code that is not derived in docs/maths.md first.
- Every guessed number goes in docs/assumptions.md, never hard-coded silently.
- Coordinates are stored as (lat, lon); convert to (lon, lat) only in code.
