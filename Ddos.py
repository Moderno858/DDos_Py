  GNU nano 2.9.3                       ddos.py                        Modified  

import  socket
import sys
import os

____  ____   ___  ____  
|  _ \|  _ \ / _ \/ ___| 
| | | | | | | | | \___ \ 
| |_| | |_| | |_| |___) |
|____/|____/ \___/|____/ 

Powered by Moderno \n\n

def init(ip, port , main):
           client  = socket.socket(socket.AF_INET, socket,SOCK_STREAM)
           client.settimeout(0.03)
           code = client.connect_ex((ip, int(port)))
            if code == 0;
                     print("[==>] -Realizando ataque ")
                     print("IP: %s, PORT:%s",ip ,port)


