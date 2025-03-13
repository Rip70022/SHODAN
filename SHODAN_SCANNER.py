import requests
import json
import time
import os
import sys
import random
import ipaddress
from datetime import datetime
from colorama import Fore, Back, Style, init

init(autoreset=True)

API_KEY = "YOUR_API_KEY"
API_URL = "https://api.shodan.io/shodan/host/{ip}?key={key}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art():
    ascii_art = f"""
{Fore.CYAN}
   ▄████████    ▄█    █▄     ▄██████▄  ████████▄     ▄████████ ███▄▄▄▄   
  ███    ███   ███    ███   ███    ███ ███   ▀███   ███    ███ ███▀▀▀██▄ 
  ███    █▀    ███    ███   ███    ███ ███    ███   ███    ███ ███   ███ 
  ███         ▄███▄▄▄▄███▄▄ ███    ███ ███    ███   ███    ███ ███   ███ 
▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ ███    ███ ▀███████████ ███   ███ 
         ███   ███    ███   ███    ███ ███    ███   ███    ███ ███   ███ 
   ▄█    ███   ███    ███   ███    ███ ███   ▄███   ███    ███ ███   ███ 
 ▄████████▀    ███    █▀     ▀██████▀  ████████▀    ███    █▀   ▀█   █▀  
                                                                         
{Fore.MAGENTA}███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
{Fore.MAGENTA}██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
{Fore.MAGENTA}███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
{Fore.MAGENTA}╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
{Fore.MAGENTA}███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
{Fore.MAGENTA}╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                         
    {Fore.GREEN}[ {Fore.YELLOW}Advanced Shodan Intelligence Scanner v1.0 {Fore.GREEN}]
    {Fore.BLUE}[ {Fore.WHITE}GitHub: https://github.com/Rip70022 {Fore.BLUE}]
    """
    print(ascii_art)

