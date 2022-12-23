import re

with open('miracle_in_the_andes.txt', 'r', encoding='utf-8') as file:
    book = file.read()

# find chapters
pattern = re.compile('Chapter [0-9]+')
findings = re.findall(pattern, book)
print(findings)
print(len(findings))

# find sentences where 'love' was used
pattern = re.compile('[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z][^.]*.')
findings = re.findall(pattern, book)
print(findings)
print(len(findings))

