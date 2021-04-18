money = 300
item = (("みかん",100),("apple",200),("grape"),3000)

n = len(item)

for i in range(2**n):
    bag = []
    for j in range(n):
        if((i>>j)&1):
            bag.append(item[j][0])

    print(bag)

