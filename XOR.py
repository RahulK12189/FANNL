import numpy as np

def activation_function(sum):
    if sum>=0:
        return 1
    else:
        return 0

def and_function(x):
    wt = np.array([1,1])
    bias = -1.5
    sum = np.dot(wt,x)+bias
    return activation_function(sum)

def or_function(x):
    wt = np.array([1,1])
    bias = -0.5
    sum = np.dot(wt,x)+bias
    return activation_function(sum)

def not_function(x):
    wt = -1
    bias = 0.5
    sum = x*wt + bias
    return activation_function(sum)

def xor_function(x):
    y1 = and_function(x)
    y2 = or_function(x)
    y3 = not_function(y1)
    ip = np.array([y2,y3])
    op = and_function(ip)
    return op
 

    


input1= np.array([0,0])
input2= np.array([0,1])
input3= np.array([1,0])
input4= np.array([1,1])



print("\tAND\n")
print(input1," : - ",and_function(input1))
print(input2," : - ",and_function(input2))
print(input3," : - ",and_function(input3))
print(input4," : - ",and_function(input4))

print("\tOR\n")
print(input1," : - ",or_function(input1))
print(input2," : - ",or_function(input2))
print(input3," : - ",or_function(input3))
print(input4," : - ",or_function(input4))


print("\tXOR\n")
print(input1," : - ",xor_function(input1))
print(input2," : - ",xor_function(input2))
print(input3," : - ",xor_function(input3))
print(input4," : - ",xor_function(input4))
