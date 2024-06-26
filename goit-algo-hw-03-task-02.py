import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    order = int(input("Введіть рівень рекурсії (ціле число): "))

    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, order, 300)
        t.right(120)
    turtle.done()

if __name__ == "__main__":
    main()
