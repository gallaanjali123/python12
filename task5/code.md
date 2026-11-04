

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

