from queues import Stack

lifo = Stack("1st", "2nd", "3rd")
for element in lifo:
  print(element)

# can also be used in list
lifo = []
lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

print(lifo.pop()) # 3rd
print(lifo.pop()) # 2nd
print(lifo.pop()) # 1st