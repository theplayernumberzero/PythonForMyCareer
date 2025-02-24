import re

text ="Please contact me at +1 (123) 456-7890 or via emial at john@example.com"
pattern =r"\+?\d{1,3}[-.\s]\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?d{1,4}"

matches = re.findall(pattern,text)
print(matches)