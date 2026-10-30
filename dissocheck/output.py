import re

def safe_filename(text):
    new_filename = re.sub(r'[/\\:*?"<>|]', "-", text.replace("%",""))

    return new_filename


print(safe_filename(r'Drug 10mg 40C\75%RH 29 Oct 26 JL'))
# (r"...") prefix runs raw string instead of test string (\7: =)

print(safe_filename("Drug 10mg 40C/75%RH 29 Oct 26 JL"))
print(safe_filename('a\\b:c*d?e"f<g>h|i'))