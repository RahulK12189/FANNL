import numpy as np
import matplotlib.pyplot as plt

lst=[]

def showGraph():

    x = np.linspace(-10,10,100)

    for i in x:
        if i>0:
            lst.append(i)
        else:
            lst.append(0)

    
    plt.style.use('seaborn')
    plt.title("Rectified Linear Unit")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.scatter(x,lst,c='r')
    plt.plot(x,lst)
    plt.show()

showGraph()
    
