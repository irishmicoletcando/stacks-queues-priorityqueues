import networkx as nx
from graph import City, load_graph, dijkstra_shortest_path

nodes, graph = load_graph("roadmap.dot", City.from_dict)