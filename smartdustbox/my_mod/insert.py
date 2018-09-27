#coding:utf-8
import pymysql.cursors


def dustbox_insert( sql ):
    # print "DB connection now"
    # print "DB insert now"
    # 接続情報
    dbh = pymysql.connect(
             host='localhost',
             user='root',
             password='password',
             db='smartdustbox',
             charset='utf8',
             cursorclass=pymysql.cursors.DictCursor
        )

    # カーソル
    stmt = dbh.cursor()

    # sql
    # sql = "INSERT INTO `dustbox`(`id`, `boxid`, `time`, `burnable`, `unburnable`, `cans`, `plastic`, `glass`, `flag`) VALUES (1, 1, NOW(), 83, 87, 47, 92, 34, 0)"
    # print "sqlの内容=", sql

    # 実行
    stmt.execute(sql)

    # コミット
    dbh.commit()

    # 掃除
    stmt.close()
    dbh.close()
    # print "DB connection end"
    # print "DB insert end"
