# Solution-1 ( Using for loop)

num = int(input('Enter a number:'))

for i in range(1,11):
    print(num, 'x' , i , '=' , num*i)


# Solution-2 (Using While Loop)
num2 =  int(input('Enter a number**:'))   
i = 1
while i <= 10:
    print(num2, 'x' , i , '=' , num2*i)
    i+=1
