import re

ROLE_ALIASES = {
    "WS":["ws", "wstd", "wk std", "working standard", "working std"], 
    "CS":["cs", "cstd", "check standard", "check std", "control standard", "control std"], 
    "BWS":["bws", "bstd", "brk", "brk std", "bracket", "bracket std", "bracketing std", "bracket standard", "bracketing standard", "bracketing ws", "bracketing wstd", "bracket ws", "bracket wstd"]
                }


def parse_sample_name(name):

    name_match = re.fullmatch(r"(\d+)-(\d+)( .*)?", name)

    if name_match is None:
        raise ValueError(f"Sample_name doesn't match. Must be in Timepoint#-Vessel# format like '10-1', got {name!r}")

    timepoint = int(name_match.group(1))
    vessel = int(name_match.group(2))

    return vessel, timepoint


def find_role(name):

    cleaned = name.strip().lower()

    for role, aliases in ROLE_ALIASES.items():
        for alias in aliases:
            if cleaned.startswith(alias):
                leftover = cleaned[len(alias):]
                if leftover == "" or leftover[0] in " -0123456789":
                    return role
    return None

from dissocheck.parser import find_role
find_role("WS"); find_role("WS2"); find_role("BWS-5"); find_role("Brk Std-1"); find_role("CS 20.10mg");  find_role("WSX"); 
