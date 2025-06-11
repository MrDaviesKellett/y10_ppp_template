# testing
# testing the test
# does this auto commit? or not?

# more changes
# save with HK Tz commit mssg?

# another change!

class Dog:
    def __init__(self,name,size):
        self.name = name
        self.size = size
dogs = {}
names = ["rex","joey"]

from random import choice, randint

for i in range(10):
    name = choice(names)
    if name not in dogs:
        dogs[name] = Dog(name,randint(1,10))
    else:
        print("dog already exists")

dogs["rex"].attack("claws")

