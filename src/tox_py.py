from __future__ import annotations

import argparse
import os
import sys
from typing import Any

import tox
from tox.config.parallel import ENV_VAR_KEY_PUBLIC as TOX_PARALLEL_ENV


def parse_py(string: str) -> str:
    if string == "current":
        return string
    if string.isdigit():
        return string
    raise argparse.ArgumentTypeError(
        f"{string!r} is not 'current' or Python version reference."
    )


@tox.hookimpl  # type: ignore [misc]
def tox_addoption(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--py",
        type=parse_py,
        help="run environments only matching this Python version.",
    )


@tox.hookimpl  # type: ignore [misc]
def tox_configure(config: Any) -> None:
    # Run on the main tox process but not in the parallelized subprocesses,
    # where the subprocess has been delegated a specific TOX_PARALLEL_ENV.
    if TOX_PARALLEL_ENV in os.environ:
        return

    # Do not do anything when tox env is specified
    if "TOXENV" in os.environ or config.option.env:
        return

    if config.option.py is not None:
        py = config.option.py
        if py == "current":
            py = "".join(str(x) for x in sys.version_info[:2])

        prefix = f"py{py}"
        config.envlist = [env for env in config.envlist if env.startswith(prefix)]

        # Set config.envlist_default to fix 'tox -l' - copying tox-factor
        config.envlist_default = config.envlist
