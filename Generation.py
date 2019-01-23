import Individual
import warehouse
import copy
import random

NUMBER_OF_INDIVIDUALS = 100
MUTATION_CHANCE = 10

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

            # znajdzmy matke i ojca dla osobnika
            father_index = random.randrange(0, 50, 1)
            mother_index = random.randrange(0, 50, 1)

            while father_index == mother_index:
                mother_index = random.randrange(0, 50, 1)

            self.cross_mother_and_father(self.individuals[father_index], self.individuals[mother_index],
                                         self.individuals[k])

            self.individuals[k].calculate_coverage()
            #self.individuals[k].initialize_cargo_list_with_random_positions(warehouse.CARGO_LIST)
        self.mutate()


    def cross_mother_and_father(self, father_individual, mother_individual, individual):
        # print ("#########################################")
        # print ("FATHER: " + str(len(father_individual.cargoList)))
        # print ("MOTHER: " + str(len(mother_individual.cargoList)))
        # print ("#########################################")


        for i in range(warehouse.Warehouse.count_number_of_cargos()):
            placed = False
            if father_individual.cargoList[i].inWarehouse is True and mother_individual.cargoList[i].inWarehouse is False : ## staramy sie wlozyc ojca
                placed = individual.cargo_can_be_placed(copy.deepcopy(father_individual.cargoList[i]))
                if placed is True:
                    individual.cargoList.append(copy.deepcopy(father_individual.cargoList[i]))
                    individual.put_cargo_in_matrix(individual.matrix, individual.cargoList[i])
            elif father_individual.cargoList[i].inWarehouse is False and mother_individual.cargoList[i].inWarehouse is True: ## staramy sie wlozyc matke
                placed = individual.cargo_can_be_placed(copy.deepcopy(mother_individual.cargoList[i]))
                if placed is True:
                    individual.cargoList.append(copy.deepcopy(mother_individual.cargoList[i]))
                    individual.put_cargo_in_matrix(individual.matrix, individual.cargoList[i])

            if placed is False:
                carg = copy.deepcopy(father_individual.cargoList[i])
                carg.randomize_position_of_left_corner()
                carg.inWarehouse = False
                individual.cargoList.append(carg)
                if individual.cargo_can_be_placed(carg):
                    individual.put_cargo_in_matrix(individual.matrix, individual.cargoList[i])
                    carg.inWarehouse = True

    def mutate(self):
        for i in range(MUTATION_CHANCE):
            a = random.randrange(0, 100, 1)
            self.individuals[a].initialize_cargo_list_with_random_positions(warehouse.CARGO_LIST)


    def sort_population_by_coverage(self):
        self.individuals.sort(key=lambda ind: ind.coverage, reverse=True)

    def print_all_coverages(self):
        print("\n " + str(self.number_of_generation) + " generacja, pokrycia: ")
        for ind in self.individuals:
            print(ind.coverage, end=' ')

        self.number_of_generation += 1

    def get_the_best_matrix(self):
        return copy.copy(self.individuals[0].matrix)