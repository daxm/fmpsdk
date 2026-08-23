"""fmpsdk — a Python SDK for the Financial Modeling Prep (FMP) API.

>>> import fmpsdk
>>> client = fmpsdk.Client()  # reads FMP_API_KEY from the environment
>>> client.search.search_symbol(query="AAPL")
"""

from .client import Client
from .exceptions import (
    FMPAuthenticationError,
    FMPError,
    FMPNotFoundError,
    FMPPlanLimitError,
    FMPRateLimitError,
    FMPServerError,
    FMPValidationError,
)

__version__ = "20250102.0"

__all__ = [
    "Client",
    "FMPAuthenticationError",
    "FMPError",
    "FMPNotFoundError",
    "FMPPlanLimitError",
    "FMPRateLimitError",
    "FMPServerError",
    "FMPValidationError",
]
