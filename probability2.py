import random
balls = ['R', 'R', 'R', 'B', 'B']

#Probability of picking first ball
first = random.choice(balls)
balls.remove(first)

#Probability of picking second ball
second = random.choice(balls)
balls.remove(second)

#Probability of picking third ball
third = random.choice(balls)
balls.remove(third)

print("First:",first)
print("Second:",second)
print("Third:",third)
print(balls)