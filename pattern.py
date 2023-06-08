def draw_diamond(rows):
    for i in range(1, rows+1):
        for j in range(1, rows-i+1):
            print(" ", end="")
        for k in range(1, 2*i):
            print("*", end="")
        print()

    for i in range(rows-1, 0, -1):
        for j in range(1, rows-i+1):
            print(" ", end="")
        for k in range(1, 2*i):
            print("*", end="")
        print()

rows = int(input("Enter the number of rows: "))
draw_diamond(rows)
