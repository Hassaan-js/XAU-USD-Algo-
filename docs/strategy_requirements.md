# Strategy Requirements (VSA + CAB + CISD)

This repository is backtest-only until the live execution layer is built. The
`VSACABCISDStrategy` placeholder exists to capture the *exact* rules needed to
implement the strategy. Please provide clear definitions so the strategy can be
translated into deterministic code.

## Required Definitions

### 1) VSA (Volume Spread Analysis)
- **Setup/conditions:** (e.g., No Supply, No Demand, Stopping Volume, Climactic)
- **Volume benchmark:** (relative to what window/average?)
- **Candle spread definition:** (body vs. total range rules)
- **Confirmation rules:** (what validates the setup?)
- **Invalidation rules:** (what cancels it?)

### 2) CAB
- **Full acronym and meaning:**
- **Market structure requirements:** (trend, range, breakout?)
- **Trigger conditions:** (price action pattern, indicator filter)
- **Stop loss rule:** (fixed %, ATR-based, structure-based)
- **Take profit rule:** (fixed RR, partials, trailing)

### 3) CISD
- **Full acronym and meaning:**
- **Entry trigger:** (pattern, indicator, time filter)
- **Exit trigger:** (target, time-based, opposing signal)
- **Position sizing:** (risk per trade, max concurrent trades)

## Execution Constraints
- **Instrument(s):** (e.g., XAU/USD)
- **Timeframe:** (e.g., 5m, 1h, 1d)
- **Session:** (e.g., London, NY, all sessions)
- **Max trades/day:**
- **Max risk/day:**
- **Allowed order types:** (market/limit/stop)

## Examples (Optional)
- Provide 2–3 annotated examples of valid setups with timestamps.

Once this is complete, the strategy can be implemented in
`strategy/vsa_cab_cisd.py` and wired into the backtest/live engine.
