"""Strategy backtesting, Sharpe ratio, and Maximum Drawdown metrics."""

import numpy as np
import pandas as pd


def compute_max_drawdown(return_series):
    """Compute peak-to-trough maximum drawdown."""
    cum = (1.0 + return_series).cumprod()
    peak = cum.cummax()
    dd = (cum - peak) / peak
    return float(dd.min())


def evaluate_etf_strategy(strategy_returns, periods_per_year=252):
    """Compute annualized return, annualized volatility, Sharpe ratio, and max drawdown."""
    total_ret = (1.0 + strategy_returns).prod() - 1.0
    n = len(strategy_returns)
    ann_ret = (1.0 + total_ret) ** (periods_per_year / max(n, 1)) - 1.0
    ann_vol = strategy_returns.std() * np.sqrt(periods_per_year)
    sharpe = ann_ret / ann_vol if ann_vol > 1e-8 else 0.0
    mdd = compute_max_drawdown(strategy_returns)
    return {
        'Total Return': total_ret,
        'Annualized Return': ann_ret,
        'Annualized Volatility': ann_vol,
        'Sharpe Ratio': sharpe,
        'Max Drawdown': mdd
    }
