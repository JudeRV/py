import turtle

def draw_square(t, center_x, center_y, side_length):
    t.penup()

    # Calculates one corner of square from its center & side length
    start_pos = (center_x - side_length / 2, center_y + side_length / 2)
    t.goto(start_pos)

    # Draws the actual square
    t.pendown()
    for i in range(4):
        t.forward(side_length)
        t.right(90)

def main():
    t = turtle.Turtle()
    t.speed(0)
    for i in range(20, 1000, 10):
        draw_square(t, 0, 0, i)
        t.right(2)
    input("Enter any key. . . ")

if __name__ == "__main__":
    main()