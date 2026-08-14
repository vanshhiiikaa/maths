#Probability

import random
result = random.choice(["Head", "Tail"])
print(result)


count = 0
for i in range(100):
    if random.choice (["Head, Tail"]) == "Head":
        count += 1

print(count)