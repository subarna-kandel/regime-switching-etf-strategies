# Research & Methodology Summary: Regime-Switching ETF Strategies

## 1. Executive Overview
This research formulates an institutional tactical asset allocation strategy utilizing Gaussian Hidden Markov Models (HMM) on market volatility dynamics ($\Delta	ext{VIX}$) to dynamically shift capital across US Equities (SPY), Long-Term Treasuries (TLT), and Gold (GLD).

## 2. Strategy Architecture
- **State Estimation**: A 3-state Gaussian HMM is calibrated on daily changes in the CBOE Volatility Index ($\Delta	ext{VIX}$), classifying markets into:
  1. Low-Volatility / Bullish Expansion (State 0)
  2. Transition / Normal Volatility (State 1)
  3. High-Volatility / Crisis Panic (State 2)
- **Allocation Rules**:
  - State 0: Overweight Equities (SPY)
  - State 1: Balanced allocation across SPY, TLT, and GLD
  - State 2: Flight-to-safety capital preservation in Treasuries (TLT) and Gold (GLD)
- **Technical Signals**: Moving average and momentum filters applied to emerging equity assets (EWZ) to generate standalone directional forecasts.

## 3. Performance & Backtest Results
- **Drawdown Abatement**: The dynamic HMM rotation strategy significantly curtailed peak-to-trough drawdowns during severe equity market corrections relative to static SPY buy-and-hold.
- **Risk-Adjusted Return**: Improved risk-adjusted metrics (Sharpe ratio and Sortino ratio) resulting from timely flight-to-safety asset rotation.
- **Regime Persistence**: Transition probability matrices revealed that high-volatility crisis states exhibit rapid clustering and mean-reversion characteristics.

## 4. Key Risks & Implementation Frictions
- High turnover during volatile transition phases can create trading fee drag; incorporating turnover penalties is recommended.
