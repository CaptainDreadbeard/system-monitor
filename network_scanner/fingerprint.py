# import necessities
import socket

# define necessary functions
def grab_banner(ip, port, timeout=2):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((ip, port))

        # optional probe (helps with some services)
        try:
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        except:
            pass

        banner = s.recv(1024)
        s.close()

        return banner.decode(errors="ignore").strip()
    
    except Exception as e:
        return None