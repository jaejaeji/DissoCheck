import re

def parse_sample_name(name):

    name_match = re.fullmatch(r"(\d+)-(\d+)( .*)?", name)

    if name_match is None:
        raise ValueError(f"Sample_name doesn't match. Must be in Timepoint#-Vessel# format like '10-1', got {name!r}")

    timepoint = int(name_match.group(1))
    vessel = int(name_match.group(2))

    return vessel, timepoint

# print(parse_sample_name("10-1"))