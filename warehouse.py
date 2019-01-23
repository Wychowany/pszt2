import Cargo

ALREADY_CHECKED = 2
CARGO = 1
FREE_SPACE = 0
WALL = -2
ENTRANCE = -1
OUT_OF_BOUNDS = -3

CARGO_LIST = [Cargo.Square1x1(), Cargo.Square2x2(), Cargo.Square5x5(), Cargo.Rectangle1x2(), Cargo.Rectangle2x1(),
              Cargo.Rectangle2x3(), Cargo.Rectangle3x2()]


class Warehouse:

    matrix = None
    WIDTH = 100
    HEIGHT = 100
    entrance = None
    index_x = 50
    index_y = 50
    first = True
    free_space_counter = 0

    def __init__(self):
        self.matrix = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        self.init_matrix()

    def init_matrix(self):
        for j in range(self.WIDTH):
            for i in range(self.HEIGHT):
                self.matrix[i][j] = OUT_OF_BOUNDS

    def set_way_on_matrix_when_moving_up(self):
        for i in range(5):
            self.matrix[self.index_x - i][self.index_y] = WALL

        if self.first is True:
            self.matrix[self.index_x][self.index_y] = ENTRANCE
            self.first = False
        self.index_x -= 5

    def set_way_on_matrix_when_moving_down(self):
        for i in range(5):
            self.matrix[self.index_x + i][self.index_y] = WALL

        if self.first is True:
            self.matrix[self.index_x][self.index_y] = ENTRANCE
            self.first = False

        self.index_x += 5

    def set_way_on_matrix_when_moving_left(self):
        for i in range(5):
            self.matrix[self.index_x][self.index_y - i] = WALL

            if self.first is True:
                self.matrix[self.index_x][self.index_y] = ENTRANCE
                self.first = False

        self.index_y -= 5

    def set_way_on_matrix_when_moving_right(self):
        for i in range(5):
            self.matrix[self.index_x][self.index_y + i] = WALL

        if self.first is True:
            self.matrix[self.index_x][self.index_y] = ENTRANCE
            self.first = False

        self.index_y += 5

    def fill_warehouse(self):
        self.fill_field_in_warehouse(49, 48) # hardcoded, wystarczy podać jakiś punkt wewnątrz magazynu
        self.count_free_space()

    def fill_field_in_warehouse(self, x, y):
        if x > 99 or y > 99 or x < 0 or y < 0 or self.matrix[x][y] == WALL \
                or self.matrix[x][y] == FREE_SPACE or self.matrix[x][y] == ENTRANCE:
            return
        elif self.matrix[x][y] == OUT_OF_BOUNDS:
            self.matrix[x][y] = FREE_SPACE

        self.fill_field_in_warehouse(x-1, y)
        self.fill_field_in_warehouse(x + 1, y)
        self.fill_field_in_warehouse(x, y+1)
        self.fill_field_in_warehouse(x, y-1)

    def count_free_space(self):
        for x in range(self.HEIGHT):
            y = 0
            while y < self.WIDTH:
                if self.matrix[x][y] == FREE_SPACE:
                    self.free_space_counter += 1
                y += 1

    def debug_warehouse_shape(self):
        print(" ")
        print("Rozmiar magazynu - : " + str(self.free_space_counter))
        # for x in range(self.HEIGHT):
        #     y = 0
        #     while y < self.WIDTH:
        #         if self.matrix[x][y] == FREE_SPACE:
        #             print("O", end='')
        #
        #         elif self.matrix[x][y] == ENTRANCE:
        #             print("-", end='')
        #
        #         elif self.matrix[x][y] > 0:
        #             print("X", end='')
        #         else:
        #             print(" ", end='')
        #         y += 1
        #     print("")

    @staticmethod
    def count_posible_coverage():
        count = 0
        for cargo_type in CARGO_LIST:
                for _ in range(cargo_type.THIS_TYPE_NUMBER):
                    count += cargo_type.height * cargo_type.width

        return count

    @staticmethod
    def count_number_of_cargos():
        count = 0
        for cargo_type in CARGO_LIST:
            count += cargo_type.THIS_TYPE_NUMBER

        return count