import random

for i in range(3):
    print(random.random())
    print(random.randint(10,20))

# randomly picking an item from a list
    members = ['John', 'Mary', 'Bob','Josh']
    leader = random.choice(members)
    print(leader)


