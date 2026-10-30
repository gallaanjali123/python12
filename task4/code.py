

# Hypothetical courier service details
services = {
    "Standard": {
        "max_weight": 10,
        "max_dimension": 100,
        "zones": ["Local", "Regional", "National"],
        "urgencies": ["Normal"],
        "restrictions": ["None"],
        "base_charge": 40
    },

    "Express": {
        "max_weight": 20,
        "max_dimension": 150,
        "zones": ["Local", "Regional", "National"],
        "urgencies": ["Normal", "Urgent"],
        "restrictions": ["None", "Fragile"],
        "base_charge": 80
    },

    "Premium": {
        "max_weight": 30,
        "max_dimension": 200,
        "zones": ["Local", "Regional", "National"],
        "urgencies": ["Normal", "Urgent"],
        "restrictions": ["None", "Fragile", "Temperature"],
        "base_charge": 120
    }
}

# Read parcel details
weight = float(input("Enter parcel weight (kg): "))

length = float(input("Enter length (cm): "))
width = float(input("Enter width (cm): "))
height = float(input("Enter height (cm): "))

zone = input("Enter distance zone (Local/Regional/National): ")
urgency = input("Enter urgency (Normal/Urgent): ")
restriction = input("Enter restriction (None/Fragile/Temperature): ")
volumetric_weight = volume / 5000
billable_weight = max(weight, volumetric_weight)

eligible_services = []
rejected_services = {}

print("\n--- COURIER SERVICE COMPARISON ---")

for name, details in services.items():

    reasons = []

    if billable_weight > details["max_weight"]:
        reasons.append("Weight limit exceeded")

    if max(length, width, height) > details["max_dimension"]:
        reasons.append("Dimension limit exceeded")

    if zone not in details["zones"]:
        reasons.append("Distance zone not supported")

    if urgency not in details["urgencies"]:
        reasons.append("Urgency not supported")

    if restriction not in details["restrictions"]:
        reasons.append("Restriction not supported")

    if reasons:
        rejected_services[name] = reasons
        print("\n", name, "- NOT ELIGIBLE")

        for reason in reasons:
            print("-", reason)

    else:
        # Hypothetical charge calculation
        weight_charge = billable_weight * 10

        zone_charge = {
            "Local": 20,
            "Regional": 50,
            "National": 100
        }

        urgency_charge = {
            "Normal": 0,
            "Urgent": 50
        }

        total_charge = (
            details["base_charge"]
            + weight_charge
            + zone_charge[zone]
            + urgency_charge[urgency]
        )

        eligible_services.append((name, total_charge))

        print("\n", name, "- ELIGIBLE")
        print("Delivery Charge: Rs.", round(total_charge, 2))

# Select the cheapest eligible service
print("\n--- FINAL RESULT ---")

if eligible_services:

    best_service = min(eligible_services, key=lambda x: x[1])

    print("Selected Courier:", best_service[0])
    print("Minimum Delivery Charge: Rs.",
          round(best_service[1], 2))

else:
    print("No eligible courier service available.")

