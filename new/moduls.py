import random

def generation_id(count):
    rnd_id = 0
    for i in range(count):
        rnd_id = str(random.randint(1,100)) + str(rnd_id)
    return rnd_id



def greet(name):
    print(f"Hey, {name}")


def generetion_name(list):
    name = random.choice(list)
    return name
