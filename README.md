# installkernel-wsl

[![Python versions](https://img.shields.io/pypi/pyversions/installkernel-wsl.svg?color=blue&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI - Version](https://img.shields.io/pypi/v/installkernel-wsl)](https://pypi.org/project/installkernel-wsl/)
[![GitHub tag (with filter)](https://img.shields.io/github/v/tag/Tatsh/installkernel-wsl)](https://github.com/Tatsh/installkernel-wsl/tags)
[![License](https://img.shields.io/github/license/Tatsh/installkernel-wsl)](https://github.com/Tatsh/installkernel-wsl/blob/master/LICENSE.txt)
[![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Tatsh/installkernel-wsl/v0.0.4/master)](https://github.com/Tatsh/installkernel-wsl/compare/v0.0.4...master)
[![CodeQL](https://github.com/Tatsh/installkernel-wsl/actions/workflows/codeql.yml/badge.svg)](https://github.com/Tatsh/installkernel-wsl/actions/workflows/codeql.yml)
[![QA](https://github.com/Tatsh/installkernel-wsl/actions/workflows/qa.yml/badge.svg)](https://github.com/Tatsh/installkernel-wsl/actions/workflows/qa.yml)
[![Tests](https://github.com/Tatsh/installkernel-wsl/actions/workflows/tests.yml/badge.svg)](https://github.com/Tatsh/installkernel-wsl/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/Tatsh/installkernel-wsl/badge.svg?branch=master)](https://coveralls.io/github/Tatsh/installkernel-wsl?branch=master)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-blue?logo=dependabot)](https://github.com/dependabot)
[![Documentation Status](https://readthedocs.org/projects/installkernel-wsl/badge/?version=latest)](https://installkernel-wsl.readthedocs.org/?badge=latest)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/)
[![Poetry](https://img.shields.io/badge/Poetry-242d3e?logo=poetry)](https://python-poetry.org)
[![pydocstyle](https://img.shields.io/badge/pydocstyle-enabled-AD4CD3?logo=pydocstyle)](https://www.pydocstyle.org/)
[![pytest](https://img.shields.io/badge/pytest-enabled-CFB97D?logo=pytest)](https://docs.pytest.org)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Downloads](https://static.pepy.tech/badge/installkernel-wsl/month)](https://pepy.tech/project/installkernel-wsl)
[![Stargazers](https://img.shields.io/github/stars/Tatsh/installkernel-wsl?logo=github&style=flat)](https://github.com/Tatsh/installkernel-wsl/stargazers)
[![Prettier](https://img.shields.io/badge/Prettier-enabled-black?logo=prettier)](https://prettier.io/)

[![@Tatsh](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpublic.api.bsky.app%2Fxrpc%2Fapp.bsky.actor.getProfile%2F%3Factor=did%3Aplc%3Auq42idtvuccnmtl57nsucz72&query=%24.followersCount&style=social&logo=bluesky&label=Follow+%40Tatsh)](https://bsky.app/profile/Tatsh.bsky.social)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Tatsh-black?logo=buymeacoffee)](https://buymeacoffee.com/Tatsh)
[![Libera.Chat](https://img.shields.io/badge/Libera.Chat-Tatsh-black?logo=liberadotchat)](irc://irc.libera.chat/Tatsh)
[![Mastodon Follow](https://img.shields.io/mastodon/follow/109370961877277568?domain=hostux.social&style=social)](https://hostux.social/@Tatsh)
[![Patreon](https://img.shields.io/badge/Patreon-Tatsh2-F96854?logo=patreon)](https://www.patreon.com/Tatsh2)

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
