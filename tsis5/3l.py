import re

text = "abb_bb_ bb _afaf ab afd_ac"
pat = r'_[a-z]*_'
match = re.search(pat, text, re.DOTALL)
if match is not None:
    print(match)

