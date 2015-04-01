#Author: Anthony Val C. Camposano
#Date   : 12/10/2014
# Unsigned and 2's complement encoding


def B2U(x):
    w = len(x)
    value = 0
    for i in range(1,w+1):
        value = value + int(x[i-1])*(2**(len(x)-i))
    return value

def B2T(x):
    w = len(x)
    value = -(int(x[0])*(2**(w-1)))
    for i in range(1,w):
        value = value + int(x[i])*(2**(len(x)-1-i))
    return value

def T2U(w,x):
    if (x < 0):
        return (x+2**w)
    else:
        return (x)

def U2T(w,x):
    if (x < 2**(w-1)):
        return x
    else:
        return (x - 2**w)
    
def truncate(k,x):
    value = 0
    for i in range(1,k+1):
        value = value + int(x[i-1])*(2**(len(x)-i))
    return value


def decimalToBit(w,x):
    b = []
    #Decimal to bit for unsigned numbers
    if x >=0:
        for i in range(1,w+1):
            b.append(x%2)
            x = int(x/2)
        b.reverse()
        bit = ''
        for i in b:
            bit = bit + str(i)
    #Decimal to bit for signed numbers
    else:
        bit = twoscomplement(decimalToBit(w,abs(x)))
    return bit


    
def twoscomplement(x):
    y = ''
    w = ''
    for i in x:
        if (i == '0'):
            y=y+'1'
        else:
            y=y+'0'
            
    for j in range(1,len(x)):
        w +='0'
        
    return bitAddition(y,w+'1')

def bitAddition(x,y):
    s = []
    carry = 0
    for i in range(len(x)-1,-1,-1):
        a,b = x[i],y[i]
        sum1 = int(a) +int(b) + carry
        carry=0
        if (sum1 == 0):
            s.append('0')
        elif (sum1 == 1):
            s.append('1')
        else:
            s.append('0')
            carry = 1

    s.reverse()
    s1=''   
    for i in s:
        s1+=str(i) 
    return s1  
            
##    
##def hexToDecimal(x):
##    hexlist='0123456789abcdef'
##    
##        
            
        
        
            
    
    
