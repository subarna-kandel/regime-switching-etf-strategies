"""Unit tests for Gaussian HMM regime estimation and tactical ETF backtesting."""

import sys
import os
import unittest
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.features import compute_technical_indicators, compute_rsi
from src.evaluation import compute_max_drawdown, evaluate_etf_strategy


class TestRegimeSwitchingStrategies(unittest.TestCase):

    def setUp(self):
        np.random.seed(42)
        self.rets = pd.Series(np.random.normal(0.0006, 0.01, 200))

    def test_compute_max_drawdown(self):
        # Known series: drops from 1.0 to 0.70 = -30% drawdown
        series = pd.Series([0.1, -0.2, -0.15, 0.05, 0.1])
        mdd = compute_max_drawdown(series)
        self.assertLess(mdd, -0.25)
        self.assertGreater(mdd, -0.40)

    def test_evaluate_etf_strategy_metrics(self):
        metrics = evaluate_etf_strategy(self.rets)
        self.assertIn('Total Return', metrics)
        self.assertIn('Annualized Return', metrics)
        self.assertIn('Annualized Volatility', metrics)
        self.assertIn('Sharpe Ratio', metrics)
        self.assertIn('Max Drawdown', metrics)
        self.assertLessEqual(metrics['Max Drawdown'], 0.0)

    def test_compute_rsi(self):
        prices = pd.Series(np.linspace(100, 150, 30))  # strictly rising series
        rsi = compute_rsi(prices, period=14).dropna()
        self.assertGreater(rsi.iloc[-1], 90.0)

    def test_compute_technical_indicators(self):
        df = pd.DataFrame({'Close': np.cumsum(np.random.normal(0.1, 1.0, 100)) + 100.0})
        feats = compute_technical_indicators(df, price_col='Close')
        self.assertIn('SMA_20', feats.columns)
        self.assertIn('SMA_50', feats.columns)
        self.assertIn('RSI_14', feats.columns)
        self.assertIn('Vol_20', feats.columns)
        self.assertEqual(len(feats), 51)  # 100 - 50 + 1 (SMA_50 window)


if __name__ == '__main__':
    unittest.main()
