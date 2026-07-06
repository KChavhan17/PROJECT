#Product Color Code Lookup

print("                                Product Color Code Lookup                       ")
print("*"*90)

# Dictionary using RGB tuples as keys
paint_stock = {
    (255, 0, 0): 50,    # Red
    (0, 255, 0): 35,    # Green
    (0, 0, 255): 120    # Blue
}

# Lookup stock quantity
search_color = (0, 0, 255)
stock_level = paint_stock.get(search_color, 0)

print(f"Stock level for color {search_color}: {stock_level}")