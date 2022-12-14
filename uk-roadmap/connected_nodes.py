from graph import connected
from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

print(connected(graph, nodes["belfast"], nodes["glasgow"]))

print(connected(graph, nodes["belfast"], nodes["derry"]))