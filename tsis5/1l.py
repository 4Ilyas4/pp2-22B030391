import re
text  = "abbbb afa   abbvbf "
pat = r'ab*'
match = re.search(pat, text, re.DOTALL)
if match is not None:
    print(match)
