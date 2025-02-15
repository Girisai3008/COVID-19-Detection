import mysql.connector
import sys
class DBConnection:
    @staticmethod
    def getConnection():
        try:
            database = mysql.connector.connect(host="localhost", user="root", password="root", db='covid')
            return database
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
if __name__=="__main__":
    print(DBConnection.getConnection())