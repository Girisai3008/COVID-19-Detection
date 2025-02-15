import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import sys

def view(rlist):
    height=rlist
    bars = ('SVM','KNN','RANForest','GaussnNB','LogisticREG')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=[ 'yellow','red', 'green','blue','purple'])
    plt.xticks(y_pos, bars)
    plt.xlabel('Algorithms')
    plt.ylabel('Accuracy')
    plt.title('Prediction Accuracy Analysis')
    plt.show()
