#!/bin/env python
# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
# import RPi.GPIO
import atexit
import time
import sys
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data, log
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca




@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def root():
    return template("index")
    # return template("backup_index02")


def my_map(val):
    in_min = 0
    in_max = 360
    out_min = 0
    out_max = 100
    val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    val = 100 - val
    # 少数切り捨ての為intに変換
    return int(val)




# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"num":"0", "onoff":true}' http://192.168.1.88:8080/setLed
@route('/setLed', method='POST')
def setLedEntry():
    var = request.json
    # print "-----------------------------------------------------------------------------------------", var["num"]
    # var["num"] = my_map(var["num"])
    # print "-----------------------------------------------------------------------------------------", var["num"]
    #
    # go_back(var["num"])

    setLedEntry2(var["num"])


    # retBody = {"ret": "ok"}
    # r = HTTPResponse(status=200, body=retBody)
    # r.set_header('Content-Type', 'application/json')
    # return r


def setLedEntry2(val):
    # var = request.json
    print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",val
    # return var




# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"dummy":"0"}' http://192.168.1.88:8080/getButton
# @route('/getButton', method='POST')
# def getButtonEntry():
#     retBody = {
#         "ret": "ok",
#         # "btn_0": RPi.GPIO.input(GPIO_PORT_BTN_0),
#         # "btn_1": RPi.GPIO.input(GPIO_PORT_BTN_1)
#     }
#     r = HTTPResponse(status=200, body=retBody)
#     r.set_header('Content-Type', 'application/json')
#     return r

def main():
    print("Initialize port")
    # RPi.GPIO.setmode(RPi.GPIO.BCM)
    # RPi.GPIO.setup(GPIO_PORT_LED_0, RPi.GPIO.OUT)
    # RPi.GPIO.setup(GPIO_PORT_LED_1, RPi.GPIO.OUT)
    # RPi.GPIO.setup(GPIO_PORT_BTN_0, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)
    # RPi.GPIO.setup(GPIO_PORT_BTN_1, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)
    # RPi.GPIO.output(GPIO_PORT_LED_0, 0)
    # RPi.GPIO.output(GPIO_PORT_LED_1, 0)

    print('Server Start')
    run(host='172.20.10.6', port=8080, debug=True, eloader=True)
    # run(host='0.0.0.0', port=8080, debug=False, reloader=False)

def atExit():
    print("atExit")
    # RPi.GPIO.cleanup()

# run(host='172.20.10.6', port=8080, debug=True, eloader=True)
# atexit.register(atExit)
# main()

if __name__ == '__main__':
    atexit.register(atExit)
    main()

    # while True:
    #     print setLedEntry2()
