# 1st solution (Using for loop)

num = int(input('Enter your factoria number here:'))

factorial = 1

if num < 0:
    print('factorial of less then 0 dose not exist')

if num == 0:
    print('factorial of 0 is ',1)    

if num > 0:
    for i in range(1,num+1):
       factorial = factorial*i
    print(num,'! =', factorial) 

   

# 2nd solution (Using Recursion)
    
def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))
    
num = int(input('Enter a number here:'))
result = fact(num)

print('the factorial number is ', result)
