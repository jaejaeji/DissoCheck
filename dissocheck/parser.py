import re

ROLE_ALIASES = {"WS":["ws", "wstd", "wk std", "working standard", "working std"], "CS":["cs", "cstd", "check standard", "check std", "control standard", "control std"]}


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

        if cleaned in aliases:
            return role
    return None