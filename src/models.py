"""Gaussian Hidden Markov Models (HMM) and regime-dependent allocation."""

import numpy as np
from hmmlearn.hmm import GaussianHMM


def fit_gaussian_hmm(dvix_series, n_states=3, random_state=42):
    """Fit Gaussian Hidden Markov Model to daily VIX changes."""
    X = np.asarray(dvix_series).reshape(-1, 1)
    model = GaussianHMM(n_components=n_states, covariance_type="diag", n_iter=1000, random_state=random_state)
    model.fit(X)
    hidden_states = model.predict(X)
    return model, hidden_states


def order_states_by_volatility(model, hidden_states):
    """Map arbitrary HMM state labels to low, medium, and high volatility regimes."""
    means = model.means_.flatten()
    sorted_order = np.argsort(means)
    mapping = {old_st: new_st for new_st, old_st in enumerate(sorted_order)}
    ordered_states = np.array([mapping[s] for s in hidden_states])
    return ordered_states, sorted_order
