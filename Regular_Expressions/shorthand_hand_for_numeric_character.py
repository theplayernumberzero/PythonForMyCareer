import re

text = "ali topu at, topu at ali"
pattern = r"\d" #equal to r"[0-9]"
pattern2 = r"\D" #any NOT DIGIT character from 0-9. opposite of \d

pattern3 = r"\w" #any alphanumerical character
pattern4 = r"\W" #opposite of \w

pattern5 = r"\s" #any whitespace character
pattern6 = r"\S" #opposite of \s
pattern7 = r"\S+" #whitespace görünceye kadar elemanları birleştirip bir eleman yapar ("ali", "topu", "at", ",")

matches = re.findall(pattern=pattern, string=text)
print(matches)
