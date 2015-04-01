


x = input("Enter the binary number:")
b=x.split('.')

sum1 = 0
i = 0
for j in b[0]:
    m=len(b[0])
    i = i+1
    sum1 = sum1+(int(j)*(2**(m-i)))

sum2=0.0
i=0
for j in b[1]:
    n = len(b[1])
    i=i+1
    sum2=(sum2)+int(j)*(2**(-i))


total = sum1 + sum2

print(total)
