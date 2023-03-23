lis = []

def indexes(n):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] + n[j]==target:
                if n[i] not in lis and n[j] not in lis:
                    lis.append(i)
                    lis.append(j)
    if lis:
            print(lis)
    else:
            print(None)
nums = list(map(int, input("Enter a list of integers: ").split()))
target = (int(input("Enter a target: " )))

indexes(nums)