#IEEE Floating Point representation
""" IEEE floating-point standard represents a number in a form
    V = (-1)**s x M x 2**E
"""


b = input("Enter the Bit representation:")
bit = b.split(' ')

# convert the bit representation to its decimal representation
def bitToDecimal(b):
    sum1=0
    j=0
    for i in b:
        n = len(b)
        j=j+1
        sum1=sum1+(int(i)*(2**(n-j)))
    return sum1


# For nonnegative values s = 0
""" Bit representation of a floating-point number is divided into
3 fields to encode the values. The sum(p)-bit floating point format
contains the values s, k, and n"""

# In this case: 8-bit floating format consist of s=1, k=4, n=3
p = 1,4,3
bias = (2**(4-1)-1)

# Calculation of the decimal value of the k-bit exponent and n-bit fraction field
e=bitToDecimal(bit[1])
f=bitToDecimal(bit[2])/(2**p[2])

# Summation of the exponent field
sum2=0
for i in bit[1]:
    sum2 = sum2 + int(i)
    
    
"""The value encoded by a given bit representation can be divided
into 3 different cases depending on the value of the exponent (k)"""


#Case 1: Special Cases
if sum2 == p[1]:
    V="Infinity"
#Case 2: Denormalized values
elif sum2 == 0:
    E = 1 - bias
    M = f
    V = (2**E)*M
#Case 3: Normalized values
else:
    E = e - bias
    M = 1 + f
    V=(2**E)*M

print(V)

    









    


    
