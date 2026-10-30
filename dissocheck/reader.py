import pandas as pd
from dissocheck.parser import parse_sample_name, find_role


def read_export(csv_path):
    df = pd.read_csv(csv_path)

    bad_names = []
    good_names = []
    
    for i, row in df.iterrows():
        name = row["Sample Name"]
        area = row["Peak Area"]
        role = find_role(name)

        if role:
            good_names.append({"name": name, "vessel": None, "timepoint": None, "peak area": area, "role": role})
            continue
        try:
            vessel, timepoint = parse_sample_name(name)
            good_names.append({"name": name, "vessel": vessel, "timepoint": timepoint, "peak area": area, "role": "sample"})
        except ValueError:
            bad_names.append(name)

    if bad_names:
        raise ValueError(f"Bad names caught: {bad_names}")

    return good_names