# Solution-1 (Using 3rd variable)

x = 13
y = 20

temp = x

x = y

y = temp

print("X :", x)
print("Y :", y)

# solution -2 (without using 3rd variable)

x = 100
y = 200

x , y = y , x

print("X :", x)
print("Y :", y)