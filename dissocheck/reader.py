import pandas as pd
from dissocheck.parser import parse_sample_name


def read_export(csv_path):
    df = pd.read_csv(csv_path)

    bad_names = []
    good_names = []
    
    for i, row in df.iterrows():
        name = row["Sample Name"]
        area = row["Peak Area"]

        if name == "WS":
            continue
        try:
            vessel, timepoint = parse_sample_name(name)
            good_names.append({"name": name, "vessel": vessel, "timepoint": timepoint, "peak area": area,})
        except ValueError:
            bad_names.append(name)

    if bad_names:
        raise ValueError(f"Bad names caught: {bad_names}")

    return good_names