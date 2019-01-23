import turtle
import warehouse
import Point


class TurtleWrapper:
    tut = None
    previous_key = None
    starting_position = None  # Wspolrzedne
    current_position = None          # Indeksy
    drawing_finished = False
    possible_finish_coordinates = [[0, 0], [0, -0], [-0, 0], [-0, -0]]

    def __init__(self):
        self.tut = turtle.Turtle()
        self.tut.speed(0)  # prevents delays
        self.starting_position = self.tut.pos()
        self.current_position = Point.Point(warehouse.Warehouse.WIDTH/2, warehouse.Warehouse.HEIGHT/2)

    def move_forward(self):
        print(self.get_current_position())
        if self.drawing_finished is False:
            self.tut.forward(50)
            if self.get_current_position() in self.possible_finish_coordinates:
                print("KONIEC RYSOWANIA MAGAZYNU")
                self.drawing_finished = True

    def move_up(self):
        if self.previous_key == "DOWN":
            return False
        else:
            self.turn_north()
            self.move_forward()
            self.previous_key = "UP"
            return True

    def draw_cargo(self, cargo):
        self.tut.penup()
        self.tut.goto((cargo.position.index_y - 50) * 10, -(cargo.position.index_x - 50)*10)
        self.turn_east()
        self.tut.pendown()
        self.tut.forward(cargo.width * 10)
        self.turn_south()
        self.tut.forward(cargo.height * 10)
        self.turn_west()
        self.tut.forward(cargo.width * 10)
        self.turn_north()
        self.tut.forward(cargo.height * 10)

    def move_down(self):
        if self.previous_key == "UP":
            return False
        else:
            self.turn_south()
            self.move_forward()
            self.previous_key = "DOWN"
            return True

    def move_right(self):
        if self.previous_key == "LEFT":
            return False
        else:
            self.turn_east()
            self.move_forward()
            self.previous_key = "RIGHT"
            return True

    def move_left(self):
        if self.previous_key == "RIGHT":
            return False
        else:
            self.turn_west()
            self.move_forward()
            self.previous_key = "LEFT"
            return True

    def turn_north(self):
        self.tut.setheading(90)

    def turn_south(self):
        self.tut.setheading(270)

    def turn_east(self):
        self.tut.setheading(0)

    def turn_west(self):
        self.tut.setheading(180)

    def get_current_position(self):
        return [int(round(self.tut.pos()[0])), int(round(self.tut.pos()[1]))]



