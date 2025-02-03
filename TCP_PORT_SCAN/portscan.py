import socket
import concurrent.futures

# LIST TOP 100 TCP PORTS
# https://nullsec.us/top-1-000-tcp-and-udp-ports-nmap-default/
TOP_PORTS = {
    80: "HTTP",
    23: "Telnet",
    443: "HTTPS",
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    3389: "RDP (Microsoft Remote Desktop)",
    110: "POP3",
    445: "Microsoft-DS (SMB)",
    139: "NetBIOS",
    143: "IMAP",
    53: "DNS",
    135: "MSRPC",
    3306: "MySQL",
    8080: "HTTP Proxy",
    1723: "PPTP VPN",
    111: "RPCBind",
    995: "POP3S",
    993: "IMAPS",
    5900: "VNC",
    1025: "NFS/IIS",
    587: "SMTP Submission",
    8888: "Sun Answerbook",
    199: "SNMP Multiplexer",
    1720: "H.323 Call Signaling",
    465: "SMTPS",
    548: "AFP (Apple Filing Protocol)",
    113: "IDENT",
    81: "Hosts2 Name Server",
    6001: "X11",
    10000: "SecureNet Pro",
    514: "Shell",
    5060: "SIP",
    179: "BGP",
    1026: "LSA or N-Terminal",
    2000: "Cisco SCCP",
    8443: "HTTPS Alternative",
    8000: "HTTP Alternative",
    32768: "FileNet TMS",
    554: "RTSP",
    26: "RSFTP",
    1433: "MS SQL Server",
    49152: "Ephemeral Port",
    2001: "DC",
    515: "Printer Spooler",
    8008: "IBM HTTP Server",
    49154: "Ephemeral Port",
    1027: "IIS",
    5666: "Nagios NRPE",
    646: "LDP (Label Distribution Protocol)",
    5000: "UPnP",
    5631: "PCAnywhere Data",
    631: "IPP (Internet Printing Protocol)",
    49153: "Ephemeral Port",
    8081: "Sun Proxy Admin",
    2049: "NFS",
    88: "Kerberos",
    79: "Finger",
    5800: "VNC HTTP",
    106: "POP3 Password Change",
    2121: "CCProxy FTP",
    1110: "NFS Keepalive",
    49155: "Ephemeral Port",
    6000: "X11",
    513: "Remote Login",
    990: "FTPS",
    5357: "WSDAPI",
    427: "Server Location",
    49156: "Ephemeral Port",
    543: "Kerberos Login",
    544: "Kerberos Shell",
    5101: "Talarian TCP",
    144: "NewS Window System",
    7: "Echo",
    389: "LDAP",
    8009: "AJP13",
    3128: "Squid HTTP Proxy",
    444: "Simple Network Paging Protocol",
    9999: "Abyss Web Server",
    5009: "Apple AirPort Admin",
    7070: "RealServer Streaming",
    5190: "AOL/ICQ",
    3000: "RemoteWare Client",
    5432: "PostgreSQL",
    1900: "UPnP",
    3986: "Mapper Workstation",
    13: "Daytime",
    1029: "Solid Mux Server",
    9: "Discard",
    5051: "ITA Agent",
    6646: "Unknown",
    49157: "Ephemeral Port",
    1028: "Unknown",
    873: "Rsync",
    1755: "Windows Media Services",
    2717: "PN Requester",
    4899: "Radmin",
    9100: "HP JetDirect",
    119: "NNTP",
    37: "Time Protocol"
}

def scan_port(ip, port):
    """tries to connect to the port with a slow timeout"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)  # (Like nmap --min-rate)
            result = sock.connect_ex((ip, port))
            if result == 0:
                return port
    except Exception:
        pass
    return None

def port_scan(ip):
    print(f"SCAN {ip} in {len(TOP_PORTS)} TOP PORTS ...\n")
    
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:  # THREADS
        result = executor.map(lambda p: scan_port(ip, p), TOP_PORTS.keys())

    for port in result:
        if port:
           open_ports.append(port)
    
    if open_ports:
        print("\nOPEN PORTS:")
        for p in open_ports:
            print(f" - PORT {p} ({TOP_PORTS.get(p, 'Unknown')})")
    else:
        print("\nNo open ports found")

if __name__ == "__main__":
    ip = input("Enter the IP to scan: ")
    port_scan(ip)

