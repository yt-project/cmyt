#!/usr/bin/env python3

import configparser
import io
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
    reqs = m[key].split("\n")
    m[key] = "\n".join(hardpin(_) for _ in reqs)


if __name__ == "__main__":
    cp = configparser.ConfigParser()
    cp.read("setup.cfg")
    hardpin_mapping(cp["options"], "install_requires")
    for target in cp["options.extras_require"].keys():
        hardpin_mapping(cp["options.extras_require"], target)

    output = io.StringIO()
    cp.write(output)
    s = output.getvalue().replace("\t", " " * 4)
    s = "\n".join(_.rstrip() for _ in s.split("\n"))
    with open("setup.cfg", "w") as fh:
        fh.write(s)
