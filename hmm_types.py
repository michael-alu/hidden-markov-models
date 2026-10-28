"""
Shared record shapes for the HMM activity recognition notebook.

Import from the notebook: from hmm_types import SamplingRateRow, WindowFeatures, HmmModel, ActivityMetrics, SessionAccuracy, ModelComparisonRow, FeatureAblationRow
"""

from typing import TypedDict

import numpy as np


class SamplingRateRow(TypedDict):
    recording: str
    duration_seconds: float
    accelerometer_hz: float
    gyroscope_hz: float


class WindowFeatures(TypedDict):
    acc_mean: float
    acc_std: float
    gyro_mean: float
    sma: float
    tilt_degrees: float
    yz_correlation: float
    dominant_frequency: float
    spectral_energy: float


class HmmModel(TypedDict):
    start_probabilities: np.ndarray
    transition_matrix: np.ndarray
    means: np.ndarray
    variances: np.ndarray


class ActivityMetrics(TypedDict):
    activity: str
    samples: int
    sensitivity: float
    specificity: float
    accuracy: float


class SessionAccuracy(TypedDict):
    session: str
    accuracy: float


class ModelComparisonRow(TypedDict):
    session: str
    learned_log_likelihood: float
    realistic_log_likelihood: float
    learned_switches: int
    realistic_switches: int
    windows_that_differ: int


class FeatureAblationRow(TypedDict):
    features: str
    accuracy: float
