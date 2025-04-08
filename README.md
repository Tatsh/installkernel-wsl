# installkernel WSL integration

[![QA](https://github.com/Tatsh/installkernel-wsl/actions/workflows/qa.yml/badge.svg)](https://github.com/Tatsh/installkernel-wsl/actions/workflows/qa.yml)
[![Tests](https://github.com/Tatsh/installkernel-wsl/actions/workflows/tests.yml/badge.svg)](https://github.com/Tatsh/installkernel-wsl/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/Tatsh/installkernel-wsl/badge.svg?branch=master)](https://coveralls.io/github/Tatsh/installkernel-wsl?branch=master)
[![Documentation Status](https://readthedocs.org/projects/installkernel-wsl/badge/?version=latest)](https://installkernel-wsl.readthedocs.io/en/latest/?badge=latest)
![PyPI - Version](https://img.shields.io/pypi/v/installkernel-wsl)
![GitHub tag (with filter)](https://img.shields.io/github/v/tag/Tatsh/installkernel-wsl)
![GitHub](https://img.shields.io/github/license/Tatsh/installkernel-wsl)
![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Tatsh/installkernel-wsl/v0.0.1/master)

Script and installkernel hook to copy Linux kernel to the host system and update .wslconfig.

## Installation

```shell
pip install installkernel-wsl
```

## Usage

```shell
installkernel-wsl
```

Add `-d` to show debug logs.

## Usage as a hook

After installation:

```shell
mkdir -p /etc/kernel/install.d
ln -sf "$(command -v installkernel-wsl)" /etc/kernel/install.d/99-wsl-kernel.install
```
