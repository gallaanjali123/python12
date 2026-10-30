

import string

def validate_email(email):

    errors = []

    # Check @ symbol
    if email.count("@") != 1:
        errors.append("Email must contain exactly one @ symbol")
        return errors

    username, domain_part = email.split("@")

    # Check missing username
    if username == "":
        errors.append("Missing username")

    # Check missing domain
    if domain_part == "":
        errors.append("Missing domain")

    # Validate username
    if username:

        allowed_username = (
            string.ascii_letters +
            string.digits + "._"
        )

        for ch in username:
            if ch not in allowed_username:
                errors.append("Invalid character in username")
                break

        if username.startswith(".") or username.endswith("."):
            errors.append("Username cannot start or end with a dot")

        if ".." in username:
            errors.append("Malformed consecutive dots in username")

    # Validate domain and extension
    if domain_part:

        if "." not in domain_part:
            errors.append("Missing domain extension")

        else:
            parts = domain_part.split(".")

            if len(parts) != 2:
                errors.append("Malformed domain separators")

            else:
                domain, extension = parts

                if domain == "":
                    errors.append("Missing domain name")

                if extension == "":
                    errors.append("Missing email extension")

                if domain:
                    allowed_domain = (
                        string.ascii_letters +
                        string.digits + "-"
                    )

                    for ch in domain:
                        if ch not in allowed_domain:
                            errors.append("Invalid character in domain")
                            break

                    if domain.startswith("-") or domain.endswith("-"):
                        errors.append("Invalid domain hyphen placement")

                if extension:
                    if len(extension) < 2:
                        errors.append("Extension must contain at least 2 letters")

                    if not extension.isalpha():
                        errors.append("Extension must contain only letters")

    return errors


def validate_student_id(student_id):

    errors = []

    # Check length
    if len(student_id) != 11:
        errors.append("Registration ID must contain 11 characters")
        return errors

    # Check prefix
    if student_id[0:3] != "NRI":
        errors.append("Invalid college prefix")

    # Check year digits
    if not student_id[3:5].isdigit():
        errors.append("Year component must contain digits")

    # Check department code
    if not student_id[5:8].isalpha() or not student_id[5:8].isupper():
        errors.append("Department component must contain 3 uppercase letters")

    # Check student number
    if not student_id[8:11].isdigit():
        errors.append("Student number must contain 3 digits")

    return errors


# Main program

n = int(input("Enter number of students: "))

valid_count = 0
invalid_count = 0

for i in range(n):

    print("\nStudent", i + 1)

    email = input("Enter student email: ")
    student_id = input("Enter registration ID: ")

    email_errors = validate_email(email)
    id_errors = validate_student_id(student_id)

    print("\n--- VALIDATION REPORT ---")

    print("Email:", email)

    if email_errors:
        print("Email Status: INVALID")

        for error in email_errors:
            print("-", error)

    else:
        print("Email Status: VALID")

    print("\nRegistration ID:", student_id)

    if id_errors:
        print("ID Status: INVALID")

        for error in id_errors:
            print("-", error)

    else:
        print("ID Status: VALID")

    if not email_errors and not id_errors:
        print("\nOverall Status: VALID")
        valid_count += 1

    else:
        print("\nOverall Status: INVALID")
        invalid_count += 1


# Final summary

print("\n--- FINAL SUMMARY ---")
print("Total Students:", n)
print("Valid Records:", valid_count)
print("Invalid Records:", invalid_count)

