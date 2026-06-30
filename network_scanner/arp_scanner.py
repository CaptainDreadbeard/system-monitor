import subprocess
import platform
import re

# -----------------------------
# Windows ARP Scanner
# -----------------------------
def arp_scan_windows():
    try:
        output = subprocess.check_output("arp -a", shell=True).decode()
    except:
        return []
    
    hosts = []
    for line in output.splitlines():
        match = re.search(r"(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F\-]{17})", line)
        if match:
            ip = match.group(1)
            mac = match.group(2).replace("-", ":").lower()
            hosts.append((ip, mac))
    
    return hosts

# -----------------------------
# Linux/MacOS ARP Scanner
# -----------------------------
def arp_scan_unix(subnet):
    try:
        output = subprocess.check_output("arp -a", shell=True).decode()
    except:
        return []
    
    hosts = []
    for line in output.splitlines():
        match = re.search(r"\((\d+\.\d+\.\d+\.\d+)\)\s+at\s+([0-9a-fA-F:]{17})", line)
        if match:
            ip = match.group(1)
            mac = match.group(2).lower()
            hosts.append((ip, mac))

    return hosts

# -----------------------------
# Filter function
# -----------------------------
def is_valid_host(ip, mac):
    # Skip broadcast MAC
    if mac == "ff:ff:ff:ff:ff:ff":
        return False
    
    # Skip multicast MAC (01:00:5e:xx:xx:xx)
    if mac.startswith("01:00:5e"):
        return False
    
    # Skip multicast IPs (224.x.x.x, 239.x.x.x)
    first_octet = int(ip.split(".")[0])
    if 224 <= first_octet <= 239:
        return False
    
    return True

# -----------------------------
# Unified ARP Scanner
# -----------------------------
def arp_scan(subnet=None):
    os_name = platform.system().lower()

    if "windows" in os_name:
        hosts = arp_scan_windows()
    else:
        hosts = arp_scan_unix(subnet)

    # Apply filter HERE
    filtered = [(ip, mac) for ip, mac in hosts if is_valid_host(ip, mac)]
    return filtered
