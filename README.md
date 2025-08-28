# installkernel-wsl

[![Python versions](https://img.shields.io/pypi/pyversions/installkernel-wsl.svg?color=blue&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI - Version](https://img.shields.io/pypi/v/installkernel-wsl)](https://pypi.org/project/installkernel-wsl/)
[![GitHub tag (with filter)](https://img.shields.io/github/v/tag/Tatsh/installkernel-wsl)](https://github.com/Tatsh/installkernel-wsl/tags)
[![License](https://img.shields.io/github/license/Tatsh/installkernel-wsl)](https://github.com/Tatsh/installkernel-wsl/blob/master/LICENSE.txt)
[![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Tatsh/installkernel-wsl/v0.0.3/master)](https://github.com/Tatsh/installkernel-wsl/compare/v0.0.3...master)
[![CodeQL](https://github.com/Tatsh/installkernel-wsl/actions/workflows/codeql.yml/badge.svg)](https://github.com/Tatsh/installkernel-wsl/actions/workflows/codeql.yml)
[![QA](https://github.com/Tatsh/installkernel-wsl/actions/workflows/qa.yml/badge.svg)](https://github.com/Tatsh/installkernel-wsl/actions/workflows/qa.yml)
[![Tests](https://github.com/Tatsh/installkernel-wsl/actions/workflows/tests.yml/badge.svg)](https://github.com/Tatsh/installkernel-wsl/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/Tatsh/installkernel-wsl/badge.svg?branch=master)](https://coveralls.io/github/Tatsh/installkernel-wsl?branch=master)
[![Documentation Status](https://readthedocs.org/projects/installkernel-wsl/badge/?version=latest)](https://installkernel-wsl.readthedocs.org/?badge=latest)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pydocstyle](https://img.shields.io/badge/pydocstyle-enabled-AD4CD3)](http://www.pydocstyle.org/en/stable/)
[![pytest](https://img.shields.io/badge/pytest-zz?logo=Pytest&labelColor=black&color=black)](https://docs.pytest.org/en/stable/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Downloads](https://static.pepy.tech/badge/installkernel-wsl/month)](https://pepy.tech/project/installkernel-wsl)
[![Stargazers](https://img.shields.io/github/stars/Tatsh/installkernel-wsl?logo=github&style=flat)](https://github.com/Tatsh/installkernel-wsl/stargazers)

[![@Tatsh](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpublic.api.bsky.app%2Fxrpc%2Fapp.bsky.actor.getProfile%2F%3Factor%3Ddid%3Aplc%3Auq42idtvuccnmtl57nsucz72%26query%3D%24.followersCount%26style%3Dsocial%26logo%3Dbluesky%26label%3DFollow%2520%40Tatsh&query=%24.followersCount&style=social&logo=bluesky&label=Follow%20%40Tatsh)](https://bsky.app/profile/Tatsh.bsky.social)
[![Mastodon Follow](https://img.shields.io/mastodon/follow/109370961877277568?domain=hostux.social&style=social)](https://hostux.social/@Tatsh)

Script and installkernel hook to copy Linux kernel to the host system and update .wslconfig.

## Installation

### Poetry

```shell
poetry add installkernel-wsl
```

### Pip

```shell
pip install installkernel-wsl
```

## Usage

Add `-d` to show debug logs.

```shell
installkernel-wsl
```

## Usage as a hook

After installation:

```shell
mkdir -p /etc/kernel/install.d
ln -sf "$(command -v installkernel-wsl)" /etc/kernel/install.d/99-wsl-kernel.install
```
