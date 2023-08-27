from scapy.all import sniff, IP

# Define the IP address you want to filter
target_ip = "192.168.0.15"  # Replace with the actual IP

def packet_callback(packet):
    if IP in packet and packet[IP].src == target_ip:
        print(f"Received packet from source IP: {packet[IP].src}")

# Start sniffing packets on the specified network interface
# Replace 'eth0' with 'en0'
sniff(iface="en0", filter="ip", prn=packet_callback)

