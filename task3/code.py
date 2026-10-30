
unavailable_rooms = ["R3", "R5"]

timetable = []

n = int(input("Enter number of courses: "))
for i in range(n):
    print("\nCourse", i + 1)

    course = input("Enter course name: ")
    day = input("Enter day: ")
    start = int(input("Enter start time (24-hour format): "))
    end = int(input("Enter end time (24-hour format): "))
    room = input("Enter room number: ")

  
    timetable.append((course, day, start, end, room))

print("\n--- TIMETABLE VALIDATION REPORT ---")

conflicts = []
for item in timetable:
    course, day, start, end, room = item

    if room in unavailable_rooms:
        message = course + ": Room " + room + " is unavailable"
        conflicts.append(message)


for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):

        c1, d1, s1, e1, r1 = timetable[i]
        c2, d2, s2, e2, r2 = timetable[j]

        
        if d1 == d2 and s1 < e2 and s2 < e1:

            # Student timetable conflict
            message = c1 + " and " + c2 + \
                      " have overlapping class periods"
            conflicts.append(message)

            # Check room conflict
            if r1 == r2:
                message = "Room " + r1 + " is assigned to both " + \
                          c1 + " and " + c2 + " at overlapping times"
                conflicts.append(message)


if conflicts:
    print("\nConflicts detected:")

    for conflict in conflicts:
        print("-", conflict)

    print("\nTimetable Status: INVALID")

else:
    print("\nNo conflicts detected.")
    print("Timetable Status: VALID")


print("\n--- PROPOSED TIMETABLE ---")

for item in timetable:
    print(item)

