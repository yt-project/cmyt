#!/usr/bin/env python3
import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

import tomli_w

import re
from collections.abc import MutableMapping


def hardpin(s: str) -> str:
    sep = re.search("(>|=|<|~)", s)
    if sep is None:
        return s
    sep_idx = sep.span()[0]
    name, specs = s[:sep_idx], s[sep_idx:]

    for spec in specs.split(","):
        if ">=" in specs:
            min_ver = spec.strip().lstrip(">=")
            break
    else:
        raise RuntimeError(f"Couldn't determine mininal specification from '{s}'")
    return f"{name}=={min_ver}"


def hardpin_mapping(m: MutableMapping, key: str) -> None:
    m[key] = [hardpin(_) for _ in m[key]]


if __name__ == "__main__":
    with open("pyproject.toml", "rb") as fh:
        conf = tomllib.load(fh)
    hardpin_mapping(conf["project"], "dependencies")
    for target in conf["project"].get("optional-dependencies", {}):
        hardpin_mapping(conf["project"]["optional-dependencies"], target)

    with open("pyproject.toml", "wb") as fhw:
        tomli_w.dump(conf, fhw)
