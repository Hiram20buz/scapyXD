from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        print(f"Received packet from source IP: {packet[IP].src}")

# Start sniffing packets on the specified network interface
# Replace 'eth0' with 'en0'
sniff(iface="en0", filter="ip", prn=packet_callback)

