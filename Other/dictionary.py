#Dictionary Methods

print("               Dictionary Methods             ")
print("------------------------------------------------")
print("\n")

student={"id":101,"name":"Raghav","grade":'A'}
print("Dictionary:", student)
print("\n")

student.keys()
print("Keys:", student.keys())
print("\n")

student.values()
print("Values:", student.values())
print("\n")

student.items()
print("Items:", student.items())
print("\n")

student.get("name")
print("Name:", student.get("name"))
print("\n")

student.update({"grade":'B'})
print("Updated Dictionary:", student)
print("\n")

student.pop("id")
print("After popping 'id':", student)
print("\n")

student.popitem()
print("After popping last item:", student)
print("\n")

student.clear()
print("After clearing:", student)
print("\n")

len(student)
print("Length:", len(student))
