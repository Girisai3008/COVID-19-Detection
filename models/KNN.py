from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import mysql.connector
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_score
from DBconn import DBConnection
# from sklearn.metrics import plot_confusion_matrix
# import matplotlib.pyplot as plt
def classify_knn(x_train, x_test, y_train, y_test):
    mydb = DBConnection.getConnection()
    cursor = mydb.cursor()
    classify1 = KNeighborsClassifier()
    classify1.fit(x_train, y_train)
    predicted1 = classify1.predict(x_test)
    query = "INSERT INTO  performance  VALUES (%s,%s,%s,%s,%s)"

    knn = metrics.accuracy_score(y_test, predicted1) * 100
    print("The accuracy score using the KNN is ->")
    print(metrics.accuracy_score(y_test, predicted1))

    precision = metrics.precision_score(y_test, predicted1, average='macro', pos_label='1')
    print("Precision score of KNN IS ->")
    print(metrics.precision_score(y_test, predicted1, average='micro', pos_label='1'))

    recall = metrics.recall_score(y_test, predicted1, average='macro', pos_label='1')
    print("Recall score of KNN  IS ->")
    print(metrics.recall_score(y_test, predicted1, average='micro', pos_label='1'))

    f1_score = metrics.f1_score(y_test, predicted1, average='macro', pos_label='1')
    print("F1 score of KNN IS ->")
    print(metrics.f1_score(y_test, predicted1, average='micro', pos_label='1'))

    val = ("KNN", str(knn), str(precision), str(recall), str(f1_score))
    cursor.execute(query, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return knn