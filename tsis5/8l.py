import re

text = "abb_bb_.Abb,_afafSs ab aDfd_ac/."
pat = r'[A-Z]'
t = re.split(pat, text)
print(t)

