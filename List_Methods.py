#List Methods in Python

print("               List Methods             ")
print("------------------------------------------------")


L=[10,20,30]
print("List:", L)
print("\n")

L.append(50)
print("After appending 50:", L)
print("\n")


L.extend([60,70])
print("After extending with [60,70]:", L)
print("\n")

L.insert(1,100)
print("After inserting 100 at index 1:", L)
print("\n")

L.remove(20)
print("After removing 20:", L)
print("\n")

L.pop()
print("After popping last item:", L)
print("\n")

#L.clear()
#print("After clearing:", L)


L.index(30)
print("Index of 30:", L.index(30))
print("\n")

L.count(10)
print("Count of 10:", L.count(10))
print("\n")

L.sort()
print("After sorting:", L)
print("\n")

L.reverse()
print("After reversing:", L)
print("\n")

L.copy()
print("Copy of the list:", L.copy())
print("\n")

L.clear()
print("After clearing:", L)
print("\n")