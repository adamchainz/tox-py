from __future__ import annotations

import os
import sys
from contextlib import contextmanager
from pathlib import Path
from textwrap import dedent

import tox
from _pytest.capture import CaptureFixture


@contextmanager
def chdir(path):
    original = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(original)


def run_tox(
    capfd: CaptureFixture[str], path: Path, args: list[str]
) -> tuple[int | str | None, str, str]:
    try:
        with chdir(path):  # pragma: no branch
            tox.cmdline(["tox"] + args)
    except SystemExit as exc:
        code = exc.code

    out, err = capfd.readouterr()
    return code, out, err


def test_current(capfd, tmp_path):
    tox_name = f"py{sys.version_info[0]}{sys.version_info[1]}"
    (tmp_path / "tox.ini").write_text(
        dedent(
            f"""
        [tox]
        skipsdist = true
        skip_install = true
        envlist = {tox_name}

        [testenv]
        commands = python --version
        """
        )
    )

    return_code, out, err = run_tox(capfd, tmp_path, ["--py", "current"])

    assert return_code == 0
    version = sys.version.split(" ")[0]
    assert f"Python {version}" in out.splitlines()
