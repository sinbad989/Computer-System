def bitToDecimal(b):
    sum1=0
    j=0
    for i in b:
        n = len(b)
        j=j+1
        sum1=sum1+(int(i)*(2**(n-j)))
    return sum1

x1 = ['000','001','010','011','100','101','110','111']
x2 = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']

##x1 = ['00','01','10','11']

# Create all the possible combination of 5-bit 0 and 1.
x = []
for j in x2:
    for i in x1:
       x.append('0'+' '+j+' '+i) 

def IEEEfloating(x):
    p = 1,8,23
    bias = (2**(p[1]-1)-1)
    v=[]
    for i in x:
        bit = i.split(' ')
        e=bitToDecimal(bit[1])
        f=bitToDecimal(bit[2])/(2**p[2])

        sum2=0
        for i in bit[1]:
            sum2 = sum2 + int(i)

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
            
        v.append(V)
    return(v)
        


