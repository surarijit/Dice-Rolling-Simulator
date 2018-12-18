import random
a= 1
while 1:
    print(random.randrange(1,7,1))
    print('do u want to continue, press 1 for yes and 0 for no ')
    a = int(input())
    if a == 0:
        break
