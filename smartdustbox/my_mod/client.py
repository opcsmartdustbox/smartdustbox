# -*- coding: utf-8 -*-

import time
import client001
import client002
import client003
import client004
import client_end
import random



UDP_IP = "192.168.201.35"
# UDP_IP = "192.168.201.72"
# UDP_IP = "192.168.0.8"
# UDP_IP = "192.168.201.46"
# UDP_IP = "172.20.10.7"
UDP_PORT = 12345


func001_data = \
{'unburnable': 62, 'plastic': 0, 'glass': 99, 'cans': 97, 'burnable': 87, 'boxid': 1}
func002_data = \
{'unburnable': 43, 'plastic': 8, 'glass': 82, 'cans': 98, 'burnable': 34, 'boxid': 2}
func003_data = \
{'unburnable': 43, 'plastic': 23, 'glass': 0, 'cans': 2, 'burnable': 73, 'boxid': 3}
func004_data = \
{'unburnable': 84, 'plastic': 23, 'glass': 82, 'cans': 2, 'burnable': 80, 'boxid': 4}


func005_data = \
{'unburnable': 62, 'plastic': 0, 'glass': 99, 'cans': 97, 'burnable': 87, 'boxid': 1}
func006_data = \
{'unburnable': 43, 'plastic': 8, 'glass': 82, 'cans': 98, 'burnable': 34, 'boxid': 2}
func007_data = \
{'unburnable': 62, 'plastic': 0, 'glass': 99, 'cans': 97, 'burnable': 87, 'boxid': 1}
func008_data = \
{'unburnable': 43, 'plastic': 8, 'glass': 82, 'cans': 98, 'burnable': 34, 'boxid': 2}
func009_data = \
{'unburnable': 43, 'plastic': 23, 'glass': 0, 'cans': 2, 'burnable': 73, 'boxid': 3}
func010_data = \
{'unburnable': 84, 'plastic': 23, 'glass': 82, 'cans': 2, 'burnable': 80, 'boxid': 4}


# ゴミ箱の容量
capa = 30

for key, val in func001_data.items():
    func001_data[key] = random.randrange(capa)
    func001_data["boxid"] = 1

for key, val in func002_data.items():
    func002_data[key] = random.randrange(capa)
    func002_data["boxid"] = 2

for key, val in func003_data.items():
    func003_data[key] = random.randrange(capa)
    func003_data["boxid"] = 3

for key, val in func004_data.items():
    func004_data[key] = random.randrange(capa)
    func004_data["boxid"] = 4


for key, val in func005_data.items():
    func005_data[key] = random.randrange(capa)
    func005_data["boxid"] = 5

for key, val in func006_data.items():
    func006_data[key] = random.randrange(capa)
    func006_data["boxid"] = 6

for key, val in func007_data.items():
    func007_data[key] = random.randrange(capa)
    func007_data["boxid"] = 7

for key, val in func008_data.items():
    func008_data[key] = random.randrange(capa)
    func008_data["boxid"] = 8

for key, val in func009_data.items():
    func009_data[key] = random.randrange(capa)
    func009_data["boxid"] = 9

for key, val in func010_data.items():
    func010_data[key] = random.randrange(capa)
    func010_data["boxid"] = 10

# over_valがないデータ
# func001_data = \
# {'unburnable': 62, 'plastic': 0, 'glass': 9, 'cans': 7, 'burnable': 8, 'boxid': 1}
# func002_data = \
# {'unburnable': 43, 'plastic': 8, 'glass': 8, 'cans': 9, 'burnable': 34, 'boxid': 2}
# func003_data = \
# {'unburnable': 43, 'plastic': 23, 'glass': 0, 'cans': 2, 'burnable': 73, 'boxid': 3}
# func004_data = \
# {'unburnable': 3, 'plastic': 23, 'glass': 2, 'cans': 2, 'burnable': 0, 'boxid': 4}


def client():
    client003.func003( func003_data, UDP_IP, UDP_PORT )
    client001.func001( func001_data, UDP_IP, UDP_PORT )
    client004.func004( func004_data, UDP_IP, UDP_PORT )
    client002.func002( func002_data, UDP_IP, UDP_PORT )

    client003.func003( func005_data, UDP_IP, UDP_PORT )
    client001.func001( func006_data, UDP_IP, UDP_PORT )
    client004.func004( func007_data, UDP_IP, UDP_PORT )
    client002.func002( func008_data, UDP_IP, UDP_PORT )
    client004.func004( func009_data, UDP_IP, UDP_PORT )
    client002.func002( func010_data, UDP_IP, UDP_PORT )
    time.sleep(0.5)
    client_end.end( UDP_IP, UDP_PORT )

if __name__ == '__main__':
    # pass
    client()
