======
tox-py
======

.. image:: https://img.shields.io/github/workflow/status/adamchainz/tox-py/CI/main?style=for-the-badge
   :target: https://github.com/adamchainz/tox-py/actions?workflow=CI

.. image:: https://img.shields.io/badge/Coverage-100%25-success?style=for-the-badge
   :target: https://github.com/adamchainz/tox-py/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/tox-py.svg?style=for-the-badge
   :target: https://pypi.org/project/tox-py/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

..

Adds the ``--py`` flag to tox to run environments matching a given Python interpreter.

Installation
============

Use **pip**:

.. code-block:: bash

    python -m pip install tox-py

Python 3.7 to 3.10 supported.

Only tox 3 is supported.
On tox 4, ensure only your target Python version is installed, and run ``tox --skip-missing-interpreters``.
(`See discussion <https://github.com/adamchainz/tox-py/issues/34#issuecomment-908456003>`__.)

----

**Testing a Django project?**
Check out my book `Speed Up Your Django Tests <https://adamchainz.gumroad.com/l/suydt>`__ which covers loads of ways to write faster, more accurate tests.

----

Usage
=====

After installation, the plugin will be automatically picked up by ``tox``.
It adds one argument: ``--py``, which takes the version to filter environments against.
The version can be specified either as a ``tox.ini``-style dotless version number, or the special string ``current`` for the version of Python that ``tox`` is running under.

For example, to run all Python 3.9 environments:

.. code-block:: sh

    tox --py 39

Or to run all environments matching the version of Python that ``tox`` is running under:


.. code-block:: sh

    tox --py current

This makes configuring CI really easy: configure your CI to trigger each Python version in parallel, running ``tox --py current``.
