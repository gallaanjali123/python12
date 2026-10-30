

fine_rules = {
    "overspeeding": 1000,
    "no_helmet": 500,
    "no_seatbelt": 500,
    "signal_jump": 1000,
    "drunk_driving": 5000
}

disqualification_offences = ["drunk_driving"]

total_penalty = 0
disqualified = False

n = int(input("Enter number of violations: "))

for i in range(n):
    print("\nViolation", i + 1)

    vehicle = input("Enter vehicle category (Two-wheeler/Four-wheeler): ").lower()

    offence = input("Enter offence type: ").lower()

    repeat = input("Is it a repeat offence? (yes/no): ").lower()

    if offence in fine_rules:

        fine = fine_rules[offence]

        if repeat == "yes":
            fine = fine * 2

        total_penalty += fine

        print("Vehicle Category:", vehicle)
        print("Offence:", offence)
        print("Final Fine: Rs.", fine)

        if offence in disqualification_offences:
            disqualified = True
            print("Disqualification Condition: Yes")
        else:
            print("Disqualification Condition: No")

    else:
        print("Invalid offence type")

print("\n----- FINAL PENALTY REPORT -----")

print("Total Penalty: Rs.", total_penalty)

if disqualified:
    print("Status: Disqualification condition identified")
else:
    print("Status: No disqualification condition identified")

print("Program Completed")

