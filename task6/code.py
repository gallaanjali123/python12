

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

capacity = rows * columns

print("Total Classroom Capacity:", capacity)

students = int(input("Enter number of students: "))

# Read reserved positions
reserved_count = int(input("Enter number of reserved seats: "))

reserved = set()

for i in range(reserved_count):
    r = int(input("Enter reserved row number: "))
    c = int(input("Enter reserved column number: "))

    if 1 <= r <= rows and 1 <= c <= columns:
        reserved.add((r, c))
    else:
        print("Invalid reserved position. Ignored.")

# Create seating arrangement
seating = []

student_count = 1
available_seats = 0

print("\n--- EXAMINATION SEATING ARRANGEMENT ---")

# Nested loops for rows and columns
for r in range(1, rows + 1):

    row_seats = []

    for c in range(1, columns + 1):

        # Check reserved position
        if (r, c) in reserved:
            seat = "RESERVED"

        # Alternate seating restriction:
        # Even-numbered columns remain empty
        elif c % 2 == 0:
            seat = "EMPTY"

        # Assign students to available seats
        elif student_count <= students:
            seat = "S" + str(student_count)
            student_count += 1
            available_seats += 1

        else:
            seat = "EMPTY"

        row_seats.append(seat)

    seating.append(row_seats)

# Display seating arrangement
for r in range(rows):

    print("\nRow", r + 1, ":", end=" ")

    for c in range(columns):
        print("[C" + str(c + 1) + ":"
              + seating[r][c] + "]", end=" ")

print("\n\n--- SEATING SUMMARY ---")

seated = student_count - 1
remaining_students = students - seated

print("Total Classroom Capacity:", capacity)
print("Total Students:", students)
print("Students Seated:", seated)
print("Remaining Students:", remaining_students)
print("Reserved Seats:", len(reserved))
print("Alternate Empty Seats:", rows * (columns // 2))

if remaining_students == 0:
    print("Status: All students are seated.")
else:
    print("Status: Insufficient eligible seats.")

