import socket
from concurrent.futures import ThreadPoolExecutor
from fingerprint import grab_banner

# Definitions

def scan_port(ip, port, timeout=0.5):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False
    
def full_port_scan(ip, max_workers=500):
    print(f"\n[+] Starting full port scan on {ip} (1-65535)...")
    open_ports = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in range(1, 65535)}

        for future in futures:
            port = futures[future]
            if future.result():
                print(f"[+] Port {port} is open!")

                banner = grab_banner(ip, port)
                if banner:
                    print(f"    └─ Banner: {banner.splitlines()[0]}")

                open_ports.append(port)

    return open_ports
