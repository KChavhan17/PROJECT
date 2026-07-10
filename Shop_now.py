#Shop now 


TECH_CATEGORIES = ("Laptops", "Smartphones", "Accessories", "Wearables")

# Product Database: [Name, Price, Stock, Category_Index]
tech_products = [
    ["Gaming Laptop", 85000, 3, 0],
    ["Ultrabook", 65000, 5, 0],
    ["Flagship Phone", 70000, 10, 1],
    ["Budget Phone", 15000, 15, 1],
    ["Wireless Mouse", 1200, 25, 2],
    ["Mechanical Keyboard", 3500, 12, 2],
    ["Smart Watch", 4500, 20, 3],
    ["Fitness Band", 2500, 30, 3]
]

cart = []
wallet = 100000 

def show_tech_inventory():
    print(f"\n--- TECH STORE CATALOG ---")
    
    for i, item in enumerate(tech_products[:6]):
        print(f"[{i}] {item[0]} - ₹{item[1]} (Stock: {item[2]})")

def add_to_cart():
    global wallet
    
    try:
        idx = int(input("\nSelect item ID to buy: "))
        qty = int(input("Enter quantity: "))
        
        # Membership & Boolean check
        item = tech_products[idx]
        if item[2] >= qty: 
            cost = item[1] * qty 
            if wallet >= cost:
                wallet -= cost 
                item[2] -= qty 
                cart.append([item[0], qty, cost])
                print(f"Successfully bought {qty}x {item[0]}!")
            else:
                print("Insufficient balance!")
        else:
            print("Not enough stock!")
    except (ValueError, IndexError):
        print("Invalid input.")

# Main Loop
while True:
    print(f"\nWallet: ₹{wallet} | Cart Items: {len(cart)}")
    print("1: View Tech Items | 2: Buy | 3: Exit")
    choice = input("Action: ")
    
    if choice == '1': show_tech_inventory()
    elif choice == '2': add_to_cart()
    elif choice == '3': break
