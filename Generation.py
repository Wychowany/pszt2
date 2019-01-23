import Individual
import warehouse
import copy

NUMBER_OF_INDIVIDUALS = 100


class Generation:

    individuals = None
    number_of_generation = 1
    the_best_individual = None
    matrix = None # kopia matrixa z magazynu
    free_space_size = None

    def __init__(self) -> None:
        super().__init__()

    def setup_matrix_and_initialize_positions_of_individuals(self, matrix, free_space_size):
        self.matrix = matrix
        self.free_space_size = free_space_size
        self.individuals = []
        for _ in range(int(NUMBER_OF_INDIVIDUALS)):
            matrix = (copy.deepcopy(self.matrix))
            self.individuals.append(Individual.Individual(matrix, self.free_space_size))

        for individual in self.individuals:
            individual.initialize_cargo_list_with_random_positions(warehouse.CARGO_LIST)

    def introduce_new_individuals(self):
        for i in range(0, int(NUMBER_OF_INDIVIDUALS/2)):
            k = int(NUMBER_OF_INDIVIDUALS/2) + i
            self.individuals[k] = Individual.Individual(copy.copy(self.matrix), self.free_space_size)
            self.individuals[k].initialize_cargo_list_with_random_positions(warehouse.CARGO_LIST)

    def sort_population_by_coverage(self):
        self.individuals.sort(key=lambda ind: ind.coverage, reverse=True)

    def print_all_coverages(self):
        print("\n " + str(self.number_of_generation) + " generacja, pokrycia: ")
        for ind in self.individuals:
            print(ind.coverage, end=' ')

        self.number_of_generation += 1

    def get_the_best_matrix(self):
        return copy.copy(self.individuals[0].matrix)