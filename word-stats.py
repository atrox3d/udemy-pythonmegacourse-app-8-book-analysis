import re

with open('miracle_in_the_andes.txt', 'r', encoding='utf-8') as file:
    book = file.read()

pattern = re.compile('[a-zA-Z]+')
findings = re.findall(pattern, book.lower())
# print(findings)
# print(len(findings))
# print(findings[:5])

d = {}
for word in findings:
    try:
        d[word] = d[word] + 1
    except KeyError:
        d[word] = 1
print(d)

dl = [(value, key) for (key, value) in d.items()]
print(sorted(dl, reverse=True))
