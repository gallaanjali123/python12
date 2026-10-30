


print("1. Hollow Diamond Pattern")
print("2. Symmetric Number Pattern")

choice = int(input("Enter your choice (1 or 2): "))

n = int(input("Enter pattern size (positive odd number): "))

# Validate dimensions
if n <= 0 or n % 2 == 0:
    print("Invalid dimension! Enter a positive odd number.")

elif choice == 1:

    print("\n--- HOLLOW DIAMOND PATTERN ---")

    mid = n // 2

    # Upper half including middle row
    for i in range(mid + 1):

        spaces = mid - i
        print(" " * spaces, end="")

        for j in range(2 * i + 1):

            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")

        print()

    # Lower half
    for i in range(mid - 1, -1, -1):

        spaces = mid - i
        print(" " * spaces, end="")

        for j in range(2 * i + 1):

            if j == 0 or j == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")

        print()

elif choice == 2:

    print("\n--- SYMMETRIC NUMBER PATTERN ---")

    mid = n // 2

    # Upper half
    for i in range(mid + 1):

        # Leading spaces
        print(" " * (mid - i), end="")

        # Increasing numbers
        for j in range(1, i + 2):
            print(j, end="")

        # Decreasing numbers
        for j in range(i, 0, -1):
            print(j, end="")

        print()

    # Lower half
    for i in range(mid - 1, -1, -1):

        print(" " * (mid - i), end="")

        for j in range(1, i + 2):
            print(j, end="")

        for j in range(i, 0, -1):
            print(j, end="")

        print()

else:
    print("Invalid choice! Select 1 or 2.")

