


import string

# Password policy rules
MIN_LENGTH = 8

prohibited_words = ["password", "admin", "1234"]

n = int(input("Enter number of passwords: "))

valid_count = 0
invalid_count = 0

# Validate each password
for i in range(n):

    password = input("\nEnter password: ")

    errors = []

    # Check minimum length
    if len(password) < MIN_LENGTH:
        errors.append("Password must contain at least 8 characters")

    # Check uppercase letter
    if not any(ch.isupper() for ch in password):
        errors.append("Missing uppercase letter")

    # Check lowercase letter
    if not any(ch.islower() for ch in password):
        errors.append("Missing lowercase letter")

    # Check digit
    if not any(ch.isdigit() for ch in password):
        errors.append("Missing numeric digit")

    # Check special character
    if not any(ch in string.punctuation for ch in password):
        errors.append("Missing special character")

    # Check three or more consecutive repeated characters
    repeated = False

    for j in range(len(password) - 2):
        if password[j] == password[j + 1] == password[j + 2]:
            repeated = True
            break

    if repeated:
        errors.append("Three or more consecutive identical characters")

    # Check prohibited substrings
    for word in prohibited_words:
        if word in password.lower():
            errors.append("Contains prohibited substring: " + word)

    # Display validation result
    print("\n--- PASSWORD VALIDATION ---")

    if errors:

        print("Password Status: INVALID")
        print("Failed Conditions:")

        for error in errors:
            print("-", error)

        invalid_count += 1

    else:

        print("Password Status: VALID")
        print("All password policy conditions satisfied.")

        valid_count += 1

# Final summary
print("\n--- FINAL SUMMARY ---")
print("Total Passwords:", n)
print("Valid Passwords:", valid_count)
print("Invalid Passwords:", invalid_count)

