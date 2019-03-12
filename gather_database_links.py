import re
from urllib.request import urlopen

db_link_handle = "machine-learning-databases/"
links_file = "links.txt"
datasets_parent_folder = "https://archive.ics.uci.edu/ml/"

with open(links_file) as f:
    content = f.readlines()

for row in content:
    link = datasets_parent_folder + row
    response = urlopen(link)
    html = str(response.read())
    db_link = re.findall(db_link_handle+'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
    print(db_link)

