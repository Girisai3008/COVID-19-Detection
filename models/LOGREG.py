from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import mysql.connector
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_score
from DBconn import DBConnection
# from sklearn.metrics import plot_confusion_matrix
# import matplotlib.pyplot as plt
def classify_lr(x_train, x_test, y_train, y_test):
    mydb = DBConnection.getConnection()
    cursor = mydb.cursor()
    classify4 = LogisticRegression()
    classify4.fit(x_train, y_train)
    predicted4 = classify4.predict(x_test)
    query = "INSERT INTO  performance  VALUES (%s,%s,%s,%s,%s)"

    lr = metrics.accuracy_score(y_test, predicted4) * 100
    print("The accuracy score using the LogisticREG is ->")
    print(metrics.accuracy_score(y_test, predicted4))

    precision = metrics.precision_score(y_test, predicted4, average='macro', pos_label='1')
    print("Precision score of LogisticREG IS ->")
    print(metrics.precision_score(y_test, predicted4, average='micro', pos_label='1'))

    recall = metrics.recall_score(y_test, predicted4, average='macro', pos_label='1')
    print("Recall score of LogisticREG  IS ->")
    print(metrics.recall_score(y_test, predicted4, average='micro', pos_label='1'))

    f1_score = metrics.f1_score(y_test, predicted4, average='macro', pos_label='1')
    print("F1 score of LogisticREG IS ->")
    print(metrics.f1_score(y_test, predicted4, average='micro', pos_label='1'))


    # plot_confusion_matrix(classify4, x_test, y_test)
    # plt.title('Confusion Matrix of LogisticREG')
    # plt.show()
    val = ("LogisticREG", str(lr), str(precision), str(recall), str(f1_score))
    cursor.execute(query, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return lr