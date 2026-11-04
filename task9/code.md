

## 1. Problem Statement

Develop a Python program to validate sample password strings based on predefined password security rules.

The program should check:

- Minimum length: Password must contain at least 8 characters.
- Uppercase character: Must contain at least one uppercase letter.
- Lowercase character: Must contain at least one lowercase letter.
- Digit: Must contain at least one numeric digit.
- Special character: Must contain at least one special character.
- Repetition: Must not contain three or more consecutive identical characters.
- Prohibited substring: Must not contain prohibited words such as `password`, `admin`, or `1234`.

The program should explain every failed condition and display whether each password is valid or invalid.

## 2. Algorithm

1. Start the program.
2. Define the minimum password length as 8.
3. Define prohibited substrings.
4. Read the number of passwords.
5. Read each password.
6. Check whether the password satisfies the minimum length.
7. Check for uppercase and lowercase characters.
8. Check whether at least one digit exists.
9. Check whether at least one special character exists.
10. Check for three or more consecutive identical characters.
11. Check whether prohibited substrings are present.
12. Display all failed conditions.
13. If no conditions fail, mark the password as valid.
14. Display the validation summary.
15. Stop the program.

## 3. Flowchart

```

                 START
                   |
                   v
          Define password rules
                   |
                   v
          Read number of passwords
                   |
                   v
             Read password
                   |
                   v
          Check minimum length
                   |
                   v
          Check uppercase letter
                   |
                   v
          Check lowercase letter
                   |
                   v
             Check digit
                   |
                   v
          Check special character
                   |
                   v
          Check repeated characters
                   |
                   v
          Check prohibited substring
                   |
                   v
          Are there failed conditions?
               /         \
             Yes          No
              |            |
              v            v
        Display failure  Mark password
           reasons          VALID
              |              |
              +-------+------+
                      |
                      v
             More passwords?
                /       \
              Yes        No
               |          |
               v          v
          Read next    Display summary
          password          |
                            v
                           STOP

```


## 5. Sample Input

```

Enter number of passwords: 3

Enter password: Hello@123

Enter password: abc

Enter password: Admin@1234

```

## 6. Sample Output

```

--- PASSWORD VALIDATION ---

Password Status: VALID
All password policy conditions satisfied.

--- PASSWORD VALIDATION ---

Password Status: INVALID
Failed Conditions:
- Password must contain at least 8 characters
- Missing uppercase letter
- Missing numeric digit
- Missing special character

--- PASSWORD VALIDATION ---

Password Status: INVALID
Failed Conditions:
- Contains prohibited substring: admin
- Contains prohibited substring: 1234

--- FINAL SUMMARY ---
Total Passwords: 3
Valid Passwords: 1
Invalid Passwords: 2

```

