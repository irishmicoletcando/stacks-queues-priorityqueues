from graph import (
  City,
  load_graph,
  depth_first_traverse,
  depth_first_search as dfs,
)

def is_twentieth_century(city):
  return city.year and 1901 <= city.year <= 2000