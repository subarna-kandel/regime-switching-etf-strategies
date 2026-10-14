"""Technical indicators and volatility feature extraction."""

import numpy as np
import pandas as pd


def compute_technical_indicators(df, price_col='Close'):
    """Compute moving average, momentum, and volatility indicators."""
    res = pd.DataFrame(index=df.index)
    p = df[price_col]
    res['SMA_20'] = p.rolling(20).mean()
    res['SMA_50'] = p.rolling(50).mean()
    res['RSI_14'] = compute_rsi(p, 14)
    res['Vol_20'] = p.pct_change().rolling(20).std() * np.sqrt(252)
    return res.dropna()


def compute_rsi(series, period=14):
    """Compute Relative Strength Index (RSI)."""
    delta = series.diff()
    gain = (delta.where(delta > 0, 0.0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0.0)).rolling(period).mean()
    rs = gain / (loss + 1e-10)
    return 100.0 - (100.0 / (1.0 + rs))
