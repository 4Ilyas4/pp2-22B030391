import re
text = " weekIsBest"
s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower())
