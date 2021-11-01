import json

edges_data = json.load(open('03 network graph/edges.json', 'r'))

all_edges = [tuple(sorted([edge['from'], edge['to']])) for edge in edges_data]
print('all_edges length = ', len(all_edges))

unique_edges = set(all_edges)
print('unique_edges length = ', len(unique_edges))

output_edges = [{'from': t[0], 'to': t[1]} for t in list(unique_edges)]


with open('unique_edges.json', 'w') as output_file:
    json.dump(output_edges, output_file, indent=4)
output_file.close()