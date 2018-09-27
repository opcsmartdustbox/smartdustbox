# -*- coding: utf-8 -*-

import socket
import time


#UDP_IP = "192.168.201.72"
# UDP_IP = "192.168.0.7"
# UDP_IP = "192.168.201.46"
# UDP_PORT = 23456


#while True:
def end( UDP_IP, UDP_PORT):
    my_dict = {'boxid':'end'}

    # my_dict["boxid"] = "end"

    my_dict = str(my_dict)


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(my_dict, (UDP_IP, UDP_PORT))
    sock.close()

#    time.sleep(3)

if __name__ == '__main__':
    UDP_IP = "192.168.201.35"
    UDP_PORT = 12345
    end( UDP_IP, UDP_PORT)
