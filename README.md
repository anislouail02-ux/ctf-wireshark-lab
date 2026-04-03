# CTF Wireshark Lab by anis

A beginner-friendly CTF challenge built on Kali Linux simulating
a basic data exfiltration scenario using packet analysis.

## Scenario
An employee was sending suspicious HTTP requests to an unknown
server. Analyze the traffic and recover the hidden data.

## Tools Used
- Kali Linux
- Python 3 + Scapy
- Wireshark

## How to Run
1. Generate the challenge pcap:
   sudo python3 generate_traffic.py

2. Open in Wireshark:
   wireshark challenge.pcap

3. Filter suspicious traffic:
   ip.dst == 10.10.10.99

4. Follow TCP Stream and look for the X-Data header

5. Decode the Base64 value in terminal:
   echo "<base64_value>" | base64 -d

