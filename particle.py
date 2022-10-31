import random

class Particle:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0

    def moveup(self):
        self.y += 1
    def moveright(self):
        self.x += 1
    def movedown(self):
        self.y -= 1
    def moveleft(self):
        self.x -= 1

    def display(self):
        print("X-Coordinate of", self.name, "=", self.x)
        print("Y-Coordinate of", self.name, "=", self.y)   



if __name__ == "__main__":

    options = {0: moveup(), 1: moveright(), 2: movedown(), 3: moveleft()}

    particles = ["alpha, beta, delta"]
    for index in range(len(particles)):

        particles[index] = Particle(particles[index])

        numOfMoves = random.randint(0, 11)
        for i in range(numOfMoves):
            movement = random.randint(0, 5)

            particles[index].Particle(options[movement])()