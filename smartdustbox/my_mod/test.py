#coding: utf-8
#!/bin/env python
# 自作関数を呼び出すための手続き
#import sys
#sys.path.append("/smartdustbox/my_mod")
# mail送信関数
from mail import mail_info
# pythonでselect
from my_select import f2, f3


def mail_send(employees_name):
    sql = "SELECT `name`, `email` FROM `employees` WHERE name = "+employees_name+'"'
    print select.dustbox_select(sql)
    # # メールアドレスの設定
    # to_addr = "oosiro708@gmail.com"
    # subject = "kenmei"
    # body = "honbun"
    # image = "neko.png"
    # mail_info( to_addr, subject, body, image )
    # to_addr = "oosiro708@gmail.com"


print "aaa"
f3()
sql = "SELECT `name`, `email` FROM `employees` WHERE name = 'NaoyaOshiro'"
print f2(sql)
