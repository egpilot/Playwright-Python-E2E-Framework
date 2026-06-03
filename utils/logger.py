"""Centralized logging setup."""
import logging
import sys
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "reports" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name: str = "qa") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    fh = logging.FileHandler(LOG_DIR / "test_run.log")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    return logger
