import random

health = 50
difficulty = 3
# 1 = Easy Mode | 2 = Normal Mode | 3 = Hard Mode
health_potion = int(random.randint(25,50)/difficulty)
health += health_potion
print(health)