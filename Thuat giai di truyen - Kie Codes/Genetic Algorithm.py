from functools import partial
from random import choices, randint, randrange, random
from typing import List, NamedTuple, Optional, Callable, Tuple
from collections import namedtuple

Genome = List[int]
Population = List[Genome]
PopulateFunc = Callable[[], Population] 
FitnessFunc = Callable[[Genome], int]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
# PrinterFunc = 

Thing = namedtuple('Thing', ['name', 'value', 'weight'])

list_items = [
    Thing('Laptop', 500, 2200),
    Thing('Airport', 80, 100),
    Thing('Booknote', 10, 500),
    Thing('Hat', 20, 200),
    Thing('Water Bottle', 30, 192)
]

list_items2 = [
    Thing('Laptop', 500, 2200),
    Thing('Headphones', 150, 160),
    Thing('Coffee Mug', 60, 350),
    Thing('Notepad', 40, 333),
    Thing('Water Bottle', 30, 192),
]

def generate_genome(len_gen: int) -> Genome:
    return [randint(0,1) for i in range(len_gen)]
    # return choices([0,1], k= len_gen)

def generate_population(size: int, len_gen: int) -> Population:
    return [generate_genome(len_gen) for _ in range(size)]

def fitness(genome: Genome,things: Thing, weight_limit: int) -> int:
    value, weight = 0, 0
    for i, v in enumerate(things):
        if genome[i] == 1:
            value += v.value
            weight += v.weight
            
            if weight > weight_limit:
                return 0
    
    return value

def single_point_crossover(g1: Genome, g2: Genome) -> Tuple[Genome, Genome]:
    len_g = len(g1)
    if len_g <2:
        return g1, g2

    p = randint(1, len_g+1)
    return g1[:p] + g2[p:], g2[:p] + g1[p:]

def mutation(a: Genome, num: int = 1, probability: float =0.5) -> Genome:
    idx = randint(0,len(a) - 1)
    a[idx] = a[idx] if random() > probability else abs(a[idx] - 1)
    return a
    # for _ in range(num):
    #     idx = randrange(len(a))
    #     a[idx] = a[idx] if radom() > probability else abs(a[idx] - 1)

# def population_fitness(population: Population, fitness_func: FitnessFunc) -> int:
#     return  sum([fitness_func(genome) for genome in population])

# def selection_pair(population: Population, fitness_func: FitnessFunc) -> Tuple(Genome, Genome):
def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k = 2
    )

def sort_population(population: Population, fitness_func: FitnessFunc) -> Population:
    return sorted(population, key=fitness_func, reverse=True)

def run_evolution(
    populate_func: PopulateFunc,
    fitness_func: FitnessFunc,
    fitness_limit: int,
    selection_fun: SelectionFunc = selection_pair,
    crossover_func: CrossoverFunc = single_point_crossover,
    mutation_func: MutationFunc = mutation,
    generation_limit: int = 100
) ->Tuple[Population, int]:
    population = populate_func()
    
    population = sorted(population, key= lambda genome: fitness_func(genome), reverse=True)

    for i in range(generation_limit):
        if fitness_func(population[0]) >= fitness_limit:
            break

        next_generation = population[:2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_fun(population, fitness_func)
            child1, child2 = crossover_func(parents[0], parents[1])
            child1 = mutation_func(child1)
            child2 = mutation_func(child2)

            next_generation += [child1, child2]
        
        population = next_generation
        population = sorted(population, key= lambda genome: fitness_func(genome), reverse=True)


    return population, i

document = """
def generate_genome:
    pass # create ma gen

def generate_population:
    pass # create quan the

def single_point_crossover:
    pass # sinh san don diem

def mutation:
    pass # dot bien don diem

def fitness:
    pass # ham thich nghi

def population_fitness:
    pass # danh gia diem quan the

def selection_pair:
    pass # lua chon cap bo me co to chat tot (do thich nghi cao)

def sort_population:
    pass # sap xep cac phan tu trong population

def run_evolution:
    pass # run giai thuat tu viec thiet lap quan the danh gia 
# mo hinh, lua chon cap bo me, sinh san , dot bien va lap cho 
# toi khi tim duoc diem mong muon
"""

population, generations = run_evolution(
    populate_func=partial(generate_population, size=10, len_gen=len(list_items)),
    fitness_func=partial(fitness, things = list_items, weight_limit=3000),
    fitness_limit=1310,
    generation_limit=100
)

print(f'so the he: {generations}')
print("-"*20)
print(f'Quan the  {population}')
print("-"*20)
result = []
for i, v in enumerate(list_items):
    if population[0][i] == 1:
        result.append(v.name)

print(f'best solution: {result}')


val = fitness(population[0],list_items,weight_limit=3000)
print('='*20)
print(f'value fitness: {val}')
