


# Hypothetical storage categories and maximum quantities
storage_rules = {
    "A": 50,
    "B": 40,
    "C": 30
}

# Hypothetical incompatible chemical pairs
incompatible_pairs = [
    ("ChemicalA", "ChemicalB"),
    ("ChemicalC", "ChemicalD"),
    ("ChemicalE", "ChemicalF")
]

inventory = []

n = int(input("Enter number of chemical records: "))
for i in range(n):
    print("\nChemical Record", i + 1)

    name = input("Enter chemical name: ")
    category = input("Enter storage category (A/B/C): ")
    quantity = float(input("Enter quantity: "))

    inventory.append({
        "name": name,
        "category": category,
        "quantity": quantity
    })

print("\n--- INVENTORY VALIDATION REPORT ---")

valid_count = 0
invalid_count = 0

for item in inventory:
    errors = []

    name = item["name"]
    category = item["category"]
    quantity = item["quantity"]

  
    if category not in storage_rules:
        errors.append("Invalid storage category")

    else:
    
        if quantity > storage_rules[category]:
            errors.append("Maximum quantity exceeded")

    
    for other in inventory:
        if name != other["name"]:
            pair = (name, other["name"])
            reverse_pair = (other["name"], name)

            if (pair in incompatible_pairs or
                    reverse_pair in incompatible_pairs):
                if "Incompatible with " + other["name"] not in errors:
                    errors.append("Incompatible with " + other["name"])

    
    print("\nChemical:", name)
    print("Category:", category)
    print("Quantity:", quantity)

    if errors:
        print("Status: INVALID")
        for error in errors:
            print("-", error)
        invalid_count += 1
    else:
        print("Status: VALID")
        valid_count += 1

print("\n--- FINAL SUMMARY ---")
print("Total Records:", n)
print("Valid Records:", valid_count)
print("Invalid Records:", invalid_count)

