duble = []
def func(n):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] == n[j]:
                if  n[i] not in duble:
                    duble.append(n[i])
    if duble:
        print(duble)
    else:
        print("None")

lis1 = [5, 1, 2, 1, 4,]
lis2= [4, 1, 2]
lis3= []
lis4= [6, 2, 5, 2, 6, 2]
lis5= [42, 42, 42, 42]

#func(lis1)
#func(lis2)
#func(lis3)
#func(lis4)
#func(lis5)
