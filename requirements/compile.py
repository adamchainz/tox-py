#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    os.environ["CUSTOM_COMPILE_COMMAND"] = "requirements/compile.py"
    os.environ.pop("PIP_REQUIRE_VIRTUALENV", None)
    common_args = [
        "-m",
        "piptools",
        "compile",
        "--generate-hashes",
        "--allow-unsafe",
    ] + sys.argv[1:]
    subprocess.run(
        ["python3.6", *common_args, "-P", "tox<4", "-o", "py36-tox3.txt"],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["python3.7", *common_args, "-P", "tox<4", "-o", "py37-tox3.txt"],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["python3.8", *common_args, "-P", "tox<4", "-o", "py38-tox3.txt"],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["python3.9", *common_args, "-P", "tox<4", "-o", "py39-tox3.txt"],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["python3.10", *common_args, "-P", "tox<4", "-o", "py310-tox3.txt"],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["python3.6", *common_args, "-P", "tox>=4.0.0a8", "-o", "py36-tox4.txt"],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["python3.7", *common_args, "-P", "tox>=4.0.0a8", "-o", "py37-tox4.txt"],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["python3.8", *common_args, "-P", "tox>=4.0.0a8", "-o", "py38-tox4.txt"],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["python3.9", *common_args, "-P", "tox>=4.0.0a8", "-o", "py39-tox4.txt"],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["python3.10", *common_args, "-P", "tox>=4.0.0a8", "-o", "py310-tox4.txt"],
        check=True,
        capture_output=True,
    )
