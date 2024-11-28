from scapy.all import *

# Define the filter parameter
target_ip = "127.0.0.1"  # Change to the target IP address
target_port = 3836 

# Define a function to process each packet
def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        # Check if the source or destination IP matches the target IP
        if ip_layer.src == target_ip or ip_layer.dst == target_ip:
            
            print(f"Captured packet: {ip_layer.src}:{packet.sport} -> {ip_layer.dst}:{packet.dport}, Size: {len(packet)} bytes")

# Start sniffing the packets

sniff(filter=f"ip and (tcp port {target_port} or udp port {target_port})", prn=packet_callback, store=0, iface = "Software Loopback Interface 1" ,timeout = 20)

#sniff(filter=f"ip host {target_ip}", prn=packet_callback, store=0, iface = "Software Loopback Interface 1" ,timeout = 5)