import turtle
import turtleWrap
import warehouse
import Point
import Generation
import copy


class Main:

    turtleWrapper = None
    warehouse = None
    screen = None
    current_position = None
    population = None

    def __init__(self):
        self.turtleWrapper = turtleWrap.TurtleWrapper()
        self.warehouse = warehouse.Warehouse()
        self.population = Generation.Generation()
        self.screen = turtle.Screen()
        self.current_position = Point.Point(round(self.warehouse.WIDTH/2), round(self.warehouse.HEIGHT/2))
        self.init_screen()

    def init_screen(self):
        self.screen = turtle.Screen()
        self.screen.setup(1000, 1000)
        self.screen.title("Algorytm ewolucyjny")

    def up_pressed(self):
        if not self.turtleWrapper.drawing_finished and self.turtleWrapper.move_up():
            self.warehouse.set_way_on_matrix_when_moving_up()

    def down_pressed(self):
        if not self.turtleWrapper.drawing_finished and self.turtleWrapper.move_down():
            self.warehouse.set_way_on_matrix_when_moving_down()

    def left_pressed(self):
        if not self.turtleWrapper.drawing_finished and self.turtleWrapper.move_left():
            self.warehouse.set_way_on_matrix_when_moving_left()

    def right_pressed(self):
        if not self.turtleWrapper.drawing_finished and self.turtleWrapper.move_right():
            self.warehouse.set_way_on_matrix_when_moving_right()

    def finish_drawing(self):
        if self.turtleWrapper.drawing_finished:
            self.warehouse.fill_warehouse()
            # populacja dostaje deep copy magazynu
            self.population.setup_matrix_and_initialize_positions_of_individuals(copy.deepcopy(self.warehouse.matrix),
                                                                                 self.warehouse.free_space_counter)

            self.population.sort_population_by_coverage()
            self.population.print_all_coverages()
            self.warehouse.debug_warehouse_shape() # debug function
            print("Możliwe pokrycie: " + str(self.warehouse.count_posible_coverage()))
            # initializing population

### Tu już mamy zainicjalizowana populacje, polosowane są miejsca

    def reproduce(self):
        print("\nReprodukuj")
        self.population.introduce_new_individuals()
        self.population.sort_population_by_coverage()
        self.population.print_all_coverages()

    def print_final_version(self):
        currently_the_best = self.population.individuals[0]
        for cargo in currently_the_best.cargoList:
            if cargo.inWarehouse is True:
                self.turtleWrapper.draw_cargo(cargo)
    def start(self):
        self.screen.onkey(self.exit_program, "q")
        self.screen.onkey(self.up_pressed, "Up")
        self.screen.onkey(self.down_pressed, "Down")
        self.screen.onkey(self.left_pressed, "Left")
        self.screen.onkey(self.right_pressed, "Right")
        self.screen.onkey(self.finish_drawing, "k")
        self.screen.onkey(self.reproduce, "space")
        self.screen.onkey(self.print_final_version, "f")
        self.screen.listen()
        self.screen.mainloop()

    def exit_program(self):
        self.screen.bye()


################# PROGRAM ###################
program = Main()
program.start()
