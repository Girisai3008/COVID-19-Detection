
from graphs import view
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import warnings
import sys
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from SVM import classify_svm
from KNN import classify_knn
from _RFC import classify_rfc
from NAIVE_BAYES import classify_nb
from LOGREG import classify_lr
# from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt

def classfy():
    try:

        # Split the data into columns and read
        warnings.warn("Variables are collinear.")
        datainput = pd.read_csv("dataset\\covid_train.csv")
        # Set the outcome and delete it
        y = datainput['TEST_RESULT']
        del datainput['TEST_RESULT']
        # Split data into Test & Training set where test data is 30% & raining data is 70%
        x_train, x_test, y_train, y_test = train_test_split(datainput, y, test_size=0.2)
        svc_accuracy=classify_svm(x_train, x_test, y_train, y_test)
        knn_accuracy=classify_knn(x_train, x_test, y_train, y_test)
        rfc_accuracy = classify_rfc(x_train, x_test, y_train, y_test)
        nb_accuracy = classify_nb(x_train, x_test, y_train, y_test)
        lr_accuracy = classify_lr(x_train, x_test, y_train, y_test)

        list = []
        list.clear()
        list.append(svc_accuracy)
        list.append(knn_accuracy)
        list.append(rfc_accuracy)
        list.append(nb_accuracy)
        list.append(lr_accuracy)
        view(list)

    except Exception as e:
        print("Error=" + e.args[0])
        tb = sys.exc_info()[2]
        print("LINE NO: ", tb.tb_lineno)

# classfy()