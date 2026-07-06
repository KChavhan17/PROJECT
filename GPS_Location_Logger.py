#GPS Location Logger

print("-"*80)
print("               GPS Location Logger             ")
print("-"*80)
print("\n")


# Store delivery route as a list of coordinate tuples (latitude, longitude)
delivery_route = [
    (12.9716, 77.5946),  # Stop 1
    (13.0827, 80.2707),  # Stop 2
    (17.3850, 78.4867)   # Stop 3
]

# Access individual latitude/longitude values via indexing
first_stop = delivery_route[0]
print(f"First Stop - Latitude: {first_stop[0]}, Longitude: {first_stop[1]}")

# Demonstrate that attempting to modify a tuple raises an error
try:
    print("\nAttempting to modify Stop 1's latitude...")
    delivery_route[0][0] = 14.0000  # This will fail because tuples are immutable
except TypeError as error:
    print(f"Error caught successfully: {error}")