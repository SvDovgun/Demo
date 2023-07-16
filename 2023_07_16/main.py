import turtle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
HALL_HEADER = 150
FOND_SIZE = 20

ROW = 3
COlUMN = 5

main_screen = turtle.Screen()
main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.setworldcoordinates(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.title("Cinema")

main_turtle = turtle.Turtle()
main_turtle.hideturtle()
main_turtle.speed(0)
main_turtle.penup()

main_writer = turtle.Turtle()
main_writer.hideturtle()
main_writer.speed(0)
main_writer.penup()

cell_width = SCREEN_WIDTH / COlUMN
cell_height = (SCREEN_HEIGHT - HALL_HEADER) / ROW

# print(cell_width, cell_height)
# main_turtle.circle(100)

seat_radius = (cell_height * 0.8)/ 2

x = cell_width / 2
y = (cell_height / 2) - seat_radius

seats = {}

for r in range(ROW):
    for c in range(COlUMN):
        seats[(x, y)] = False
        x += cell_width
    x = cell_width / 2
    y += cell_height 


def write_free_seats():
    main_screen.tracer(False)
    main_writer.clear()
    main_writer.setposition(10, SCREEN_HEIGHT - (FOND_SIZE * 2))
    main_writer.pendown()
    free_seats = len(seats.values()) - sum(seats.values())
    main_writer.write(f"Free seats: {free_seats}", font=("Times New Roman", FOND_SIZE, "bold"))
    main_writer.penup()
    main_screen.tracer(True)


def draw_seat(x, y, color="steel blue"):
    main_turtle.setposition(x, y) #(*seat)
    main_turtle.pendown()
    main_turtle.begin_fill()
    main_turtle.circle(seat_radius)
    main_turtle.fillcolor(color)
    main_turtle.end_fill()
    main_turtle.penup()


def get_seat(x, y):
    for _x, _y in seats:
        distance = ((x - _x)**2 + (y - (_y + seat_radius))**2)**0.5
        if distance <= seat_radius:
            return _x, _y


def book_seat(x, y):
#    print(x, y)
#    print(get_seat(x, y))
    seat_coord = get_seat(x, y)
    if seat_coord:
        seats[seat_coord] = True
        draw_seat(*seat_coord, color = "tomato")
        write_free_seats()



main_screen.tracer(False)
for seat in seats: 
#    print(seat)
    draw_seat(*seat)

main_screen.tracer(True)

write_free_seats()

#main_screen.onclick(on_click)

main_screen.onclick(book_seat)
#main_screen.onclick(book_seat, btn=3)
main_screen.mainloop()