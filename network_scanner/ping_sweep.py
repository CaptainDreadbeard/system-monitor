# Import required libraries
import subprocess
import platform
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from fingerprint import grab_banner
from arp_scanner import arp_scan
import socket
from full_port_scanner import full_port_scan
from mac_vendor_lookup import lookup_vendor

# Detect OS
def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    timeout = "-w" if platform.system().lower() == "windows" else "-W"

    command = ["ping", param, "1", timeout, "300", ip]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return result.returncode == 0

# Scan common Ports
def scan_common_ports(ip):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

    print(f"\nScanning ports in {ip}...")
    for port in common_ports:
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((ip, port))
            s.close()

            print(f"[+] Port {port} is open")

            banner = grab_banner(ip, port)
            if banner:
                print(f"    └─ Banner: {banner.splitlines()[0]}")
        except:
            pass 

def scan_subnet(base_ip):
    print(f"Scanning subnet: {base_ip}0/24 ...")
    alive_hosts = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(ping_host, f"{base_ip}{i}"): i for i in range(1, 255)}

        for future in futures:
            ip_end = futures[future]
            ip = f"{base_ip}{ip_end}"
            if future.result():
                print(f"[+] Host Alive: {ip}")
                alive_hosts.append(ip)
                scan_common_ports(ip)

    return alive_hosts

def normalize_subnet(user_input):
    # if user inputs full IP, extract the /24 subnet
    try:
        ip = ipaddress.ip_address(user_input)
        parts = user_input.split(".")
        return ".".join(parts[:3]) + "."
    except ValueError:
        # User already added a subnet like "10.0.0"
        if user_input.endswith("."):
            return user_input
        else:
            return user_input + "."

# Main Program

if __name__ == "__main__":
    print("Choose scan type:")
    print("1. Ping Sweep")
    print("2. ARP Scan (recommended)")
    print("3. Full Port Scan")

    choice = input("Enter Choice: ")
    user_input = input("Enter Subnet or IP(e.g. 192.168.1 or 192.168.1.50): ")
    subnet =  normalize_subnet(user_input)
    
    if choice == "2":
        print("\nPerforming ARP scan...")
        results = arp_scan(subnet)
        print("\nARP Scan Results:")
        for ip, mac in results:
            vendor = lookup_vendor(mac)
            print(f"{ip}  →  {mac}  →  {vendor}")
    else:
        results = scan_subnet(subnet)
        print("\nPing Sweep Results:")
        for host in results:
            print(" -", host)
elif choice == "3":
    target = input("Enter a single IP to scan all ports: ")
    full_port_scan(target)