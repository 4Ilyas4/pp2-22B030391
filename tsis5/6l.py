import re

text = "abb_bb_.Abb,_afaf ab afd_ac/."
pat = r'[\s\.\,]'
match = re.search(pat, text, re.DOTALL)
t = re.sub(pat,':',text)
print(t)

