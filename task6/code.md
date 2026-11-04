

## 1. Problem Statement

Develop a Python program to generate an examination seating arrangement using nested loops.

The program should:

- Generate seats using row and column identifiers.
- Consider the fixed classroom seating capacity.
- Reserve specified seating positions for special purposes.
- Apply alternate seating restrictions to maintain space between students.
- Assign students to available seats.
- Display the final seating arrangement.
- Identify the total number of students seated and available seats.

## 2. Algorithm

1. Start the program.
2. Read the number of rows and columns.
3. Calculate the total classroom seating capacity.
4. Read the number of students.
5. Read the reserved seating positions.
6. Create an empty seating arrangement.
7. Use nested loops to process each row and column.
8. Skip reserved positions.
9. Apply the alternate seating restriction by leaving alternate columns empty.
10. Assign students to available positions.
11. Display the seating arrangement with row and column identifiers.
12. Display the number of students seated and remaining seats.
13. Stop the program.

## 3. Flowchart

```

               START
                 |
                 v
        Read rows and columns
                 |
                 v
       Calculate classroom capacity
                 |
                 v
         Read number of students
                 |
                 v
         Read reserved positions
                 |
                 v
        Initialize student counter
                 |
                 v
          Start outer row loop
                 |
                 v
        Start inner column loop
                 |
                 v
         Is position reserved?
              /       \
            Yes        No
             |          |
             v          v
        Mark RESERVED  Is column
                       alternate?
                       /      \
                     Yes       No
                      |         |
                      v         v
                  Mark EMPTY  Assign student
                              if available
                      \         /
                       v       v
                   Next column
                       |
                       v
                  Next row
                       |
                       v
              Display seating plan
                       |
                       v
              Display seat summary
                       |
                       v
                      STOP

```


```

## 5. Sample Input

```

Enter number of rows: 3
Enter number of columns: 4

Total Classroom Capacity: 12

Enter number of students: 4

Enter number of reserved seats: 2

Enter reserved row number: 1
Enter reserved column number: 3

Enter reserved row number: 3
Enter reserved column number: 1

```

## 6. Sample Output

```

--- EXAMINATION SEATING ARRANGEMENT ---

Row 1 : [C1:S1] [C2:EMPTY] [C3:RESERVED] [C4:EMPTY]

Row 2 : [C1:S2] [C2:EMPTY] [C3:S3] [C4:EMPTY]

Row 3 : [C1:RESERVED] [C2:EMPTY] [C3:S4] [C4:EMPTY]


--- SEATING SUMMARY ---

Total Classroom Capacity: 12
Total Students: 4
Students Seated: 4
Remaining Students: 0
Reserved Seats: 2
Alternate Empty Seats: 6
Status: All students are seated.

```

