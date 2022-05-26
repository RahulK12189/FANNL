import numpy as np


def activation_function(sum):
        if sum>=0:
                return 1
        else:
                return 0

def and_function(x):
        wt = np.array([1,1])
        bais = -1.5
        sum = np.dot(x,wt) + bais
        return activation_function(sum)


def or_function(x):
        wt = np.array([1,1])
        bais = -0.5
        sum = np.dot(x,wt) + bais
        return activation_function(sum)







input1 = np.array([0,0])
input2 = np.array([0,1])
input3 = np.array([1,0])
input4 = np.array([1,1])

print("\nOR\n")
print(input1," :-\t ",or_function(input1))
print(input2," :-\t ",or_function(input2))
print(input3," :-\t ",or_function(input3))
print(input4," :-\t ",or_function(input4))


print("\nAND\n")
print(input1," :-\t ",and_function(input1))
print(input2," :-\t ",and_function(input2))
print(input3," :-\t ",and_function(input3))
print(input4," :-\t ",and_function(input4))
