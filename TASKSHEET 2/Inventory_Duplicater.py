#Inventory Duplicate Finder

print("-"*70)
print("                  Inventory Duplicate Finder                ")
print("-" * 70)

product_codes=["A123", "B456", "C789", "A123", "D012", "B456", "E345", "F678", "G901", "H234"]
print("\nList of product codes:", product_codes)
print("\n")


repeated_codes =product_codes.count("A123")
print("Duplicate count of 'A123':", repeated_codes)
print("\n")

duplicate_code_index=product_codes.index("A123")
print("Index of first occurrence of duplicate code 'A123':", duplicate_code_index)
print("\n")

