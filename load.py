from urllib.request import urlopen
import json
import parse

f = open('data.json')
all_data = json.load(f)

for data in all_data:
    f = urlopen(data['link']).read().decode('UTF-8').split('\n')
    for line in f:
        parse.parse_line(line, data['year'])
