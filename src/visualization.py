"""Visualizations for regime transitions, return distributions, and drawdown charts."""

import matplotlib.pyplot as plt
import numpy as np


def plot_regimes_over_time(price_series, regime_series, title="Regime Classification Over Time"):
    """Plot price chart overlaid with color-coded HMM regimes."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(price_series.index, price_series, color='black', alpha=0.6, label='Price')
    colors = ['green', 'orange', 'red']
    for st in np.unique(regime_series):
        mask = (regime_series == st)
        ax.scatter(price_series.index[mask], price_series[mask], s=4, label=f'Regime {st}')
    ax.set_title(title)
    ax.legend()
    plt.tight_layout()
    return fig
