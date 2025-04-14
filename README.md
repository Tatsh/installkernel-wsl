# installkernel-wsl

[![QA](https://github.com/Tatsh/installkernel-wsl/actions/workflows/qa.yml/badge.svg)](https://github.com/Tatsh/installkernel-wsl/actions/workflows/qa.yml)
[![Tests](https://github.com/Tatsh/installkernel-wsl/actions/workflows/tests.yml/badge.svg)](https://github.com/Tatsh/installkernel-wsl/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/Tatsh/installkernel-wsl/badge.svg?branch=master)](https://coveralls.io/github/Tatsh/installkernel-wsl?branch=master)
[![Documentation Status](https://readthedocs.org/projects/installkernel-wsl/badge/?version=latest)](https://installkernel-wsl.readthedocs.org/?badge=latest)
[![PyPI - Version](https://img.shields.io/pypi/v/installkernel-wsl)](https://pypi.org/project/installkernel-wsl/)
[![GitHub tag (with filter)](https://img.shields.io/github/v/tag/Tatsh/installkernel-wsl)](https://github.com/Tatsh/installkernel-wsl/tags)
[![License](https://img.shields.io/github/license/Tatsh/installkernel-wsl)](https://github.com/Tatsh/installkernel-wsl/blob/master/LICENSE.txt)
[![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Tatsh/installkernel-wsl/v0.0.3/master)](https://github.com/Tatsh/installkernel-wsl/compare/v0.0.3...master)

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
