import re
text = " weekIsBest"
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', text))

