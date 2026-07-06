#Database Row Processor

print("                        Database Row Processor"                             )
print("*"*80)


# Nested tuple representing database rows (tx_id, customer_id, amount)
transactions = (
    (1, "C101", 250),
    (2, "C102", 450),
    (3, "C101", 150),
    (4, "C103", 300)
)

# Extract customer IDs to count occurrences
customer_ids = tuple(row[1] for row in transactions)
target_customer = "C101"
print(f"Transactions for {target_customer}: {customer_ids.count(target_customer)}\n")

# Locate specific transaction record index
target_tx = (2, "C102", 450)
print(f"Transaction {target_tx} index: {transactions.index(target_tx)}\n")