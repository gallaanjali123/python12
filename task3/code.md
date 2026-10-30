

## 1. Problem Statement

Develop a Python program to validate a proposed student timetable. Course schedules are represented using strings and tuples containing course names, days, time periods, and room numbers.

The program should:

- Detect overlapping class periods on the same day.
- Identify rooms that are unavailable.
- Check whether two courses are assigned to the same room at overlapping times.
- Validate the proposed timetable.
- Display the conflicts and final timetable status.

## 2. Algorithm

1. Start the program.
2. Define the list of unavailable rooms.
3. Read the number of courses.
4. For each course, read the course name, day, start time, end time, and room number.
5. Store the schedule details in tuples.
6. Check whether the assigned room is unavailable.
7. Compare each course with the remaining courses.
8. Check whether two courses overlap on the same day.
9. If overlapping courses are assigned to the same student, report a timetable conflict.
10. If overlapping courses use the same room, report a room conflict.
11. Display all conflicts.
12. Display whether the proposed timetable is valid.
13. Stop.

## 3. Flowchart

```

             START
               |
               v
       Define unavailable rooms
               |
               v
       Read number of courses
               |
               v
       Read course details
       (Name, Day, Start, End, Room)
               |
               v
        Store details in tuples
               |
               v
        Is room unavailable?
            /       \
          Yes        No
           |          |
           v          v
      Report room   Continue
       unavailable
           \          /
            v        v
       Compare course schedules
               |
               v
       Same day and overlapping?
            /       \
          Yes        No
           |          |
           v          v
      Report student  Compare next
        conflict      courses
           |
           v
       Same room also?
          /      \
        Yes       No
         |         |
         v         v
    Report room  Continue
      conflict
         |
         v
       More courses?
         /      \
       Yes       No
        |         |
        v         v
    Compare    Display conflicts
    next pair  and final status
                   |
                   v
                  STOP

```

## 4. Python Source Code

```
# Student Timetable Conflict Detection# List of unavailable roomsunavailable_rooms = ["R3", "R5"]timetable = []n = int(input("Enter number of courses: "))# Read course detailsfor i in range(n):    print("\nCourse", i + 1)    course = input("Enter course name: ")    day = input("Enter day: ")    start = int(input("Enter start time (24-hour format): "))    end = int(input("Enter end time (24-hour format): "))    room = input("Enter room number: ")    # Store details as a tuple    timetable.append((course, day, start, end, room))print("\n--- TIMETABLE VALIDATION REPORT ---")conflicts = []# Check unavailable roomsfor item in timetable:    course, day, start, end, room = item    if room in unavailable_rooms:        message = course + ": Room " + room + " is unavailable"        conflicts.append(message)# Compare course schedules
```

## 5. Sample Input

```

Enter number of courses: 4

Course 1
Enter course name: Python
Enter day: Monday
Enter start time (24-hour format): 9
Enter end time (24-hour format): 11
Enter room number: R1

Course 2
Enter course name: Mathematics
Enter day: Monday
Enter start time (24-hour format): 10
Enter end time (24-hour format): 12
Enter room number: R2

Course 3
Enter course name: Physics
Enter day: Tuesday
Enter start time (24-hour format): 9
Enter end time (24-hour format): 11
Enter room number: R3

Course 4
Enter course name: English
Enter day: Monday
Enter start time (24-hour format): 13
Enter end time (24-hour format): 14
Enter room number: R1

```

## 6. Sample Output

```

--- TIMETABLE VALIDATION REPORT ---

Conflicts detected:
- Python and Mathematics have overlapping class periods
- Physics: Room R3 is unavailable

Timetable Status: INVALID

--- PROPOSED TIMETABLE ---
('Python', 'Monday', 9, 11, 'R1')
('Mathematics', 'Monday', 10, 12, 'R2')
('Physics', 'Tuesday', 9, 11, 'R3')
('English', 'Monday', 13, 14, 'R1')

```


