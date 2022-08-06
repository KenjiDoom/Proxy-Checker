from colorama import Fore
import concurrent.futures
import requests
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
        results = executor.map(grab_proxies, urls) # executor.map method

def proxy_checker(filename):
    with open(filename, 'r') as IP:
        for proxy in IP:
            try:
                proxy = proxy.strip()
                #print(Fore.WHITE + "Using" + filename) # This will display where the proxy is being used from
                if filename.strip('http'): # How can I clean this up? Duplicate code
                    r = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https':proxy}, timeout=1)
                    print(Fore.RED + "HTTP Proxy" + proxy)
                elif filename.strip('socks5.txt'):
                    r = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https':proxy}, timeout=1)
                    print(Fore.RED + "SOCKS5 PROXY: " + proxy)
                elif filename.strip('socks4.txt'):
                    r = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https':proxy}, timeout=1)
                    print(Fore.RED + "SOCKS4 PROXY: " + proxy)
            except requests.ConnectionError as err:
                    #print(Fore.GREEN + repr(err))
                    print(Fore.GREEN + proxy + " is not working")
# Self-note:
# How to know what file is being used? 
# to save to a socks5, socks4 working file

def test_proxies():
    direct = os.getcwd()
    filename = [direct + '/socks5.txt',
    direct + '/socks4.txt',
    direct + '/http.txt']
    # Self-Note: Grab the users path for the .txt files

    # shotcut to not creating a full for loop using the map function
    #              # function goes,   # list goes here
    if all(list(map(os.path.exists, filename))):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(proxy_checker, filename)
    else:
        print(Fore.RED + "Proxy files are not found. Starting Download...")
        download_proxies()
        test_proxies()


test_proxies()
