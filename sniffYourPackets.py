from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        print(f"Received packet from source IP: {packet[IP].src}")

# Start sniffing packets on the specified network interface
# Change 'eth0' to your actual network interface name
sniff(iface="eth0", filter="ip", prn=packet_callback)

