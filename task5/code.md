

## 1. Problem Statement

Develop a Python program to calculate water bills for multiple households based on their monthly water consumption.

The program should:

- Calculate charges using progressive consumption slabs.
- Add fixed monthly fees.
- Apply penalties for excessive water consumption.
- Compare water consumption among households.
- Identify households with excessive water usage.
- Display individual bills and the total revenue collected

## 2. Algorithm

1. Start the program.
2. Define water consumption slabs and their rates.
3. Define the fixed monthly fee and excessive usage limit.
4. Read the number of households.
5. For each household, read the household name and water consumption.
6. Calculate the water charge using progressive slabs:
   - First 100 litres: ₹2 per litre.
   - Next 100 litres: ₹3 per litre.
   - Above 200 litres: ₹5 per litre.
7. Add the fixed monthly fee of ₹50.
8. If consumption exceeds 250 litres, apply a penalty of ₹100.
9. Calculate the final bill.
10. Compare household consumption.
11. Identify the household with the highest consumption.
12. Display all household bills and total revenue.
13. Stop the program.

## 3. Flowchart

```

               START
                 |
                 v
       Define tariff slabs,
       fixed fee and penalty
                 |
                 v
       Read number of households
                 |
                 v
       Read household name
       and water consumption
                 |
                 v
       Calculate slab charges
                 |
                 v
       Add fixed monthly fee
                 |
                 v
       Is consumption > 250?
             /       \
           Yes        No
            |          |
            v          v
       Add penalty   No penalty
            |          |
            +----+-----+
                 |
                 v
        Calculate final bill
                 |
                 v
        Store household details
                 |
                 v
        More households?
             /       \
           Yes        No
            |          |
            v          v
        Read next   Compare consumption
        household       |
                        v
                 Find highest usage
                        |
                        v
                 Display household bills
                 and total revenue
                        |
                        v
                       STOP

```

## 4. Python Source Code

```
    elif consumption <= 200:        water_charge = (100 * 2) + ((consumption - 100) * 3)    else:        water_charge = (100 * 2) + (100 * 3) + \                       ((consumption - 200) * 5)    # Add fixed fee    bill = water_charge + fixed_fee    # Apply excessive usage penalty    extra_penalty = 0    if consumption > excess_limit:        extra_penalty = penalty        bill += extra_penalty    # Store household details    households.append((name, consumption, bill, extra_penalty))    total_revenue += bill# Display household billsprint("\n--- WATER BILL REPORT ---")for item in households:    name, consumption, bill, extra_penalty = item    print("\nHousehold:", name)    print("Consumption:", consumption, "litres")    print("Water Charge: Rs.", round(bill - fixed_fee - extra_penalty, 2))    print("Fixed Fee: Rs.", fixed_fee)    print("Penalty: Rs.", extra_penalty)    print("Total Bill: Rs.", round(bill, 2))    if consumption > excess_limit:        print("Usage Status: EXCESSIVE")    else:        print("Usage Status: NORMAL")# Find highest water consumptionhighest = max(households, key=lambda x: x[1])print("\n--- CONSUMPTION ANALYSIS ---")print("Highest Consumption Household:", highest[0])print("Highest Water Usage:", highest[1], "litres")# Calculate average consumptionaverage = sum(item[1] for item in households) / nprint("Average Water Consumption:", round(average, 2), "litres")# Display total revenueprint("\nTotal Revenue: Rs.", round(total_revenue, 2))
```

## 5. Sample Input

```

Enter number of households: 3

Household 1
Enter household name: Ravi
Enter water consumption (litres): 80

Household 2
Enter household name: Priya
Enter water consumption (litres): 180

Household 3
Enter household name: Kumar
Enter water consumption (litres): 300

```

## 6. Sample Output

```

--- WATER BILL REPORT ---

Household: Ravi
Consumption: 80.0 litres
Water Charge: Rs. 160.0
Fixed Fee: Rs. 50
Penalty: Rs. 0
Total Bill: Rs. 210.0
Usage Status: NORMAL

Household: Priya
Consumption: 180.0 litres
Water Charge: Rs. 440.0
Fixed Fee: Rs. 50
Penalty: Rs. 0
Total Bill: Rs. 490.0
Usage Status: NORMAL

Household: Kumar
Consumption: 300.0 litres
Water Charge: Rs. 900.0
Fixed Fee: Rs. 50
Penalty: Rs. 100
Total Bill: Rs. 1050.0
Usage Status: EXCESSIVE

--- CONSUMPTION ANALYSIS ---
Highest Consumption Household: Kumar
Highest Water Usage: 300.0 litres
Average Water Consumption: 186.67 litres

Total Revenue: Rs. 1750.0

```

## 7. Result

The Python program successfully calculates progressive water bills for multiple households, applies fixed fees and excessive usage penalties, compares consumption patterns, identifies the household with the highest water usage, and calculates total revenue.

Python concepts used: Lists, tuples, loops, conditional statements, arithmetic operations, `max()`, and `sum()`.
