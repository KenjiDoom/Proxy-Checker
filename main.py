from colorama import Fore
from time import time
import concurrent.futures
import requests
import wget
import os

def grabproxies(url):
    # The main work function
    file_name_start_pos = url.rfind("/") + 1
    file_name = url[file_name_start_pos:]
    

    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        print(Fore.GREEN + "Downloaded: " + url)
        with open(file_name, 'wb') as f:
            for data in r:
                f.write(data)
    elif r.status_code == 404:
        print(Fore.RED + "404 Failed to download: " + url)

def download_proxies():
    # Thanks to TheSpeedX
    urls = ['https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt']
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(grabproxies, urls)

def testproxies():
    pass

# Thanks to TheSpeedX
#grabproxies("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txtgt")
#grabproxies("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
#grabproxies("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
download_proxies()