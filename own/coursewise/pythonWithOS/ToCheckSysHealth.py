'''import shutil
import psutil

def check_disk_usage(disk):
    du=shutil.disk_usage(disk)
    free=du.free/du.total *100
    return free>20

def check_cpu_usage():
    usage=psutil.cpu_percent(1)
    return usage<75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERRor")
else :
    print('everythn is a ok')'''

import socket
import requests

def check_localhost():
    localhost=socket.gethostbyname("localhost")
    return localhost== "127.0.0.1"
def check_connectivity():
    request=requests.get("http://www.google.com")
    return request.status_code==200
print(check_connectivity())
print(check_localhost())