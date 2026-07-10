#Shop Managager

# ==========================================
# THE ULTIMATE RPG INVENTORY & SHOP MANAGER
# ==========================================

# --- 1. SETTING UP VARIABLES & LISTS ---
# Player Stats (Variables)
player_name = "Aria the Brave"
player_gold = 150
max_weight_capacity = 50.0

# Player Inventory (A List, because items can change)
backpack = ["wooden sword", "health potion", "bread", "rusty shield"]

print("--- Welcome to the RPG Inventory Manager ---")
print("Player Name:", player_name)
print("Starting Gold:", player_gold)
print("Initial Backpack:", backpack)
print("-" * 40)


# --- 2. FIXED SHOP DATA (TUPLES) ---
# Shop Catalog (A Tuple, because the shopkeeper's item list is fixed)
shop_items = ("steel sword", "mana potion", "phoenix feather", "antidote")
print("Items available in the town shop today:", shop_items)


# --- 3. USING MEMBERSHIP OPERATORS ---
# Check if a specific item is already in the player's backpack
has_potion = "health potion" in backpack
print("Does the player already have a health potion?", has_potion)

# Check if the shop sells the item the player wants to buy
look_for_item = "steel sword"
is_available_in_shop = look_for_item in shop_items
print("Is the 'steel sword' available in the shop catalog?", is_available_in_shop)
print("-" * 40)


# --- 4. ARITHMETIC OPERATIONS & LIST MODIFICATION ---
# Simulating the purchase of a 'steel sword'
# Let's say a steel sword costs 120 gold and weighs 15.5 lbs
sword_cost = 120
sword_weight = 15.5

print(f"Buying 1 '{look_for_item}' for {sword_cost} gold...")

# Arithmetic Subtraction: Deducting gold from the player
player_gold = player_gold - sword_cost

# List Operation: Adding the new item to the end of the list
backpack.append("steel sword") 

print("Updated Remaining Gold:", player_gold)
print("Updated Backpack Content:", backpack)
print("-" * 40)


# --- 5. CALCULATING WEIGHT WITH BASIC OPERATIONS ---
# Let's assign individual weights to every item now in the backpack
item1_weight = 5.0   # wooden sword
item2_weight = 1.0   # health potion
item3_weight = 0.5   # bread
item4_weight = 12.0  # rusty shield
item5_weight = 15.5  # steel sword (the new item)

# Arithmetic Addition: Summing up all item weights
total_backpack_weight = item1_weight + item2_weight + item3_weight + item4_weight + item5_weight

# Comparison Operator: Checking if total weight exceeds maximum capacity
is_overweight = total_backpack_weight > max_weight_capacity

print("--- Weight Summary ---")
print("Total Backpack Weight:", total_backpack_weight, "lbs")
print("Max Weight Allowed:", max_weight_capacity, "lbs")
print("Is the player carrying too much weight (Encumbered)?", is_overweight)
print("=" * 40)