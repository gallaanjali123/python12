

## 1. Problem Statement

Develop a Python program to calculate courier delivery charges based on parcel weight, dimensions, distance zones, delivery urgency, and declared restrictions.

The program should compare different courier service options, check their eligibility based on parcel requirements, calculate the delivery charges, and select the most economical eligible service.

The program should also display ineligible services with their reasons for rejection.



## 2. Algorithm

1. Start the program.
2. Define courier service options with their weight limits, dimension limits, and supported restrictions.
3. Read parcel weight, length, width, and height.
4. Read the distance zone and delivery urgency.
5. Read the parcel restriction type.
6. Calculate the parcel volume.
7. Check each courier service for:
   - Maximum weight limit.
   - Maximum dimension limit.
   - Supported distance zone.
   - Delivery urgency availability.
   - Restriction compatibility.
8. Calculate charges for eligible services.
9. Compare all eligible courier services.
10. Select the service with the lowest delivery charge.
11. Display the service comparison and selected courier.
12. Stop.

## 3. Flowchart

```

                START
                  |
                  v
         Define courier services
                  |
                  v
          Read parcel details
       (Weight and dimensions)
                  |
                  v
       Read distance zone,
       urgency and restrictions
                  |
                  v
         Calculate parcel volume
                  |
                  v
         Check each courier service
                  |
                  v
         Check weight and dimensions
                  |
                  v
         Check zone and urgency
                  |
                  v
         Check restrictions
                  |
                  v
          Is service eligible?
             /          \
           No            Yes
           |              |
           v              v
       Record reason   Calculate charge
       for rejection        |
           |                v
           |          Store service
           |          and its charge
           |                |
           +-------+--------+
                   |
                   v
          More services to check?
              /          \
            Yes            No
             |              |
             v              v
         Check next     Any eligible
         service         service?
                       /        \
                     No          Yes
                     |            |
                     v            v
                Display no    Select lowest
                eligible      charge service
                service           |
                     |            v
                     +------> Display report
                                  |
                                  v
                                 STOP

```

## 4. Python Source Code

```
    reasons = []    if billable_weight > details["max_weight"]:        reasons.append("Weight limit exceeded")    if max(length, width, height) > details["max_dimension"]:        reasons.append("Dimension limit exceeded")    if zone not in details["zones"]:        reasons.append("Distance zone not supported")    if urgency not in details["urgencies"]:        reasons.append("Urgency not supported")    if restriction not in details["restrictions"]:        reasons.append("Restriction not supported")    if reasons:        rejected_services[name] = reasons        print("\n", name, "- NOT ELIGIBLE")        for reason in reasons:            print("-", reason)    else:        # Hypothetical charge calculation        weight_charge = billable_weight * 10        zone_charge = {            "Local": 20,            "Regional": 50,            "National": 100        }        urgency_charge = {            "Normal": 0,            "Urgent": 50        }        total_charge = (            details["base_charge"]            + weight_charge            + zone_charge[zone]            + urgency_charge[urgency]        )        eligible_services.append((name, total_charge))        print("\n", name, "- ELIGIBLE")        print("Delivery Charge: Rs.", round(total_charge, 2))# Select the cheapest eligible serviceprint("\n--- FINAL RESULT ---")if eligible_services:    best_service = min(eligible_services, key=lambda x: x[1])    print("Selected Courier:", best_service[0])    print("Minimum Delivery Charge: Rs.",          round(best_service[1], 2))else:    print("No eligible courier service available.")
```

## 5. Sample Input

```

Enter parcel weight (kg): 5

Enter length (cm): 30
Enter width (cm): 20
Enter height (cm): 15

Enter distance zone (Local/Regional/National): National
Enter urgency (Normal/Urgent): Urgent
Enter restriction (None/Fragile/Temperature): Fragile

```

## 6. Sample Output

```

--- COURIER SERVICE COMPARISON ---

 Standard - NOT ELIGIBLE
- Urgency not supported
- Restriction not supported

 Express - ELIGIBLE
Delivery Charge: Rs. 180.0

 Premium - ELIGIBLE
Delivery Charge: Rs. 220.0

--- FINAL RESULT ---

Selected Courier: Express
Minimum Delivery Charge: Rs. 180.0

```

## 7. Result

The Python program successfully validates parcel details, checks courier service restrictions, calculates delivery charges, compares eligible services, and selects the courier service with the lowest delivery cost.

Concepts used: Python dictionaries, tuples, lists, loops, conditional statements, functions such as `max()` and `min()`, and arithmetic operations.
