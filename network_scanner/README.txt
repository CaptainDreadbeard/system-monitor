# **Disclaimer**
This tool is intended **only for scanning networks you own or have permission to analyze**.  
Unauthorized scanning of networks may violate local laws or terms of service.
---

# **Network Scanner & Recon Toolkit**  
A modular, multi‑function network reconnaissance tool written in Python.  
Designed for LAN discovery, port scanning, service fingerprinting, and device identification using ARP and MAC vendor lookup.

This tool is built to be:

- **Beginner‑friendly** — anyone can run it  
- **Technically accurate** — behaves like real recon tools  
- **Modular** — each feature is its own clean module  
- **Fast** — uses threading for high‑speed scanning  
- **Cross‑platform** — works on Windows, macOS, and Linux  

---

# **Features**

### ✔ **Ping Sweep (ICMP Host Discovery)**  
Scans an entire `/24` subnet (e.g., `192.168.1.0/24`) to find alive hosts.

### ✔ **Common Port Scanner**  
Automatically scans common ports (22, 80, 443, etc.) on each alive host.

### ✔ **Banner Grabbing**  
Identifies services running on open ports (e.g., Apache, SSH, nginx).

### ✔ **ARP Scanner (Layer‑2 Discovery)**  
Reads the ARP table to find devices on the LAN — even those that block ping.

### ✔ **MAC Vendor Lookup**  
Identifies device manufacturers (Apple, Samsung, Cisco, Amazon, Google, etc.).

### ✔ **Full Port Scanner (1–65535)**  
Threaded, high‑speed scan of every TCP port on a target device.

---

# **Who Is This Tool For?**

This tool is ideal for:

- Students learning networking or cybersecurity  
- Home users mapping their own network  
- Developers wanting a clean example of modular Python networking code  
- Anyone who wants to understand what devices are on their LAN  

No prior networking knowledge is required — the tool explains everything as it runs.

---

# **Installation**

### **1. Install Python 3.10+**
Download from:  
[https://www.python.org/downloads/](https://www.python.org/downloads/)

### **2. Clone the repository**
```
git clone https://github.com/YOUR_USERNAME/network-scanner.git
cd network-scanner
```

### **3. Install required Python modules**
This project uses only Python’s standard library — **no external dependencies**.

You can run it immediately.

---

# **How to Run the Program**

From inside the project folder:

```
python ping_sweep.py
```

You will see a menu:

```
Choose scan type:
1. Ping Sweep
2. ARP Scan (recommended)
3. Full Port Scan
```

---

# **Scan Modes Explained (Beginner‑Friendly)**

## **1. Ping Sweep**
Use this when you want to find all devices on your network.

Example input:
```
192.168.1.50
```

The tool automatically converts this to:
```
192.168.1.0/24
```

It will show:
- which devices are alive  
- which ports are open  
- what services are running  

---

## **2. ARP Scan (Recommended)**
Use this for the **most accurate device discovery**.

ARP scanning finds devices even if they:

- block ping  
- don’t respond to ICMP  
- are phones/tablets using privacy features  

Output example:
```
10.0.0.1    → 1c:9d:72:70:d3:cf → Cisco Systems
10.0.0.37   → e0:bb:9e:0f:68:5f → Samsung Electronics
10.0.0.142  → 6c:22:1a:03:66:5b → Apple Inc.
```

This tells you:
- the IP address  
- the MAC address  
- the device manufacturer  

---

## **3. Full Port Scan**
Use this when you want to scan **every port** on a single device.

Example:
```
Enter IP: 10.0.0.124
```

The tool scans ports **1–65535** and prints:

- open ports  
- service banners  
- protocol information  

Example output:
```
[+] Port 22 is open
    └─ Banner: SSH-2.0-OpenSSH_6.6.0
[+] Port 80 is open
    └─ Banner: HTTP/1.1 405 Method Not Allowed
```

---

# **Understanding the Output**

### **Open Ports**
If you see:
```
[+] Port 80 is open
```
That means the device is running a web server.

### **Banners**
If you see:
```
SSH-2.0-OpenSSH_6.6.0
```
That tells you:
- the service (SSH)  
- the version (OpenSSH 6.6.0)  
- the OS family (Linux/Unix)  

### **MAC Vendor**
If you see:
```
Samsung Electronics
Apple Inc.
Amazon Technologies
Cisco Systems
Google Inc.
```
You know exactly what type of device it is.

---

# **Project Structure**

```
network_scanner/
│
├── ping_sweep.py            # Main program & menu
├── arp_scanner.py           # ARP scanning module
├── full_port_scanner.py     # Full 1–65535 port scanner
├── fingerprint.py           # Banner grabbing module
├── mac_vendor_lookup.py     # MAC vendor identification
└── README.md                # Documentation
```

---

