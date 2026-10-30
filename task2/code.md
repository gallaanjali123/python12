

## 1. Problem Statement

Develop a Python program to analyse hypothetical laboratory chemical inventory records. The program should check whether each chemical is stored in the correct storage category, verify that the stored quantity does not exceed the maximum permitted quantity, and identify incompatible chemical combinations. Finally, display valid records and flag all inventory violations.



## 2. Algorithm

1. Start the program.
2. Define the allowed storage categories and maximum quantities.
3. Define hypothetical incompatible chemical pairs.
4. Read the number of chemical records.
5. For each chemical, read its name, storage category, and quantity.
6. Check whether the storage category is valid.
7. Check whether the quantity exceeds the maximum allowed quantity.
8. Compare the chemical with previously entered chemicals to identify incompatible combinations.
9. Display the violations for each record.
10. Display the total number of valid and invalid records.
11. Stop the program.

## 3. Flowchart

```

             START
               |
               v
     Define storage categories,
     maximum quantities and
     compatibility rules
               |
               v
       Read number of records
               |
               v
       Read chemical details
               |
               v
       Is category valid?
          /          \
        No            Yes
        |              |
        v              v
   Flag invalid   Check maximum
     category       quantity
                       |
                       v
                Quantity exceeds
                  maximum?
                  /       \
                Yes        No
                 |          |
                 v          v
             Flag excess  Continue
              quantity
                  \        /
                   v      v
             Check incompatible
              chemical pairs
                    |
                    v
             Any violation?
               /       \
             Yes        No
              |          |
              v          v
          Mark invalid  Mark valid
               \        /
                v      v
             Display results
                    |
                    v
             More records?
               /       \
             Yes        No
              |          |
              v          v
          Read next    Display summary
          record           |
                           v
                          STOP

```

## 4. Python Source Code

```
    errors = []    name = item["name"]    category = item["category"]    quantity = item["quantity"]    # Check storage category    if category not in storage_rules:        errors.append("Invalid storage category")    else:        # Check maximum quantity        if quantity > storage_rules[category]:            errors.append("Maximum quantity exceeded")    # Check compatibility with other records    for other in inventory:        if name != other["name"]:            pair = (name, other["name"])            reverse_pair = (other["name"], name)            if (pair in incompatible_pairs or                    reverse_pair in incompatible_pairs):                if "Incompatible with " + other["name"] not in errors:                    errors.append("Incompatible with " + other["name"])    # Display result    print("\nChemical:", name)    print("Category:", category)    print("Quantity:", quantity)    if errors:        print("Status: INVALID")        for error in errors:            print("-", error)        invalid_count += 1    else:        print("Status: VALID")        valid_count += 1# Display summaryprint("\n--- FINAL SUMMARY ---")print("Total Records:", n)print("Valid Records:", valid_count)print("Invalid Records:", invalid_count)
```

## 5. Sample Input

```

Enter number of chemical records: 4

Chemical Record 1
Enter chemical name: ChemicalA
Enter storage category (A/B/C): A
Enter quantity: 30

Chemical Record 2
Enter chemical name: ChemicalB
Enter storage category (A/B/C): B
Enter quantity: 20

Chemical Record 3
Enter chemical name: ChemicalC
Enter storage category (A/B/C): C
Enter quantity: 40

Chemical Record 4
Enter chemical name: ChemicalD
Enter storage category (A/B/C): X
Enter quantity: 10

```

## 6. Sample Output

```

--- INVENTORY VALIDATION REPORT ---

Chemical: ChemicalA
Category: A
Quantity: 30.0
Status: INVALID
- Incompatible with ChemicalB

Chemical: ChemicalB
Category: B
Quantity: 20.0
Status: INVALID
- Incompatible with ChemicalA

Chemical: ChemicalC
Category: C
Quantity: 40.0
Status: INVALID
- Maximum quantity exceeded

Chemical: ChemicalD
Category: X
Quantity: 10.0
Status: INVALID
- Invalid storage category

--- FINAL SUMMARY ---
Total Records: 4
Valid Records: 0
Invalid Records: 4

```

Note: The program uses hypothetical rules for learning Python lists, dictionaries, loops, conditions, and validation.
