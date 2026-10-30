

## 1. Problem Statement

Develop a Python program to validate student email-like strings and registration identifiers according to predefined formatting rules.

The program should:

- Check whether the student email contains the required components.
- Validate the presence of exactly one `@` symbol.
- Check whether the email contains a valid domain and extension.
- Identify malformed separators and invalid characters.
- Validate student registration identifiers.
- Check for missing components and incorrect identifier formats.
- Display the validation result and explain each error.

Validation rules used in this program:

Email format:

- Must contain a username, `@` symbol, domain name, and extension.
- Username can contain letters, digits, dots, and underscores.
- Domain can contain letters, digits, and hyphens.
- Extension must contain at least two letters.
- Username and domain cannot start or end with a dot.

Registration ID format:

- Must follow the format `NRI26CSE001`.
- First three characters must be `NRI`.
- Next two characters must be digits.
- Next three characters must be uppercase letters.
- Last three characters must be digits.

## 2. Algorithm

1. Start the program.
2. Read the number of student records.
3. Read the student email and registration ID.
4. Split the email using the `@` symbol.
5. Check whether exactly one `@` symbol exists.
6. Validate the username, domain, and extension.
7. Identify invalid characters and malformed separators.
8. Check whether the registration ID contains exactly 11 characters.
9. Validate each registration ID component.
10. Store all validation errors.
11. Display valid or invalid status for the email and registration ID.
12. Display the final validation summary.
13. Stop the program.

## 3. Flowchart

```

                 START
                   |
                   v
          Read number of students
                   |
                   v
          Read email and student ID
                   |
                   v
             Validate email
                   |
                   v
          Check number of @ symbols
                   |
                   v
          Check username component
                   |
                   v
          Check domain and extension
                   |
                   v
          Check invalid characters
                   |
                   v
          Validate registration ID
                   |
                   v
          Check ID length and format
                   |
                   v
          Are validation errors present?
                /          \
              Yes           No
               |             |
               v             v
         Display errors   Mark VALID
               |             |
               +------+------+
                      |
                      v
            Display student results
                      |
                      v
             More student records?
                 /       \
               Yes        No
                |          |
                v          v
            Read next   Display summary
            record           |
                             v
                            STOP

```

## 4. Python Source Code

```
# Student Email and Identifier Validationimport stringdef validate_email(email):    errors = []    # Check @ symbol    if email.count("@") != 1:        errors.append("Email must contain exactly one @ symbol")        return errors    username, domain_part = email.split("@")    # Check missing username    if username == "":        errors.append("Missing username")    # Check missing domain    if domain_part == "":        errors.append("Missing domain")    # Validate username    if username:        allowed_username = (            string.ascii_letters +            string.digits + "._"        )        for ch in username:            if ch not in allowed_username:                errors.append("Invalid character in username")                break
```

## 5. Sample Input

```

Enter number of students: 3

Student 1
Enter student email: priya@nri.edu
Enter registration ID: NRI26CSE001

Student 2
Enter student email: ravi@@gmail.com
Enter registration ID: NRI26CSE02A

Student 3
Enter student email: @college.com
Enter registration ID: ABC26CSE002

```

## 6. Sample Output

```

--- VALIDATION REPORT ---

Email: priya@nri.edu
Email Status: VALID

Registration ID: NRI26CSE001
ID Status: VALID

Overall Status: VALID


--- VALIDATION REPORT ---

Email: ravi@@gmail.com
Email Status: INVALID
- Email must contain exactly one @ symbol

Registration ID: NRI26CSE02A
ID Status: INVALID
- Student number must contain 3 digits

Overall Status: INVALID


--- VALIDATION REPORT ---

Email: @college.com
Email Status: INVALID
- Missing username

Registration ID: ABC26CSE002
ID Status: INVALID
- Invalid college prefix

Overall Status: INVALID


--- FINAL SUMMARY ---
Total Students: 3
Valid Records: 1
Invalid Records: 2

```

## 7. Result

The Python program successfully validates student email-like strings and registration identifiers. It identifies malformed separators, invalid characters, missing components, and incorrect identifier formats, and displays detailed validation reports.

Python concepts used: Strings, functions, lists, loops, conditional statements, string slicing, `split()`, `count()`, `isalpha()`, `isdigit()`, and `isupper()`.


