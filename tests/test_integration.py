import os
import sys
from contextlib import contextmanager
from textwrap import dedent

import tox


@contextmanager
def chdir(path):
    original = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(original)


def run_tox(capfd, path, args):
    try:
        with chdir(path):
            tox.cmdline(["tox"] + args)
    except SystemExit as exc:
        code = exc.code

    out, err = capfd.readouterr()
    return code, out, err


def test_current(capfd, tmp_path):
    (tmp_path / "tox.ini").write_text(
        dedent(
            """
        [tox]
        skipsdist = true
        skip_install = true
        envlist =
            py{36,37,38,39}

        [testenv]
        commands = python --version
        """
        )
    )

    return_code, out, err = run_tox(capfd, tmp_path, ["--py", "current"])

    assert return_code == 0
    version = ".".join(str(x) for x in sys.version_info[:3])
    assert f"Python {version}" in out.splitlines()
