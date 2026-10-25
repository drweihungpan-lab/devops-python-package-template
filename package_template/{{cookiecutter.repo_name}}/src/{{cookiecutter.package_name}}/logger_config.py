"""
This module contains a function to configure the logger.
"""

import logging
import os


def configure_logger():
    """Configure the logger"""
    configured_logger = logging.getLogger(__name__)
    LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
    logging.basicConfig(
        format="%(asctime)s (from %(funcName)s) %(levelname)s: %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
        level=LOGLEVEL,
    )
    return configured_logger


# Call the function to configure the logger
logger = configure_logger()
