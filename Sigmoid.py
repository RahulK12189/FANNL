import numpy as np
import matplotlib.pyplot as plt

def showGraph():

    x = np.linspace(-10,10,100)
    
    y= 1/(1+np.exp(-x))
    
    plt.style.use('seaborn')
    plt.title("Sigmoid")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.scatter(x,y,c='r')
    plt.plot(x,y)
    plt.show()

showGraph()
    
