def draw_bot():
    while True:
        print("Draw Bot")
        print("1. Draw a square")
        print("2. Draw a triangle")
        print("3. Draw a circle")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            size = int(input("Enter the size of the square: "))
            draw_square(size)
        elif choice == "2":
            size = int(input("Enter the size of the triangle: "))
            draw_triangle(size)
        elif choice == "3":
            size = int(input("Enter the size of the circle: "))
            draw_circle(size)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def draw_square(size):
    for _ in range(size):
        print("*" * size)

def draw_triangle(size):
    for i in range(1, size + 1):
        print("*" * i)

def draw_circle(size):
    for i in range(size):
        angle = 2 * 3.14 * i / size
        x = int(size * (0.5 + 0.4 * (1 - abs(math.sin(angle)))))
        print(" " * (size - x) + "*" * (2 * x))

draw_bot()
