# -*- coding: utf-8 -*-

import socket
import time


#UDP_IP = "192.168.201.72"
# UDP_IP = "192.168.0.7"
# UDP_IP = "192.168.201.46"
# UDP_PORT = 23456


#while True:
def func002( func002_data, UDP_IP, UDP_PORT ):
    # my_dict = {'dustid':'', 'burnable':'', 'unburnable':'', 'cans':'', 'plastic':'', 'glass':''}
    #
    # my_dict["dustid"] = 002
    # my_dict["burnable"] = 34
    # my_dict["unburnable"] = 43
    # my_dict["cans"] = 99
    # my_dict["plastic"] = 8
    # my_dict["glass"] = 82
    #
    # my_dict = str(my_dict)
    my_dict = str( func002_data )


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(my_dict, (UDP_IP, UDP_PORT))
    sock.close()

#    time.sleep(3)
