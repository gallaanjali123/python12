

## 1. Problem Statement

Process multiple traffic violations based on vehicle category, offence type, repeat-offence status, and predefined fine rules. Calculate the total penalty for each violation and identify whether the vehicle or driver meets any disqualification conditions.

## 2. Algorithm

1. Start.
2. Input the number of traffic violations.
3. For each violation:
   - Input vehicle category.
   - Input offence type.
   - Input whether it is a repeat offence.
4. Determine the basic fine based on the offence type.
5. Apply the repeat-offence penalty if applicable.
6. Calculate the final fine.
7. Check whether the offence has a disqualification condition.
8. Display the offence details and final penalty.
9. Calculate the total penalty for all violations.
10. Display the total fine and disqualification status.
11. Stop.

## 3. Flowchart (Copyable Text)

```

                 START
                   |
                   v
        INPUT NUMBER OF VIOLATIONS
                   |
                   v
         INPUT VEHICLE CATEGORY
                   |
                   v
            INPUT OFFENCE TYPE
                   |
                   v
        IS IT A REPEAT OFFENCE?
              /          \
            YES           NO
             |             |
             v             |
       APPLY REPEAT        |
          FINE             |
             |             |
             +------+------+
                    |
                    v
           CALCULATE FINAL FINE
                    |
                    v
          CHECK DISQUALIFICATION
                    |
                    v
          DISPLAY VIOLATION FINE
                    |
                    v
          UPDATE TOTAL PENALTY
                    |
                    v
          MORE VIOLATIONS?
              /         \
            YES          NO
             |            |
             v            v
        INPUT NEXT    DISPLAY TOTAL
        VIOLATION       PENALTY
                          |
                          v
                  DISPLAY DISQUALIFICATION
                          |
                          v
                         STOP

```

## 4. Python Source Code

This is a simple educational example using predefined sample fine amounts, not actual legal traffic-fine rates.

```
# Traffic Violation Penalty Calculatorfine_rules = {    "overspeeding": 1000,    "no_helmet": 500,    "no_seatbelt": 500,    "signal_jump": 1000,    "drunk_driving": 5000}disqualification_offences = ["drunk_driving"]total_penalty = 0disqualified = Falsen = int(input("Enter number of violations: "))for i in range(n):    print("\nViolation", i + 1)    vehicle = input("Enter vehicle category (Two-wheeler/Four-wheeler): ").lower()    offence = input("Enter offence type: ").lower()    repeat = input("Is it a repeat offence? (yes/no): ").lower()    if offence in fine_rules:        fine = fine_rules[offence]        if repeat == "yes":            fine = fine * 2        total_penalty += fine
```

## 5. Sample Input

```
Enter number of violations: 3

Violation 1
Enter vehicle category (Two-wheeler/Four-wheeler): Two-wheeler
Enter offence type: no_helmet
Is it a repeat offence? (yes/no): no

Violation 2
Enter vehicle category (Two-wheeler/Four-wheeler): Four-wheeler
Enter offence type: overspeeding
Is it a repeat offence? (yes/no): yes

Violation 3
Enter vehicle category (Two-wheeler/Four-wheeler): Four-wheeler
Enter offence type: drunk_driving
Is it a repeat offence? (yes/no): no
```

## 6. Sample Output

```
Violation 1
Vehicle Category: two-wheeler
Offence: no_helmet
Final Fine: Rs. 500
Disqualification Condition: No

Violation 2
Vehicle Category: four-wheeler
Offence: overspeeding
Final Fine: Rs. 2000
Disqualification Condition: No

Violation 3
Vehicle Category: four-wheeler
Offence: drunk_driving
Final Fine: Rs. 5000
Disqualification Condition: Yes

----- FINAL PENALTY REPORT -----
Total Penalty: Rs. 7500
Status: Disqualification condition identified
Program Completed
```

Note: The program doubles the fine for repeat offences. For this demonstration, drunk driving is treated as a disqualification condition. Actual penalties and legal disqualification rules depend on applicable traffic laws.
