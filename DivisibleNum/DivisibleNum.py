# Soltion-1 (Using for loop)

for i in range(1,100):
    if i % 13 == 0:
        print(i)



l = [39,26,48,98,33,67,91,87] 

result = list(filter(lambda x : x % 13 == 0,l))

print(result)