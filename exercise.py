import re

with open('miracle_in_the_andes.txt', 'r', encoding='utf-8') as file:
    book = file.read()

# extract the paragraphs where 'love' was used
pattern = re.compile('[^\n]+love[^\n]+')
findings = re.findall(pattern, book.lower())
print(findings[58])
print(len(findings))

# extract the chapter titles
pattern = re.compile('(chapter [0-9])+[\n]+(.+)')
findings = re.findall(pattern, book.lower())
print(findings)
print(len(findings))


def find(word):
    pattern = re.compile('[a-zA-Z]+')
    findings = re.findall(pattern, book.lower())

    # for loop
    count = 0
    for i in findings:
        if i == word:
            count += 1
    print(count)

    # str.count
    print(findings.count(word))

    # dict.get
    d = {}
    for search in findings:
        count = d.get(search, 0)
        d[search] = count + 1

    try:
        print(d[word])
    except:
        print(f'{word} not found')

    # d.keys
    d = {}
    for search in findings:
        if search in d.keys():
            d[search] += 1
        else:
            d[search] = 1

    try:
        print(d[word])
    except:
        print(f'{word} not found')

    # KeyError
    d = {}
    for search in findings:
        try:
            d[search] += 1
        except:
            d[search] = 1

    try:
        print(d[word])
    except:
        print(f'{word} not found')


find('chapter')
