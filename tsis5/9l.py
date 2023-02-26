import re

text = "HelloMyDearWorld"
print(re.sub(r"(\w)([A-Z])", r"\1 \2", text))
