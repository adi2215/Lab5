import re

pattern = re.compile(r'^ab{2,3}$')

file_path = r'labkaRow.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
    result = re.findall(pattern, text)
    print(result)
