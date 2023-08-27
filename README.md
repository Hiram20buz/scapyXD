# scapyXD
Packet manipulation tool

pip install scapy


sudo python port_scanner.py -t 192.168.0.17 -s syn -p 22

python port_scanner.py -t "target ip" -s "type of scan" -p "ports to scan"


### Certainly! When using the sniff function in Scapy, you need to specify the network interface on which you want to capture packets. You would replace "eth0" with the actual name of your network interface. Here's how you can find the name of your network interface:

# Linux:

Open a terminal and run the ifconfig command. Look for the interface with your active IP address. The interface name will be listed there. It's usually named something like eth0, eth1, wlan0, etc.

# macOS:

Open a terminal and run the ifconfig command or the networksetup -listallhardwareports command. You will find the network interface name listed under the "Hardware Port" for your active connection.

# Windows:

Open a command prompt and run the ipconfig command. Look for the network interface with your active IP address. The interface name will be listed there.
