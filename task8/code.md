

## 1. Problem Statement

Develop a Python program to process transaction identifiers and transaction amounts stored in lists.

The program should:

- Identify duplicate transaction IDs.
- Detect transactions that exceed a specified amount threshold.
- Generate a list of suspicious transactions.
- Display the transaction details and reasons for flagging.
- Calculate the total number of suspicious transactions.

## 2. Algorithm

1. Start the program.
2. Read the number of transactions.
3. Read each transaction ID and transaction amount.
4. Store the transaction details in a list.
5. Read the transaction amount threshold.
6. Create an empty list to store suspicious transactions.
7. Use loops to compare transaction IDs.
8. Identify duplicate transaction IDs.
9. Check whether each transaction amount exceeds the threshold.
10. Add suspicious transactions to the suspicious list.
11. Display duplicate transactions and threshold violations.
12. Display the total number of suspicious transactions.
13. Stop the program.

## 3. Flowchart

```

                START
                  |
                  v
          Read number of transactions
                  |
                  v
        Read transaction IDs and amounts
                  |
                  v
          Store records in a list
                  |
                  v
          Read amount threshold
                  |
                  v
          Initialize suspicious list
                  |
                  v
          Compare transaction IDs
                  |
                  v
          Is transaction ID repeated?
              /          \
            Yes           No
             |             |
             v             v
       Mark as duplicate   Continue
             |             |
             +------+------+
                    |
                    v
         Check transaction amount
                    |
                    v
         Amount exceeds threshold?
              /          \
            Yes           No
             |             |
             v             v
       Mark threshold    Continue
         violation
             |
             v
       Add suspicious entry
             |
             v
       More transactions?
           /        \
         Yes         No
          |           |
          v           v
       Repeat     Display suspicious
                    transactions
                        |
                        v
                   Display summary
                        |
                        v
                       STOP

```

## 4. Python Source Code

```
# Repeated Transaction Detectiontransactions = []# Read transaction detailsn = int(input("Enter number of transactions: "))for i in range(n):    print("\nTransaction", i + 1)    trans_id = input("Enter transaction ID: ")    amount = float(input("Enter transaction amount: "))    transactions.append((trans_id, amount))# Read thresholdthreshold = float(input("\nEnter transaction threshold: "))# Find duplicate transaction IDsduplicate_ids = []for i in range(len(transactions)):    for j in range(i + 1, len(transactions)):        if transactions[i][0] == transactions[j][0]:            if transactions[i][0] not in duplicate_ids:                duplicate_ids.append(transactions[i][0])# Generate suspicious transaction listsuspicious = []for trans_id, amount in transactions:
```

## 5. Sample Input

```

Enter number of transactions: 5

Transaction 1
Enter transaction ID: T101
Enter transaction amount: 500

Transaction 2
Enter transaction ID: T102
Enter transaction amount: 1500

Transaction 3
Enter transaction ID: T101
Enter transaction amount: 700

Transaction 4
Enter transaction ID: T103
Enter transaction amount: 2500

Transaction 5
Enter transaction ID: T104
Enter transaction amount: 300

Enter transaction threshold: 1000

```

## 6. Sample Output

```

--- DUPLICATE TRANSACTION IDs ---
T101

--- SUSPICIOUS TRANSACTIONS ---

Transaction ID: T101
Amount: Rs. 500.0
Reason: Duplicate transaction ID

Transaction ID: T102
Amount: Rs. 1500.0
Reason: Amount exceeds threshold

Transaction ID: T101
Amount: Rs. 700.0
Reason: Duplicate transaction ID

Transaction ID: T103
Amount: Rs. 2500.0
Reason: Amount exceeds threshold

--- FINAL SUMMARY ---
Total Transactions: 5
Duplicate IDs: 1
Suspicious Entries: 4

```

## 7. Result

The Python program successfully detects duplicate transaction identifiers, identifies transactions exceeding the specified amount threshold, and generates a list of suspicious entries.

Python concepts used: Lists, tuples, nested loops, conditional statements, string comparison, and list operations.
