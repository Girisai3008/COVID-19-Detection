from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import mysql.connector
from sklearn.metrics import roc_auc_score
from sklearn.metrics import precision_score
from DBconn import DBConnection
# from sklearn.metrics import plot_confusion_matrix
# import matplotlib.pyplot as plt

def classify_nb(x_train, x_test, y_train, y_test):
    mydb = DBConnection.getConnection()
    cursor = mydb.cursor()
    classify3 = GaussianNB()
    classify3.fit(x_train, y_train)
    predicted3 = classify3.predict(x_test)
    query = "INSERT INTO  performance  VALUES (%s,%s,%s,%s,%s)"

    NB = metrics.accuracy_score(y_test, predicted3) * 100
    print("The accuracy score using the NaiveBayes is ->")
    print(metrics.accuracy_score(y_test, predicted3))

    precision = metrics.precision_score(y_test, predicted3, average='macro', pos_label='1')
    print("Precision score of NaiveBayes IS ->")
    print(metrics.precision_score(y_test, predicted3, average='micro', pos_label='1'))

    recall = metrics.recall_score(y_test, predicted3, average='macro', pos_label='1')
    print("Recall score of NaiveBayes  IS ->")
    print(metrics.recall_score(y_test, predicted3, average='micro', pos_label='1'))

    f1_score = metrics.f1_score(y_test, predicted3, average='macro', pos_label='1')
    print("F1 score of NaiveBayes IS ->")
    print(metrics.f1_score(y_test, predicted3, average='micro', pos_label='1'))


    # plot_confusion_matrix(classify3, x_test, y_test)
    # plt.title('Confusion Matrix of NaiveBayes')
    # plt.show()
    val = ("NaiveBayes", str(NB), str(precision), str(recall), str(f1_score))
    cursor.execute(query, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return NB