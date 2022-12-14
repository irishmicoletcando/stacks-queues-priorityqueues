from graph import shortest_path
from graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

def by_latitude(city):
  return -city.latitude


print(" → ".join(city.name for city in shortest_path(graph, city1, city2)))

print(" → ".join(
  city.name
  for city in shortest_path(graph, city1, city2, by_latitude)
))