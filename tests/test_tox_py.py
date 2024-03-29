from __future__ import annotations

import os
from argparse import ArgumentTypeError
from types import SimpleNamespace
from unittest import mock

import pytest
from tox.config.parallel import ENV_VAR_KEY_PUBLIC as TOX_PARALLEL_ENV

from tox_py import parse_py
from tox_py import tox_configure


class TestParsePy:
    def test_current(self):
        assert parse_py("current") == "current"

    def test_310_accepted(self):
        assert parse_py("310") == "310"

    def test_anything_else_rejected(self):
        with pytest.raises(ArgumentTypeError) as excinfo:
            parse_py("something")

        assert excinfo.value.args == (
            "'something' is not 'current' or Python version reference.",
        )


class TestToxConfigure:
    def test_parallel(self):
        with mock.patch.dict(os.environ, {TOX_PARALLEL_ENV: "1"}):
            result = tox_configure(None)

        assert result is None

    def test_env_set_env_var(self):
        with mock.patch.dict(os.environ, {"TOXENV": "py39"}):
            result = tox_configure(None)

        assert result is None

    def test_env_set_arg(self):
        config = SimpleNamespace(option=SimpleNamespace(env="py39"))

        result = tox_configure(config)

        assert result is None

    def test_py_not_set(self):
        config = SimpleNamespace(option=SimpleNamespace(env=None, py=None))

        result = tox_configure(config)

        assert result is None

    def test_py_set(self):
        config = SimpleNamespace(
            envlist=[
                "py38",
                "py38-something",
                "py39",
                "py39-something",
            ],
            option=SimpleNamespace(env=None, py="39"),
        )

        result = tox_configure(config)

        assert result is None
        assert config.envlist == ["py39", "py39-something"]
