import pandas as pd
from dissocheck.parser import parse_sample_name


def read_export(csv_path):
    df = pd.read_csv(csv_path)

    bad_names = []
    good_names = []
    
    for name in df["Sample Name"]:
        if name == "WS":
            continue
        try:
            good_names.append(parse_sample_name(name))
        except ValueError:
            bad_names.append(name)

    if bad_names:
        raise ValueError(f"Bad names caught: {bad_names}")

    return good_names