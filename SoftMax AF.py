import numpy as np
import matplotlib.pyplot as plt

def showGraph():
    x = np.linspace(-10,10,50)
    y = np.exp(x)/np.sum(np.exp(x))
    
    plt.style.use('seaborn')
    plt.title("Softmax Activation Function")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(x,y,c='r')
    plt.plot(x,y)
    plt.show()


showGraph()
