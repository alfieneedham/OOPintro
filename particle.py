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

    particles = ["alpha", "beta", "delta", "gamma", "orange", "table", "computerisation"]

    for index in range(len(particles)):

        particles[index] = Particle(particles[index])

        numOfMoves = random.randint(10, 101)
        for i in range(numOfMoves):
            movement = random.randint(0, 4)

            if movement == 0:
                particles[index].moveup()
            if movement == 1:
                particles[index].moveright()
            if movement == 2:
                particles[index].movedown()
            if movement == 3:
                particles[index].moveleft()
        
        particles[index].display()
        print("")