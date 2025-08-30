installkernel_wsl
=================

.. only:: html

   .. image:: https://img.shields.io/pypi/pyversions/installkernel-wsl.svg?color=blue&logo=python&logoColor=white
      :target: https://www.python.org/
      :alt: Python versions

   .. image:: https://img.shields.io/pypi/v/installkernel-wsl
      :target: https://pypi.org/project/installkernel-wsl/
      :alt: PyPI Version

   .. image:: https://img.shields.io/github/v/tag/Tatsh/installkernel-wsl
      :target: https://github.com/Tatsh/installkernel-wsl/tags
      :alt: GitHub tag (with filter)

   .. image:: https://img.shields.io/github/license/Tatsh/installkernel-wsl
      :target: https://github.com/Tatsh/installkernel-wsl/blob/master/LICENSE.txt
      :alt: License

   .. image:: https://img.shields.io/github/commits-since/Tatsh/installkernel-wsl/v0.0.3/master
      :target: https://github.com/Tatsh/installkernel-wsl/compare/v0.0.3...master
      :alt: GitHub commits since latest release (by SemVer including pre-releases)

   .. image:: https://github.com/Tatsh/installkernel-wsl/actions/workflows/codeql.yml/badge.svg
      :target: https://github.com/Tatsh/installkernel-wsl/actions/workflows/codeql.yml
      :alt: CodeQL

   .. image:: https://github.com/Tatsh/installkernel-wsl/actions/workflows/qa.yml/badge.svg
      :target: https://github.com/Tatsh/installkernel-wsl/actions/workflows/qa.yml
      :alt: QA

   .. image:: https://github.com/Tatsh/installkernel-wsl/actions/workflows/tests.yml/badge.svg
      :target: https://github.com/Tatsh/installkernel-wsl/actions/workflows/tests.yml
      :alt: Tests

   .. image:: https://coveralls.io/repos/github/Tatsh/installkernel-wsl/badge.svg?branch=master
      :target: https://coveralls.io/github/Tatsh/installkernel-wsl?branch=master
      :alt: Coverage Status

   .. image:: https://readthedocs.org/projects/installkernel-wsl/badge/?version=latest
      :target: https://installkernel-wsl.readthedocs.org/?badge=latest
      :alt: Documentation Status

   .. image:: https://www.mypy-lang.org/static/mypy_badge.svg
      :target: http://mypy-lang.org/
      :alt: mypy

   .. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
      :target: https://github.com/pre-commit/pre-commit
      :alt: pre-commit

   .. image:: https://img.shields.io/badge/pydocstyle-enabled-AD4CD3
      :target: http://www.pydocstyle.org/en/stable/
      :alt: pydocstyle

   .. image:: https://img.shields.io/badge/pytest-zz?logo=Pytest&labelColor=black&color=black
      :target: https://docs.pytest.org/en/stable/
      :alt: pytest

   .. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
      :target: https://github.com/astral-sh/ruff
      :alt: Ruff

   .. image:: https://static.pepy.tech/badge/installkernel-wsl/month
      :target: https://pepy.tech/project/installkernel-wsl
      :alt: Downloads

   .. image:: https://img.shields.io/github/stars/Tatsh/installkernel-wsl?logo=github&style=flat
      :target: https://github.com/Tatsh/installkernel-wsl/stargazers
      :alt: Stargazers

   .. image:: https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpublic.api.bsky.app%2Fxrpc%2Fapp.bsky.actor.getProfile%2F%3Factor%3Ddid%3Aplc%3Auq42idtvuccnmtl57nsucz72%26query%3D%24.followersCount%26style%3Dsocial%26logo%3Dbluesky%26label%3DFollow%2520%40Tatsh&query=%24.followersCount&style=social&logo=bluesky&label=Follow%20%40Tatsh
      :target: https://bsky.app/profile/Tatsh.bsky.social
      :alt: Follow @Tatsh

   .. image:: https://img.shields.io/mastodon/follow/109370961877277568?domain=hostux.social&style=social
      :target: https://hostux.social/@Tatsh
      :alt: Mastodon Follow

Script and installkernel hook to copy Linux kernel to the host system and update .wslconfig.

Commands
--------

.. click:: installkernel_wsl.main:main
  :prog: installkernel-wsl
  :nested: full

Usage as a hook
---------------

After installation:

.. code-block:: bash

   mkdir -p /etc/kernel/install.d
   ln -sf "$(command -v installkernel-wsl)" /etc/kernel/install.d/99-wsl-kernel.install

.. only:: html

   Library
   -------
   .. automodule:: installkernel_wsl.utils
      :members:

   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
