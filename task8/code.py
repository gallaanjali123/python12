

transactions = []

# Read transaction details
n = int(input("Enter number of transactions: "))

for i in range(n):

    print("\nTransaction", i + 1)

    trans_id = input("Enter transaction ID: ")
    amount = float(input("Enter transaction amount: "))

    transactions.append((trans_id, amount))

# Read threshold
threshold = float(input("\nEnter transaction threshold: "))

# Find duplicate transaction IDs
duplicate_ids = []

for i in range(len(transactions)):
    for j in range(i + 1, len(transactions)):

        if transactions[i][0] == transactions[j][0]:

            if transactions[i][0] not in duplicate_ids:
                duplicate_ids.append(transactions[i][0])

# Generate suspicious transaction list
suspicious = []

for trans_id, amount in transactions:

    reasons = []

    if trans_id in duplicate_ids:
        reasons.append("Duplicate transaction ID")

    if amount > threshold:
        reasons.append("Amount exceeds threshold")

    if reasons:
        suspicious.append((trans_id, amount, reasons))

# Display duplicate IDs
print("\n--- DUPLICATE TRANSACTION IDs ---")

if duplicate_ids:
    for trans_id in duplicate_ids:
        print(trans_id)
else:
    print("No duplicate transactions found.")

# Display suspicious transactions
print("\n--- SUSPICIOUS TRANSACTIONS ---")

if suspicious:

    for trans_id, amount, reasons in suspicious:

        print("\nTransaction ID:", trans_id)
        print("Amount: Rs.", amount)

        for reason in reasons:
            print("Reason:", reason)

else:
    print("No suspicious transactions found.")

# Final summary
print("\n--- FINAL SUMMARY ---")
print("Total Transactions:", len(transactions))
print("Duplicate IDs:", len(duplicate_ids))
print("Suspicious Entries:", len(suspicious))

