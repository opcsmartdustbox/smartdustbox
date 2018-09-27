# -*- coding: utf-8 -*-

import socket
import time


#UDP_IP = "192.168.201.72"
# UDP_IP = "192.168.0.7"
# UDP_IP = "192.168.201.46"
# UDP_PORT = 23456


#while True:
def func001( func001_data, UDP_IP, UDP_PORT ):
    # my_dict = {'boxid':'', 'burnable':'', 'unburnable':'', 'cans':'', 'plastic':'', 'glass':''}
    #
    # my_dict["boxid"] = 001
    # my_dict["burnable"] = 82
    # my_dict["unburnable"] = 61
    # my_dict["cans"] = 97
    # my_dict["plastic"] = 65
    # my_dict["glass"] = 99
    #
    # my_dict = str(my_dict)
    my_dict = str( func001_data )

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(my_dict, (UDP_IP, UDP_PORT))
    sock.close()

#    time.sleep(3)
