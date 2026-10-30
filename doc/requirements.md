# Requirements

R1. DissoCheck shall parse Empower sample names (T#-V# format, e.g. 10-1) into vessel and timepoint integers
Verified by: 10-1 should translate to (Vessel 1, Timepoint 10 minutes), 15-10 into (Vessel 10 - Timepoint 15 minutes)

R2. Reject a malformed name. Raises an error
Verified by: unacceptable/unrecognizeable title name or typos = 10-, V1-T10, V3-T raises a ValueError naming the bad input. Blank, WS and CS injections are handled before the parser

R3. Recognize the standard injection order (blank, 6 WS, CS, media blank, a bracket every 6)
Verified by: a synthetic sequence goes in and each injection gets a role. If only 5 WS is present an error is raised.

R4. Make the file name safe. Names that include unaccepted formats such as 40C/75%RH should be 40C-75RH instead
Verified by: Drug 10mg tablets 40C/75%RH 27 Oct 26 JL. Expected output: Drug 10mg tablets 40C-75RH 27 Oct 26 JL

R5. Enforce .gitignore rules. This prevents the files listed from being pushed to Git.
```
.venv/
__pycache__/
*work*.yaml
*.xlsx
*.csv
!tests/answer_keys/*.xlsx
!tests/answer_keys/*.csv
!tests/data/*.csv

```
Verified by: check git status. no work*.yaml, .csv or .xslx (except those in tests/answer_keys folder) files should be here


