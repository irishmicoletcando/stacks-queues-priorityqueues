from graph import City, load_graph
import networkx as nx

nodes, graph = load_graph("roadmap.dot", City.from_dict)