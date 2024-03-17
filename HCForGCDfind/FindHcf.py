# Find HCF or GCD 

# HCF = Highest Common Factor 

def findhcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x%i == 0) and (y%i==0)):
            hcf = i
          
    return hcf

x = int(input('enter first number here:'))                
y = int(input('enter first second here:'))

print('the hcf of the given two numbers is ', findhcf(x,y))