def futuristic_loading():
    chars = "▁▂▃▄▅▆▇█▇▆▅▄▃▂▁"
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    
    print(f"\n{Fore.CYAN}[{Fore.WHITE}*{Fore.CYAN}] Initializing cyber-reconnaissance module...")
    time.sleep(0.5)
    
    print(f"{Fore.CYAN}[{Fore.WHITE}*{Fore.CYAN}] Establishing secure connection to Shodan intelligence network...")
    time.sleep(0.5)
    
    print(f"{Fore.CYAN}[{Fore.WHITE}*{Fore.CYAN}] Routing through proxies for enhanced OPSEC...")
    time.sleep(0.5)
    
    print(f"\n{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] Retrieving target intelligence data...\n")
    
    for _ in range(20):
        for char in chars:
            color = random.choice(colors)
            progress = color + char * 50
            sys.stdout.write(f"\r{progress}")
            sys.stdout.flush()
            time.sleep(0.05)
    
    print(f"\n\n{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Connection established! Intelligence data acquired.")
    time.sleep(1)

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def display_host_info(host_data):
    clear_screen()
    print_ascii_art()
    
    print(f"\n{Fore.CYAN}╔{'═' * 70}╗")
    print(f"{Fore.CYAN}║ {Fore.WHITE}TARGET INTELLIGENCE REPORT {' ' * 47}║")
    print(f"{Fore.CYAN}╚{'═' * 70}╝")
    
    print(f"\n{Fore.YELLOW}╔{'═' * 70}╗")
    print(f"{Fore.YELLOW}║ {Fore.WHITE}BASIC INFORMATION {' ' * 53}║")
    print(f"{Fore.YELLOW}╚{'═' * 70}╝")
    
    print(f"\n{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] IP Address: {Fore.WHITE}{host_data.get('ip_str', 'N/A')}")
    print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Organization: {Fore.WHITE}{host_data.get('org', 'N/A')}")
    print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] ISP: {Fore.WHITE}{host_data.get('isp', 'N/A')}")
    print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] ASN: {Fore.WHITE}{host_data.get('asn', 'N/A')}")
    print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Last Update: {Fore.WHITE}{host_data.get('last_update', 'N/A')}")
    
    print(f"\n{Fore.MAGENTA}╔{'═' * 70}╗")
    print(f"{Fore.MAGENTA}║ {Fore.WHITE}LOCATION INFORMATION {' ' * 49}║")
    print(f"{Fore.MAGENTA}╚{'═' * 70}╝")
    
    print(f"\n{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Country: {Fore.WHITE}{host_data.get('country_name', 'N/A')} ({host_data.get('country_code', 'N/A')})")
    print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] City: {Fore.WHITE}{host_data.get('city', 'N/A')}")
    print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Latitude: {Fore.WHITE}{host_data.get('latitude', 'N/A')}")
    print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Longitude: {Fore.WHITE}{host_data.get('longitude', 'N/A')}")
    
    print(f"\n{Fore.BLUE}╔{'═' * 70}╗")
    print(f"{Fore.BLUE}║ {Fore.WHITE}DOMAIN INFORMATION {' ' * 50}║")
    print(f"{Fore.BLUE}╚{'═' * 70}╝")
    
    hostnames = host_data.get('hostnames', [])
    if hostnames:
        print(f"\n{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Hostnames:")
        for hostname in hostnames:
            print(f"  {Fore.CYAN}→ {Fore.WHITE}{hostname}")
    else:
        print(f"\n{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Hostnames: {Fore.WHITE}None found")
    
    domains = host_data.get('domains', [])
    if domains:
        print(f"\n{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Domains:")
        for domain in domains:
            print(f"  {Fore.CYAN}→ {Fore.WHITE}{domain}")
    else:
        print(f"\n{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Domains: {Fore.WHITE}None found")
    
    print(f"\n{Fore.RED}╔{'═' * 30}╗")
    print(f"{Fore.RED}║ {Fore.WHITE}OPEN PORTS & SERVICES {' ' * 48}║")
    print(f"{Fore.RED}╚{'═' * 30}╝")
    
    ports = host_data.get('ports', [])
    if ports:
        print(f"\n{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Open Ports:")
        for port in ports:
            print(f"  {Fore.CYAN}→ {Fore.WHITE}{port}")
    else:
        print(f"\n{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Open Ports: {Fore.WHITE}None found")
    
    print(f"\n{Fore.YELLOW}╔{'═' * 30}╗")
    print(f"{Fore.YELLOW}║ {Fore.WHITE}DETAILED SERVICE INFORMATION {' ' * 42}║")
    print(f"{Fore.YELLOW}╚{'═' * 30}╝\n")
    
    data = host_data.get('data', [])
    if data:
        for i, service in enumerate(data):
            print(f"{Fore.CYAN}┌{'─' * 30}┐")
            print(f"{Fore.CYAN}│ {Fore.WHITE}SERVICE #{i+1} {' ' * 59}│")
            print(f"{Fore.CYAN}└{'─' * 30}┘")
            
            print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Port: {Fore.WHITE}{service.get('port', 'N/A')}")
            print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Protocol: {Fore.WHITE}{service.get('transport', 'N/A')}")
            print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Timestamp: {Fore.WHITE}{service.get('timestamp', 'N/A')}")
            
            module = service.get('_shodan', {}).get('module', 'N/A')
            print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Module: {Fore.WHITE}{module}")
            
            if 'data' in service and service['data']:
                print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Data: {Fore.WHITE}{service['data']}")
            
            print("")
    else:
        print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Detailed Service Information: {Fore.WHITE}None available")
    
    print(f"\n{Fore.CYAN}╔{'═' * 30}╗")
    print(f"{Fore.CYAN}║ {Fore.WHITE}SCAN COMPLETED AT: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {' ' * 27}║")
    print(f"{Fore.CYAN}╚{'═' * 30}╝")

def fetch_host_data(ip):
    url = API_URL.format(ip=ip, key=API_KEY)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}] Error: {e}")
        return None

def main():
    clear_screen()
    print_ascii_art()
    
    while True:
        print(f"\n{Fore.CYAN}[{Fore.WHITE}*{Fore.CYAN}] Enter target IP address to scan (or 'exit' to quit):")
        ip = input(f"{Fore.GREEN}┌──({Fore.CYAN}Shodan Scanner{Fore.GREEN})─[{Fore.WHITE}~{Fore.GREEN}]\n└─$ {Fore.WHITE}")
        
        if ip.lower() == 'exit':
            print(f"\n{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] Terminating session. Follow me on GitHub for more scripts!")
            break
        
        if not validate_ip(ip):
            print(f"\n{Fore.RED}[{Fore.WHITE}!{Fore.RED}] Invalid IP address. Please try again.")
            continue
        
        futuristic_loading()
        
        host_data = fetch_host_data(ip)
        if host_data:
            display_host_info(host_data)
        else:
            print(f"\n{Fore.RED}[{Fore.WHITE}!{Fore.RED}] Failed to retrieve data for {ip}. The IP might not be indexed by Shodan.")
        
        print(f"\n{Fore.CYAN}[{Fore.WHITE}*{Fore.CYAN}] Press Enter to continue...")
        input()
        clear_screen()
        print_ascii_art()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[{Fore.WHITE}*{Fore.YELLOW}] Operation cancelled by user. Exiting...")
        sys.exit(0)
