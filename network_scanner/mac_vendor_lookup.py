# Simple MAC Vendor lookup module

OUI_DB = {
    "1c:9d:72": "Cisco Systems",
    "e0:bb:9e": "Samsung Electronics",
    "9e:aa:5f": "Amazon Technologies",
    "6c:22:1a": "Apple Inc",
    "3c:e1:a1": "Google Inc",
    "7a:ce:81": "Unknown / Randomized MAC"
}

# definitions

def normalize_mac(mac):
    return mac.lower().replace("-", ":")[:8]

def lookup_vendor(mac):
    prefix = normalize_mac(mac)
    return OUI_DB.get(prefix, "Unknown Vendor")