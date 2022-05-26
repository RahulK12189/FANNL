import numpy as np

def activation_function(sum):
        if sum>=0:
                return 1
        else:
                return 0

def not_function(x):
        wt = -1
        bais = 0.5
        sum = (x*wt) + bais
        return activation_function(sum)




input1 = 0
input2 = 1
print("\nXOR\n")
print(input1," :-\t ",not_function(input1))
print(input2," :-\t ",not_function(input2))
