from scapy.all import * 

def packet_callback(packet):
    if packet.haslayer(ICMP):
        icmp_layer = packet[ICMP]   
        print(f"ICMP Packet Information")
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Type: {icmp_layer.type}")
        print(f"Code: {icmp_layer.code}")
        print(f"ID: {icmp_layer.id}")
        print(f"Sequence: {icmp_layer.seq}")
        print(f"Load:{icmp_layer.load}")
        print("-" * 30)
        
def main():
    sniff(prn=packet_callback, filter="icmp", store=0)
    
if __name__ == "__main__":
    main()
