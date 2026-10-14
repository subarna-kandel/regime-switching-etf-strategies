# Data Documentation: Regime-Switching ETF Strategies

## Directory Structure
- `raw/`: Daily ETF and index pricing series from Yahoo Finance (SPY, TLT, GLD, EWZ, ^VIX).
- `processed/`: Daily log-returns, daily VIX changes ($\Delta	ext{VIX}$), rolling technical indicators, and hidden Markov regime probability distributions.

## Data Sources & Acquisition
- **Acquisition Pipeline**:
  Downloaded programmatically via `yfinance`:
  - `^VIX`: CBOE Volatility Index (used to estimate Hidden Markov Model regimes).
  - `SPY`, `TLT`, `GLD`: Liquid asset universe representing US Equities, Long-Term Treasuries, and Gold.
  - `EWZ`: iShares MSCI Brazil ETF (for technical indicator trend classification).
- **Processing**:
  1. Missing prices forward-filled and aligned across trading days.
  2. First-differencing of VIX level: $\Delta	ext{VIX}_t = 	ext{VIX}_t - 	ext{VIX}_{t-1}$.
  3. Return calculation and regime-conditional strategy returns computation (`src/data.py`).
