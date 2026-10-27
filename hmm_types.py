"""
Shared record shapes for the HMM activity recognition notebook.

Import from the notebook: from hmm_types import SamplingRateRow
"""

from typing import TypedDict


class SamplingRateRow(TypedDict):
    recording: str
    duration_seconds: float
    accelerometer_hz: float
    gyroscope_hz: float
