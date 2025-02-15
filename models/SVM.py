from sklearn.svm import SVC
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn import metrics
import mysql.connector
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_score
from DBconn import DBConnection
# from sklearn.metrics import plot_confusion_matrix
# import matplotlib.pyplot as plt
def classify_svm(x_train, x_test, y_train, y_test):
    mydb = DBConnection.getConnection()
    cursor = mydb.cursor()
    classify = SVC()
    classify.fit(x_train, y_train)
    predicted = classify.predict(x_test)
    query = "INSERT INTO  performance  VALUES (%s,%s,%s,%s,%s)"

    svc = metrics.accuracy_score(y_test, predicted) * 100
    print("The accuracy score using the SVM is ->")
    print(metrics.accuracy_score(y_test, predicted))

    precision = metrics.precision_score(y_test, predicted, average='macro', pos_label='1')
    print("Precision score of SVM IS ->")
    print(metrics.precision_score(y_test, predicted, average='micro', pos_label='1'))

    recall = metrics.recall_score(y_test, predicted, average='macro', pos_label='1')
    print("Recall score of SVM  IS ->")
    print(metrics.recall_score(y_test, predicted, average='micro', pos_label='1'))

    f1_score = metrics.f1_score(y_test, predicted, average='macro', pos_label='1')
    print("F1 score of SVM IS ->")
    print(metrics.f1_score(y_test, predicted, average='micro', pos_label='1'))



    val = ("SVM", str(svc), str(precision), str(recall), str(f1_score))
    cursor.execute(query, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return svc