import Cargo
import copy
import warehouse


class Individual:

    coverage = 0
    matrix = None # kazdy osobnik ma deep copy matrixa populacji
    cargoList = None

    def __init__(self, matrix, free_space_size) -> None:
        super().__init__()
        self.matrix = copy.deepcopy(matrix)
        self.cargoList = []

    def initialize_cargo_list_with_random_positions(self, cargo_type_list):
        id = 0
        for cargo_type in cargo_type_list:
                for _ in range(cargo_type.THIS_TYPE_NUMBER):
                    cargo = Cargo.Cargo(cargo_type, id)
                    cargo.randomize_position_of_left_corner()
                    self.cargoList.append(cargo)

        self.place_cargo_list_in_warehouse()
        self.calculate_coverage()

    def place_cargo_list_in_warehouse(self):
        for cargo in self.cargoList:
            if self.cargo_can_be_placed(cargo) is True:
                cargo.inWarehouse = True
                self.put_cargo_in_matrix(self.matrix, cargo)

    def cargo_can_be_placed(self, cargo):
        for i in range(0, cargo.height):
            for j in range(0, cargo.width):
                if self.matrix[cargo.position.index_x + i][cargo.position.index_y +j] != warehouse.FREE_SPACE:
                    return False

        copied_matrix = copy.deepcopy(self.matrix)

        self.put_cargo_in_matrix(copied_matrix, cargo)

        return self.path_exists(copied_matrix, cargo)

    def path_exists(self, temporary_matrix, cargo):

        for i in range(cargo.height):

            if self.check_if_enterance(temporary_matrix, cargo.position.index_x + i, cargo.position.index_y - 1) is True:
                return True

            if self.check_if_enterance(temporary_matrix, cargo.position.index_x + i, cargo.position.index_y + cargo.width) is True:
                return True

        for j in range(cargo.width):

            if self.check_if_enterance(temporary_matrix, cargo.position.index_x - 1, cargo.position.index_y + j) is True:
                return True

            if self.check_if_enterance(temporary_matrix, cargo.position.index_x + cargo.height, cargo.position.index_y + j) is True:
                return True

        return False

    def check_if_enterance(self, temporary_matrix, x, y):
        if temporary_matrix[x][y] == warehouse.ENTRANCE:
            return True
        elif temporary_matrix[x][y] == warehouse.FREE_SPACE:
            temporary_matrix[x][y] = warehouse.ALREADY_CHECKED
            return self.check_if_enterance(temporary_matrix, x+1, y) or self.check_if_enterance(temporary_matrix, x-1 , y) or \
                   self.check_if_enterance(temporary_matrix, x, y+1) or self.check_if_enterance(temporary_matrix, x, y-1)
        else:
            return False

    def put_cargo_in_matrix(self, matrix, cargo):
        for i in range(0, cargo.height):
            for j in range(0, cargo.width):
                matrix[cargo.position.index_x + i][cargo.position.index_y + j] = warehouse.CARGO

    def calculate_coverage(self):
        self.coverage = 0
        for x in range(100):
            for y in range(100):
                if self.matrix[x][y] == warehouse.CARGO:
                    self.coverage += 1
