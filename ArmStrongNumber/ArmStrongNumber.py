# Solution (Find an armstrong number)

num = int(input('enter a number here :'))
order = len(str(num))
sum = 0

temp = num

while temp > 0:
    digit = temp % 10
    cube = digit ** order
    sum = sum + cube
    temp //=10

if sum == num:
    print('it is an armstrong number')
else:
    print('it is not an armstrong number')        