from heapq import heappush, heappop

fruits = []

# pushing elements to fruits list 
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)

# removing the first element in fruits list
print(heappop(fruits))

print(fruits)

# tuple comparison
person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print(person1 < person2)
print(person2 < person3)