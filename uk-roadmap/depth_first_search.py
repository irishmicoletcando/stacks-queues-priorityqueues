import networkx as nx
from graph import City, load_graph

def is_twentieth_century(year):
  return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)