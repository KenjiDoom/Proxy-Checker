from colorama import Fore
from time import time
import concurrent.futures
import requests
import wget
import os

def grab_proxies(url):
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
        results = executor.map(grab_proxies, urls) # pool map method

def proxy_checker(filename):
    with open(filename, 'r') as IP:
        for proxy in IP:
            try:
                proxy = proxy.strip()
                r = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https':proxy}, timeout=1)
                print(Fore.RED + proxy)
            except requests.ConnectionError as err:
                    print(Fore.GREEN + repr(err))

# Self-note:
# How to know what file is being used? 
# to save to a socks5, socks4 working file


def test_proxies():
    filename = ['/home/$USER/Desktop/Proxy-Checker/socks5.txt',
    '/home/$USER/Desktop/Proxy-Checker/socks4.txt',
    '/home/$USER/Desktop/Proxy-Checker/http.txt']
    # Self-Note: Grab the users path for the .txt files

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(proxy_checker, filename)



test_proxies()
#download_proxies()