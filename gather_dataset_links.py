import re
from urllib.request import urlopen

datasets_url = "https://archive.ics.uci.edu/ml/datasets.html?format=&task=reg&att=&area=&numAtt=&numIns=&type=&sort=nameUp&view=table"

response = urlopen(datasets_url)
html = str(response.read())

#index_1 = 'table cellpadding="5" border="1">'
index_1 = 'datasets/3D+Road+Network+%28North+Jutland%2C+Denmark%29'
index_2 = 'datasets/YearPredictionMSD'

table_starts = html.find(index_1)
table_ends = html.find(index_2)

print(table_starts)
print(table_ends)

page = html[table_starts:table_ends]
links = re.findall('datasets/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', page)

links.append(index_1)
links.append(index_2)
links=sorted(set(links))

with open('links.txt', 'w') as links_file:
    for row in links:
        links_file.write(row+'\n')
links_file.close()
