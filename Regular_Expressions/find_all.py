import re

text = "ali topu at, topu at ali"
pattern = r"ali"
matches = re.findall(pattern=pattern, string=text)
print(matches)

#character class ve findall birlikte kullanılabilir