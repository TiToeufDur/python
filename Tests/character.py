import random 
def ran(a=False,b=False):
    if a == True:
        return random.randint(0,90)
    elif b == True:
        return random.randint(0,1)

age = ran(1)
chance = ran(0,1)
print(chance)
while age >= 50:
    if chance == 1:
        age = ran(True)
        chance = ran(0,True)
    else:
        break
print(age)
