import requests
import json
import os

nodes = json.load(open('03 network graph/misc/nodes.json', 'r'))

for node in nodes:
    # print(node['id'])
    # print(node['fill']['src'])
    response = requests.get(node['fill']['src'])

    file = open(os.path.join('thumbnails', '{}.png'.format(node['id'])), "wb")
    file.write(response.content)
    file.close()