

## 1. Problem Statement

Develop a Python program to generate advanced numerical patterns based on user-specified dimensions.

The program should:

- Generate a hollow diamond pattern.
- Generate a symmetric numerical pattern.
- Accept the pattern size from the user.
- Validate the entered dimensions.
- Display an error message for invalid dimensions.
- Use nested loops and proper spacing to produce aligned patterns.

## 2. Algorithm

1. Start the program.
2. Display the pattern choices:
   - Hollow Diamond
   - Symmetric Number Pattern
3. Read the user's choice.
4. Read the pattern size.
5. Check whether the size is a positive odd integer.
6. If the size is invalid, display an error message.
7. If the user selects a hollow diamond:
   - Generate the upper half using nested loops.
   - Print numbers or symbols at the boundary positions.
   - Generate the lower half in reverse order.
8. If the user selects a symmetric number pattern:
   - Generate increasing numbers from 1 to the row number.
   - Generate decreasing numbers to create symmetry.
9. Display the generated pattern.
10. Stop the program.

## 3. Flowchart

```

                START
                  |
                  v
          Display pattern choices
                  |
                  v
          Read user choice
                  |
                  v
          Read pattern size
                  |
                  v
          Is size a positive
             odd integer?
              /       \
            No         Yes
            |           |
            v           v
       Display error  Check pattern choice
                         |
                 +-------+-------+
                 |               |
                 v               v
           Hollow Diamond   Symmetric Pattern
                 |               |
                 v               v
           Generate upper   Generate number
               half           sequences
                 |               |
                 v               v
           Generate lower   Arrange numbers
               half          symmetrically
                 |               |
                 +-------+-------+
                         |
                         v
                  Display pattern
                         |
                         v
                        STOP

```

## 4. Python Source Code

```
            if j == 0 or j == 2 * i:                print("*", end="")            else:                print(" ", end="")        print()elif choice == 2:    print("\n--- SYMMETRIC NUMBER PATTERN ---")    mid = n // 2    # Upper half    for i in range(mid + 1):        # Leading spaces        print(" " * (mid - i), end="")        # Increasing numbers        for j in range(1, i + 2):            print(j, end="")        # Decreasing numbers        for j in range(i, 0, -1):            print(j, end="")        print()    # Lower half    for i in range(mid - 1, -1, -1):        print(" " * (mid - i), end="")        for j in range(1, i + 2):            print(j, end="")        for j in range(i, 0, -1):            print(j, end="")        print()else:    print("Invalid choice! Select 1 or 2.")
```

## 5. Sample Input 1

HOLLOW DIAMOND

```

1. Hollow Diamond Pattern
2. Symmetric Number Pattern

Enter your choice (1 or 2): 1
Enter pattern size (positive odd number): 5

```

## 6. Sample Output 1

HOLLOW DIAMOND PATTERN

```

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *

```

## 7. Sample Input 2

SYMMETRIC NUMBER PATTERN

```

1. Hollow Diamond Pattern
2. Symmetric Number Pattern

Enter your choice (1 or 2): 2
Enter pattern size (positive odd number): 5

```

## 8. Sample Output 2

SYMMETRIC NUMBER PATTERN

```

    1
   121
  12321
 1234321
123454321
 1234321
  12321
   121
    1

```

## 9. Sample Input 3 – Invalid Dimension

```

1. Hollow Diamond Pattern
2. Symmetric Number Pattern

Enter your choice (1 or 2): 1
Enter pattern size (positive odd number): 4

```

## 10. Sample Output 3

```

Invalid dimension! Enter a positive odd number.

```

## 11. Result

The Python program successfully generates hollow diamond and symmetric numerical patterns using nested loops. It also validates user-specified dimensions and displays an error message for invalid input.

Python concepts used: Nested loops, `range()`, conditional statements, string multiplication, arithmetic operations, and input validation.
