

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

