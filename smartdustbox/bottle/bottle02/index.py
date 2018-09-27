#!/bin/env python
# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
# import RPi.GPIO
import atexit
import time
import sys
# sys.path.append("/kaiyo/my_mod")
# from my_get_serial import get_data, send_data, log
# from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca



@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


@route('/')
def root():
    return template("index")


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
    print
    print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",var
    print
    # fnc(var)


# def fnc(val):
#     va = request.json
#     print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",va
#     return va


def main():
    print("Initialize port")
    print('Server Start')
    run(host='192.168.201.35', port=8080, debug=True, eloader=True)
    # run(host='172.20.10.6', port=8080)


def atExit():
    print("atExit")

# atexit.register(atExit)
# main()
if __name__ == '__main__':
    atexit.register(atExit)
    main()
