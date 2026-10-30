
def label_injections(rows):


     count_ws = 0
     count_cs = 0
     count_bws = 0

     for row in rows:

          if row["role"] == "WS":
               count_ws += 1
               row["label"] = f"WS-{count_ws}"
          elif row["role"] == "CS":
               count_cs += 1
               row["label"] = f"CS-{count_cs}"
          elif row["role"] == "sample":
               row["label"] = f"V{row["vessel"]}-T{row["timepoint"]}"
          elif row["role"] == "BWS":
               count_bws += 1
               row["label"] = f"BWS-{count_bws}"
          else:
               raise ValueError(f"{row["role"]} role not found")

     if count_ws != 6:
          raise ValueError(f"# of WS injections is {count_ws} (not 6).")


     return rows