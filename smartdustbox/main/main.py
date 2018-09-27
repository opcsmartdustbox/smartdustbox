# -*- coding: utf-8 -*-
# 時刻取得
from datetime import datetime

# 自作関数を呼び出すための手続き
import sys
sys.path.append("/smartdustbox/my_mod")
# 自作関数
from server import all_data_func, over_data_func, client_start, server_start
# pythonでinsert
from insert import dustbox_insert
# pythonでselect
from my_select import dustbox_select
# mail送信関数
from mail import mail_info

sys.path.append("/smartdustbox/voice")
from jtalk import say_datetime, jtalk

# -----------------------------------------------------------------------------



over_val = 70
# kugiri = "□■"*8
kugiri = "--"*15


# ごみ箱の設置場所を取得
def boxname_select():
    sql = "SELECT `boxid`, `boxname` FROM `boxinfo` WHERE 1"
    rows = dustbox_select(sql)

    boxname = {}
    for row in rows:
        # unicod から strに変換してから辞書型に代入
        boxname[str(row["boxid"])] = row["boxname"].encode('utf8')
    return boxname


def mail_send():
    # 英語を日本語に変換する為の辞書型を作成
    dust_data_jp = {'unburnable': '燃えないゴミ', 'plastic': 'ペットボトル', 'glass': 'ビン', 'cans': 'カン', 'burnable': '燃えるゴミ', 'boxid': 'ゴミ箱番号'}
    # オーバーデータを設定して取得
    over_data = over_data_func(over_val)
    # オーバーデータの数を取得
    over_data_numver = len(over_data)
    # メールアドレスの設定
    to_addr = "oosiro708@gmail.com"
    # to_addr = "m.kou0809@gmail.com"
    # 送信画像
    image = "/smartdustbox/image/dust_image/dust_now.jpg"

    # オーバーしてるデータがあるときとないとき
    if over_data_numver == 0:
        subject = "満タンのゴミ箱はありません!!"
        body = "満タンのゴミ箱はありません!!"
        body += "\n\n\nSmartDustBox :  http://192.168.201.35:8888/"
        body += "\nWEBサイト :  http://192.168.201.35/doc/dustbox.php"
    else:
        boxname = boxname_select()
        print "\n"
        print "---Over data numver:", over_data_numver, "---"
        # 件名を作成(オーバーしているデータの数を取得)
        subject = str(over_data_numver)+"箇所のゴミ箱が満タンです!!"
        # 本文を作成(オーバーしているデータの数を取得)
        body = "\n"+str(over_data_numver)+"箇所のゴミ箱が満タンです!!\n\n"
        # oオーバーしているデータをソートしながら、本文を作成
        for key, val in sorted(over_data.items()):
            print key, val
            body += kugiri
            body += "\nゴミ箱ID:" + str(val["boxid"])
            body += "（" + boxname[str(val["boxid"])] + "）\n"

            for key2, val2 in val.items():
                # over_val以上の値があったら実行(ゴミの種類)
                if val2 >= over_val:
                    body += dust_data_jp[key2] + ":" + str(val2) + "%\n"
                    # body += str(val2) + "\n"


    body += "\n\n\nSmartDustBox :  http://192.168.201.35:8888/"
    body += "\nWEBサイト : http://192.168.201.35/doc/dustbox.php"
    body += "\n\nRaspberryPi3B+ からの送信"
    # メール送信内容の確認
    print "\n"
    print "---Sent Mail---"
    print "=================================================="
    print "to_addr\n"+to_addr
    print "================================="
    print "subject\n"+subject
    print "================================="
    print "body"+body
    print "=================================================="
    print "\n"


    print "Sending mail!!"
    mail_info( to_addr, subject, body, image )
    print "Sent mail!!\n"


def voice_data_func():
    dust_data_jp = {'unburnable': '燃えないゴミ', 'plastic': 'ペットボトル', 'glass': 'ビン', 'cans': 'カン', 'burnable': '燃えるゴミ', 'boxid': 'ゴミ箱番号'}
    over_data = over_data_func(over_val)
    over_data_numver = len(over_data)

    d = datetime.now()
    time_now = '%s月%s日、%s時%s分%s秒現在、' % (d.month, d.day, d.hour, d.minute, d.second)

    if over_data_numver == 0:
        voice_data = time_now + "満タンのゴミ箱はありません!!"
    else:
        print "オーバーしているゴミ箱の数:",over_data_numver
        print "オーバーしているゴミ箱のデータ↓"

        voice_data = time_now + str(over_data_numver)+"箇所のゴミ箱が満タンです!!読み上げます、"

        for key, val in sorted(over_data.items()):
            print key, val
            voice_data += "ゴミ箱番号:" + str(val["boxid"]) + "は、"
            for key2, val2 in val.items():
                # over_val以上の値があったら実行
                if val2 >= over_val:
                    voice_data += dust_data_jp[key2] + "が" + str(val2) + "%、"

    voice_data += "以上が満タンのゴミ箱です。"
    # メール送信内容の確認
    print "読み上げる内容↓"
    print voice_data

    return voice_data


# ソートしてからインサート
def all_data_insert():
    for key, val in sorted(all_data_func().items()):
        if val["boxid"] == "end":
            pass
        else:
            id =            str( val["boxid"] )
            boxid =         str( val["boxid"] )
            burnable =      str( val["burnable"] )
            unburnable =    str( val["unburnable"] )
            cans =          str( val["cans"] )
            plastic =       str( val["plastic"] )
            glass =         str( val["glass"] )
            image =         "'/smartdustbox/image/dust_image/dustbox"+str(val["boxid"])+".jpg'"
            flag =          "0"

            # INSERT INTO `dustbox`(`boxid`, `time`, `burnable`, `unburnable`, `cans`, `plastic`, `glass`, `flag`, `image`) VALUES(8, NOW(), 16, 23, 10, 86, 13, 0, '/smartdustbox/image/dust_image/dustbox8.jpg')
            sql = "INSERT INTO `dustbox`(`boxid`, `time`, `burnable`, `unburnable`, `cans`, `plastic`, `glass`, `flag`, `image`) "
            sql += "VALUES("+boxid+", NOW(), "+burnable+", "+unburnable+", "+cans+", "+plastic+", "+glass+", "+flag+", "+image+")"


            # insert実行
            print sql
            dustbox_insert( sql )



if __name__ == '__main__':
    # client_start()
    server_start()

    mail_send()
    boxname_select()
    all_data_insert()

    # jtalk(voice_data_func())


#end
