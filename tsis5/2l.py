import re

text = "abbbbbb afaf ab afdac"
pat = r'a(bb)|(bbb)'
match = re.search(pat, text, re.DOTALL)
if match is not None:
    print(match)

