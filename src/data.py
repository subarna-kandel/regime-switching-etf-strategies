"""Market data download and return processing for ETFs and VIX."""

import numpy as np
import pandas as pd
import yfinance as yf


def download_asset_data(tickers=['SPY', 'TLT', 'GLD', '^VIX'], start_date='2010-01-01', end_date=None):
    """Download historical price series for ETFs and VIX index."""
    df = yf.download(tickers, start=start_date, end=end_date, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        prices = df['Adj Close'] if 'Adj Close' in df.columns.levels[0] else df['Close']
    else:
        prices = df['Adj Close'] if 'Adj Close' in df else df['Close']
    prices = prices.dropna()
    return prices


def compute_vix_changes_and_returns(prices_df):
    """Calculate daily ETF log-returns and first-differenced VIX level."""
    log_rets = np.log(prices_df[['SPY', 'TLT', 'GLD']] / prices_df[['SPY', 'TLT', 'GLD']].shift(1)).dropna()
    vix_series = prices_df['^VIX'].reindex(log_rets.index)
    dvix = vix_series.diff().dropna()
    combined = log_rets.loc[dvix.index].copy()
    combined['DVIX'] = dvix
    return combined
