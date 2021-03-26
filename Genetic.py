import numpy as np
import time
import random

seed = time.time()
random.seed(seed)

class population:
    """Defines the population"""
    def __init__(self):
        self.generation = 0
        self.gen1 = []
        self.gen2 = []
        self.gen3 = []
        self.gen4 = []
        self.gen5 = []
        self.gen6 = []
        self.gen7 = []
        self.gen8 = []

    def initializePop(self):
        self.generation =+ 1
        for x in range(256):
            subject = individual()
            for y in range(8):
                if random.random() >= 0.51:
                    subject.genes[y] = True
            self.gen1.append(subject)

    def assignFit(self, gen):
        if gen == 1:
            for x in range(len(self.gen1)):
                self.gen1[x].fitness = 0
                for y in range(8):
                    if self.gen1[x].genes[y] == True:
                        self.gen1[x].fitness = 1 + self.gen1[x].fitness
                self.gen1[x].odds = (0.125 * self.gen1[x].fitness)

        if gen == 2:
            for x in range(len(self.gen2)):
                self.gen2[x].fitness = 0
                for y in range(8):
                    if self.gen2[x].genes[y] == True:
                        self.gen2[x].fitness = 1 + self.gen2[x].fitness
                self.gen2[x].odds = (0.125 * self.gen2[x].fitness)

        if gen == 3:
            for x in range(len(self.gen3)):
                self.gen3[x].fitness = 0
                for y in range(8):
                    if self.gen3[x].genes[y] == True:
                        self.gen3[x].fitness = 1 + self.gen3[x].fitness
                self.gen3[x].odds = (0.125 * self.gen3[x].fitness)

        if gen == 4:
            for x in range(len(self.gen4)):
                self.gen4[x].fitness = 0
                for y in range(8):
                    if self.gen4[x].genes[y] == True:
                        self.gen4[x].fitness = 1 + self.gen4[x].fitness
                self.gen4[x].odds = (0.125 * self.gen4[x].fitness)

        if gen == 5:
            for x in range(len(self.gen5)):
                self.gen5[x].fitness = 0
                for y in range(8):
                    if self.gen5[x].genes[y] == True:
                        self.gen5[x].fitness = 1 + self.gen5[x].fitness
                self.gen5[x].odds = (0.125 * self.gen5[x].fitness)

        if gen == 6:
            for x in range(len(self.gen6)):
                self.gen6[x].fitness = 0
                for y in range(8):
                    if self.gen6[x].genes[y] == True:
                        self.gen6[x].fitness = 1 + self.gen6[x].fitness
                self.gen6[x].odds = (0.125 * self.gen6[x].fitness)

        if gen == 7:
            for x in range(len(self.gen7)):
                self.gen7[x].fitness = 0
                for y in range(8):
                    if self.gen7[x].genes[y] == True:
                        self.gen7[x].fitness = 1 + self.gen7[x].fitness
                self.gen7[x].odds = (0.125 * self.gen7[x].fitness)

        if gen == 8:
            for x in range(len(self.gen8)):
                self.gen8[x].fitness = 0
                for y in range(8):
                    if self.gen8[x].genes[y] == True:
                        self.gen8[x].fitness = 1 + self.gen8[x].fitness
                self.gen8[x].odds = (0.125 * self.gen8[x].fitness)

    def roulette(self, gen):
        candidates = {}
        winners = []
        for x in range(len(gen)):
            candidates[x] = gen[x].odds

        for x in range(int(len(gen)/2)):
            winner = pop(candidates)
            winners.append(gen[winner])
            candidates.pop(winner)
        return winners

    def mix(self, gen):
        tam = len(gen)
        mid = tam/2


        for x in range(int(mid)):
            son1 = individual()
            son2 = individual()

            for y in range(4):
                son1.genes[0 + y] = gen[x].genes[0 + y]
                son1.genes[4 + y] = gen[(tam-1) - x].genes[4 + y]
            for y in range(4):
                son2.genes[0 + y] = gen[(tam - 1) - x].genes[0 + y]
                son2.genes[4 + y] = gen[x].genes[4 + y]

            gen[(tam - 1) - x] = son1
            gen[x] = son2
        return gen


    def mutate(self, gen):

        for item in gen:
            if random.random() > 0.4:
                mutation1 = random.randrange(7)
                mutation2 = random.randrange(7)
                if not item.genes[mutation1]:
                    item.genes[mutation1] = True
                if not item.genes[mutation2]:
                    item.genes[mutation2] = True
        return gen


def pop(candidates):
    max = sum(candidates.values())
    pick = random.uniform(0, max)
    current = 0
    for key, value in candidates.items():
        current += value
        if current > pick:
            return key



class individual:
    """Defines each individual of the population"""
    def __init__(self):
        self.genes = np.array([False, False, False, False, False, False, False, False])
        self.fitness = 0
        self.odds = 0

    def calculateFit(self):
        x = 0
        for item in self.genes:
            if item == True:
                self.fitness =+ 1


sociedad = population()
sociedad.initializePop()
sociedad.gen1 = sociedad.mutate(sociedad.gen1)
sociedad.assignFit(1)

sociedad.gen2 = sociedad.roulette(sociedad.gen1)
sociedad.gen2 = sociedad.mix(sociedad.gen2)
sociedad.gen2 = sociedad.mutate(sociedad.gen2)
sociedad.assignFit(2)

sociedad.gen3 = sociedad.roulette(sociedad.gen2)
sociedad.gen3 = sociedad.mix(sociedad.gen3)
sociedad.gen3 = sociedad.mutate(sociedad.gen3)
sociedad.assignFit(3)

sociedad.gen4 = sociedad.roulette(sociedad.gen3)
sociedad.gen4 = sociedad.mix(sociedad.gen4)
sociedad.gen4 = sociedad.mutate(sociedad.gen4)
sociedad.assignFit(4)

sociedad.gen5 = sociedad.roulette(sociedad.gen4)
sociedad.gen5 = sociedad.mix(sociedad.gen5)
sociedad.gen5 = sociedad.mutate(sociedad.gen5)
sociedad.assignFit(5)

sociedad.gen6 = sociedad.roulette(sociedad.gen5)
sociedad.gen6 = sociedad.mix(sociedad.gen6)
sociedad.gen6 = sociedad.mutate(sociedad.gen6)
sociedad.assignFit(6)

sociedad.gen7 = sociedad.roulette(sociedad.gen6)
sociedad.gen7 = sociedad.mix(sociedad.gen7)
sociedad.gen7 = sociedad.mutate(sociedad.gen7)
sociedad.assignFit(7)

sociedad.gen8 = sociedad.roulette(sociedad.gen7)
sociedad.gen8 = sociedad.mix(sociedad.gen8)
sociedad.gen8 = sociedad.mutate(sociedad.gen8)
sociedad.assignFit(8)

gigachad = []

gigachad = sociedad.roulette(sociedad.gen8)


print("Population:")
for item in sociedad.gen1:
    print(item.genes)

print("Gigachad:")

for item in gigachad:
    print(item.genes)

