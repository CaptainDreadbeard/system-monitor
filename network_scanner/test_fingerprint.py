from fingerprint import grab_banner

ip = input("Enter IP: ")
port = int(input("Enter port: "))

banner = grab_banner(ip, port)

if banner:
    print("\n[+] Banner Received:")
    print(banner)
else:
    print("\n[-] No banner or connection refused.")