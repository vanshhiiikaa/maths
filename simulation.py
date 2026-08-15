#Simulation
import random

heads = 0
tails = 0
for i in range (1000):
    result = random.choice(["Head", "Tail"])
    if result == "Head" :
        heads += 1
    else : 
        tails += 1
print(heads)
print(tails)