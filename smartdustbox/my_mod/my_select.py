#coding:utf-8
import pymysql.cursors

def dustbox_select(sql):
    #接続情報
    dbh = pymysql.connect(
             host='localhost',
             user='root',
             password='password',
             db='smartdustbox',
             charset='utf8',
             cursorclass=pymysql.cursors.DictCursor
        )

    #カーソル
    stmt = dbh.cursor()

    #SQL
    # sql = "select * from dustbox where state >= 80"

    #実行
    stmt.execute(sql)

    #取得
    rows = stmt.fetchall()

    # print rows
    # print type(rows)
    # 取得した値(list型)をdict型に変換
    # for row in rows : pass
    """
    select_data = {}
    for row in rows:
        select_data["boxid"+str(row['boxid'])]=row

    print select_data
    """

    # print rows

    for row in rows:
        # print row
        pass

    #掃除
    stmt.close();
    dbh.close();

    return rows

# if __name__ == '__main__':
#     sql = "SELECT * FROM `employees` WHERE 1"
#     sql = "SELECT `name`, `email` FROM `employees` WHERE name = 'NaoyaOshiro'"
#     print dustbox_select(sql)
