from scapy.all import *
import base64

FLAG = "CTF{Anis_was_here}"
flag_encoded = base64.b64encode(FLAG.encode()).decode()

packets = []

# --- Normal traffic (decoy) ---
for i in range(5):
    pkt = (IP(src="192.168.1.10", dst="93.184.216.34") /
           TCP(dport=80, flags="S") /
           Raw(load=f"GET /page{i} HTTP/1.1\r\nHost: example.com\r\n\r\n"))
    packets.append(pkt)

# --- Suspicious packet with hidden flag ---
sus_pkt = (IP(src="192.168.1.10", dst="10.10.10.99") /
           TCP(dport=80, flags="S") /
           Raw(load=f"GET /upload HTTP/1.1\r\n"
                    f"Host: unknown-server.net\r\n"
                    f"X-Data: {flag_encoded}\r\n\r\n"))
packets.append(sus_pkt)

# --- More decoy traffic ---
for i in range(4):
    pkt = (IP(src="192.168.1.10", dst="93.184.216.34") /
           TCP(dport=80, flags="S") /
           Raw(load=f"GET /home HTTP/1.1\r\nHost: example.com\r\n\r\n"))
    packets.append(pkt)

wrpcap("challenge.pcap", packets)
print("[+] challenge.pcap ready!")
print(f"[+] Encoded flag: {flag_encoded}")
