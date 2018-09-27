#!/bin/env python
# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
import RPi.GPIO
import atexit
import time

# 自作関数を呼び出すための手続き
import sys
sys.path.append("/smartdustbox/my_mod")
# mail送信関数
from mail import mail_info
# pythonでselect
from my_select import dustbox_select

GPIO_PORT_LED_0 = 5
GPIO_PORT_LED_1 = 6
GPIO_PORT_BTN_0 = 20
GPIO_PORT_BTN_1 = 21

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def root():
    return template("index")

# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"num":"0", "onoff":true}' http://192.168.1.88:8080/setLed
@route('/setLed', method='POST')
def setLedEntry():
    var = request.json
    print (var)

    mail_send(var["num"])

    # if (var["num"] == "naoya" ):
    #     mail_send("NaoyaOshiro")
    # elif (var["num"] == "kosuke" ):
    #     mail_send("KosukeMiyagi")
    # elif (var["num"] == "tomoki" ):
    #     mail_send("TomokiSakuda")
    # elif (var["num"] == "takuto" ):
    #     mail_send("TakutoNakano")

    retBody = {"ret": "ok"}
    r = HTTPResponse(status=200, body=retBody)
    r.set_header('Content-Type', 'application/json')
    return r

# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"dummy":"0"}' http://192.168.1.88:8080/getButton
@route('/getButton', method='POST')
def getButtonEntry():
    retBody = {
        "ret": "ok",
        "btn_0": RPi.GPIO.input(GPIO_PORT_BTN_0),
        "btn_1": RPi.GPIO.input(GPIO_PORT_BTN_1)
    }
    r = HTTPResponse(status=200, body=retBody)
    r.set_header('Content-Type', 'application/json')
    return r



def mail_send(employees_name):
    # sql = "SELECT `name`, `email` FROM `employees` WHERE name = '"+employees_name+"'"
    sql = "SELECT  `name`,  `email`FROM `employees` WHERE 1"
    # print sql
    # sql = "SELECT `name`, `email` FROM `employees` WHERE name = 'NaoyaOshiro'"
    # print dustbox_select(sql)
    rows = dustbox_select(sql)
    mail_data = {}
    for row in rows:
        mail_data[str(row['name'])]=row
    for key, val in mail_data.items():
        # print key, val
        # print val["name"]
        if val["name"] == employees_name:
            pass
        else:
            print val["name"]

            # メールアドレスの設定
            to_addr = val["email"]
            subject = employees_name + "が回収に行きます!!"
            body = employees_name + "が回収に行きます!!!"
            body += "\n\n\nSmartDustBox :  http://192.168.201.35:8888/"
            body += "\nWEBサイト :  http://192.168.201.35:8888/"
            body += "\n\nこのひと↓"
            # 送信画像
            image = "/smartdustbox/image/user_image/"+employees_name + ".png"
            # メール送信
            mail_info( to_addr, subject, body, image )



def main():
    print("Initialize port")
    RPi.GPIO.setmode(RPi.GPIO.BCM)
    RPi.GPIO.setup(GPIO_PORT_LED_0, RPi.GPIO.OUT)
    RPi.GPIO.setup(GPIO_PORT_LED_1, RPi.GPIO.OUT)
    RPi.GPIO.setup(GPIO_PORT_BTN_0, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)
    RPi.GPIO.setup(GPIO_PORT_BTN_1, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)
    RPi.GPIO.output(GPIO_PORT_LED_0, 0)
    RPi.GPIO.output(GPIO_PORT_LED_1, 0)

    print('Server Start')
    run(host='192.168.201.35', port=8888, debug=True, reloader=True)
    # run(host='0.0.0.0', port=8080, debug=False, reloader=False)

def atExit():
    print("atExit")
    RPi.GPIO.cleanup()

if __name__ == '__main__':
    atexit.register(atExit)
    main()
