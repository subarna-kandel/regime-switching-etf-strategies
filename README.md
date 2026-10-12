# Systematic Investing and Backtests

Exploratory market-regime and technical-indicator workflows for ETF allocation and prediction.

## Research modules

- Gaussian HMM regimes from VIX changes and ETF rotation versus benchmarks.
- Technical-indicator generation and machine-learning experiments for EWZ.

## Execution and interpretation

Install dependencies from `requirements.txt` and run in Jupyter. Market histories are retrieved online and can change. The technical-indicator notebook uses `pandas_ta`; dependency compatibility may need adjustment.

Use strictly walk-forward estimation for regime-to-asset selection and review the feature/label split for temporal leakage before describing results as out of sample.
