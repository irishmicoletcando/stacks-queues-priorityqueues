from graph import City, load_graph
import networkx as nx

print(nx.nx_agraph.read_dot("roadmap.dot"))
nodes, graph = load_graph("roadmap.dot", City.from_dict)

nodes["london"]

print(graph)