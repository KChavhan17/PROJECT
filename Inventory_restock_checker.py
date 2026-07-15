#Inventory Restock Checker

product_count=int(input("Enter number of product : "))
products={}
for i in range(product_count):
    print(">Enter product name and stock : ")
    product_name=input(">")
    product_stock=int(input(">"))
    products[product_name]=product_stock
print("===Records===")
for name in products:
    product_stock=products[name]
    print(f"Product : {name}\nStock : {product_stock}")
    if product_stock >= 20:
        print("Stock OK")
    else:
        print("Reorder Needed")
    print("-"*12)   