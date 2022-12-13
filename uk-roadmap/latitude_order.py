import networkx as nx
from graph import City, load_graph

def order(neighbors):
  def by_latitude(city):
    return city.latitude
  return iter(sorted(neighbors, key=by_latitude, reverse=True))

def is_twentieth_century(year):
  return year and 1901 <= year <= 2000