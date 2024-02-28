import re

pattern = re.compile(r'^a[b]*$')

with open('labkaRow.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    pattern = r"ab*"
    result = re.findall(pattern, text)
    print(result)