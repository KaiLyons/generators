import random
def evnt():
    return random.choice(["beats", "kills", "has sex with", "shoots", "fires at", "eats"])
def obj1():
    return random.choice(["horse", "child", "clown", "egg", "storm", "movie star", "kindergarden", "store", "daycare"])
def obj2():
    return random.choice(["horse", "child", "clown", "egg", "storm", "movie star", "kindergarden", "store", "daycare"])
def wa():
    return random.choice(["with", "as", "near"])

def finalprod():
    print("Florida man", evnt(), obj1(), wa(), obj2())
finalprod()
