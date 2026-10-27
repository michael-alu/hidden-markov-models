"""
Shared record shapes for the HMM activity recognition notebook.

Import from the notebook: from hmm_types import SamplingRateRow, WindowFeatures
"""

from typing import TypedDict


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
