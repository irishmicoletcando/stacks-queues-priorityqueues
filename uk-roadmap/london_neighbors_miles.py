from graph import City, load_graph
import networkx as nx

nodes, graph = load_graph("roadmap.dot", City.from_dict)

def sort_by(neighbors, strategy):
  return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
  return float(weights["distance"])