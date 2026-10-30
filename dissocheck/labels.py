
def label_injections(rows):

    count = 0

    for row in rows:
         if row["role"] == "WS":
              count += 1
              row["label"] = f"WS{count}"

    if count < 6:
         raise ValueError(f"# of WS injections is {count} (under 6).")
    

    return rows