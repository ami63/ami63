n = int(input("Enter the number of row: "))

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()

# Que 2 ============

n = int(input ("Enter the number of rows: "))

for i in range(n, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()