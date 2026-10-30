


households = []

fixed_fee = 50
excess_limit = 250
penalty = 100

n = int(input("Enter number of households: "))

total_revenue = 0

# Read household details
for i in range(n):

    print("\nHousehold", i + 1)

    name = input("Enter household name: ")
    consumption = float(input("Enter water consumption (litres): "))

    # Calculate progressive water charges
    if consumption <= 100:
        water_charge = consumption * 2

    elif consumption <= 200:
        water_charge = (100 * 2) + ((consumption - 100) * 3)

    else:
        water_charge = (100 * 2) + (100 * 3) + \
                       ((consumption - 200) * 5)

    # Add fixed fee
    bill = water_charge + fixed_fee

    # Apply excessive usage penalty
    extra_penalty = 0

    if consumption > excess_limit:
        extra_penalty = penalty
        bill += extra_penalty

    # Store household details
    households.append((name, consumption, bill, extra_penalty))

    total_revenue += bill

# Display household bills
print("\n--- WATER BILL REPORT ---")

for item in households:

    name, consumption, bill, extra_penalty = item

    print("\nHousehold:", name)
    print("Consumption:", consumption, "litres")
    print("Water Charge: Rs.", round(bill - fixed_fee - extra_penalty, 2))
    print("Fixed Fee: Rs.", fixed_fee)
    print("Penalty: Rs.", extra_penalty)
    print("Total Bill: Rs.", round(bill, 2))

    if consumption > excess_limit:
        print("Usage Status: EXCESSIVE")
    else:
        print("Usage Status: NORMAL")

# Find highest water consumption
highest = max(households, key=lambda x: x[1])

print("\n--- CONSUMPTION ANALYSIS ---")
print("Highest Consumption Household:", highest[0])
print("Highest Water Usage:", highest[1], "litres")

# Calculate average consumption
average = sum(item[1] for item in households) / n

print("Average Water Consumption:", round(average, 2), "litres")

# Display total revenue
print("\nTotal Revenue: Rs.", round(total_revenue, 2))

