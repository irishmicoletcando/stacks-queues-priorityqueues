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