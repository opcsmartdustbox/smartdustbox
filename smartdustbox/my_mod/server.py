# -*- coding: utf-8 -*-

import socket
import numpy as np
import cv2
import threading
# pip install time
# 時間計測の為
import time
# pip install ast
# str型をdict型に変換
import ast
import sys
# 自作関数クライント
import client
# pythonでselect
from my_select import dustbox_select


UDP_IP = "192.168.201.35"
# UDP_IP = "192.168.201.72"
# UDP_IP = "192.168.0.8"
# UDP_IP = "192.168.201.46"
# UDP_IP = "172.20.10.7"
UDP_PORT = 12345
Port_kamera = 23456

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))


class prosess (threading.Thread):
     def run(self):
         global data

t1 = prosess()
t1.start()

# クライアント実行
def client_start():
    client.client()



# 受信したデータを2次元dictに格納
all_data = {}
all_data_map = {}
def server_start():
    print "\n"
    print "---Received data(server.py)---"
    while True:
        #Socketで値を取得
        dust_data, addr = sock.recvfrom(1024)
        #str型をdict型に変換
        dust_data = ast.literal_eval(dust_data)
        # 2次元dict生成
        # exec('all_data["boxid{}"]={}'. format(dust_data["boxid"], dust_data))
        # 受信したデータを2次元dictに格納
        all_data["boxid"+str(dust_data['boxid'])]=dust_data
        all_data_map["boxid"+str(dust_data['boxid'])]=dust_data

        print dust_data


        # boxidにendが来たらSocket_Server を停止
        if dust_data["boxid"] == "end" or dust_data["boxid"] == "END" or dust_data["boxid"] == "End":
            # すべて受信したらマーセントに変換
            all_data_map_func()
            break

        # 画像受信--------------------------------------------------------------
        # if dust_data != "{'boxid':'end'}" :
        #     print "kamera_recv"
        #     socket_kamera = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #     socket_kamera.bind((UDP_IP, Port_kamera))
        #     for img in recive(socket_kamera):
        #         # 保存先
        #         file_name = "dustid"+str(dust_data["boxid"])
        #         cv2.imwrite("/smartdustbox/image/dust_image/"+file_name+".jpg",img)


def all_data_map_func():
    # ゴミ箱容量をセレクト
    sql = "SELECT `boxid`, `capa` FROM `boxinfo` WHERE 1"
    rows = dustbox_select(sql)

    # ゴミ箱容量を辞書型に変換
    # {'11': 30, '10': 30, '1': 30, '3': 30, '2': 50, '5': 30, '4': 30, '7': 30, '6': 30, '9': 30, '8': 30}
    box_capa = {}
    for i in rows:
        box_capa[str(i["boxid"])] = i["capa"]

    # センサで取得した値をパーセントに変換
    for key, val in all_data.items():
        if val["boxid"] == "end":
            pass
        else:
            for key2, val2 in val.items():
                if key2 != "boxid":
                    # all_data[key][key2] = my_map(box_capa[str(val["boxid"])], val2)
                    all_data_map[key][key2] = my_map(box_capa[str(val["boxid"])], val2)

    # return all_data
    return all_data_map


def all_data_func():
    return all_data_map


# パーセントに変換
def my_map(capa, val):
    val = capa - val
    in_min = 0
    in_max = capa
    out_min = 0
    out_max = 100
    val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    # 少数切り捨ての為intに変換
    return int(val)


# 指定された値以上のデータを抽出
# オーバーのデータを入れる（辞書型）
over_data = {}
def over_data_func( over_val ):
    for key, val in all_data_func().items():
        if max(val.values()) >= over_val:
            over_data["boxid"+str(val['boxid'])]=val
    # boxidendは必ず抽出されるので削除
    over_data.pop("boxidend")

    return over_data


# 画像受信
def recive(socket_kamera):
    buff = 1024 * 64
    while True:
        recive_data = bytes()
        while True:
            jpg_str, addr = socket_kamera.recvfrom(buff)
            is_len = len(jpg_str) == 7
            is_end = jpg_str == b'__end__'
            if is_len and is_end: break
            recive_data += jpg_str

        if len(recive_data) == 0: continue

        narray = np.fromstring(recive_data, dtype='uint8')

        img = cv2.imdecode(narray, 1)
        yield img
        print "kamera_getdata"
        break



if __name__ == '__main__':
    client_start()
    server_start()



    # print all_data_func()


    # print all_data

# end
