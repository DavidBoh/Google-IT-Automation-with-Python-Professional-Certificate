#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
path = '/home/user/supplier-data/images/'
files = os.listdir(path)

file_list = []

for f in files:
    if os.path.isfile(os.path.join(path,f)):
        file_list.append(f)

for i in file_list:
    f = os.path.join(path, i)
    with open(f, 'rb') as opened:
        if f.endswith(".jpeg"):
            r = requests.post(url, files={'file': opened})

