import re

text = "gsdfgs hgdg 214 d agsdgsg4gf43GRFGDgfbfsgs "
pat = r'a(.*)b'
match = re.search(pat, text, re.DOTALL)
if match is not None:
    print(match)

