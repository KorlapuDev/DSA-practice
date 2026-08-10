x = [2, 5, 1, 3, 0]

temp = x[0]

for i in range(1, len(x)-1):
    if(x[i]>temp):
        temp = x[i]

print(temp)