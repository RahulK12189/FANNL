import numpy as np
import matplotlib.pyplot as plt

def compute(x,y):
    n = np.size(x)

    xmean = np.mean(x)
    
    ymean = np.mean(y)

    sxy = np.sum(x*y)-n*xmean*ymean
    sxx = np.sum(x*x)-n*xmean*xmean

    b0 = sxy/sxx
    b1 = ymean-b0*xmean

    return [b0,b1]

def draw(x,y,b):
    plt.scatter(x,y)
    op = b[0] + b[1]*x
    plt.plot(x,op)
    plt.show()

x = np.array([0,1,2,3,4,5,6])
y = np.array([1,2,3,4,5,6,7])

b = compute(x,y)

print("b[0] ; ",b[0])
print("b[1] : ",b[1])

draw(x,y,b)
