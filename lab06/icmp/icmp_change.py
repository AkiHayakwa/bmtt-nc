from scapy.all import *

def modify_icmp_packet(packet):
    if packet.haslayer(ICMP):
        icmp_layer = packet[ICMP]
       
        print(f"Original ICMP Packet:")
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Type: {icmp_layer.type}")
        print(f"Code: {icmp_layer.code}")
        print(f"ID: {icmp_layer.id}")
        print(f"Sequence: {icmp_layer.seq}")
        print(f"Load: {icmp_layer.load}")
        
        new_load = b"This is a modified ICMP packet."
        new_packet = IP(src=packet[IP].dst,dst= packet[IP].src)/ICMP(type=icmp_packet.type , code = icmp_packet.code , id = icmp_packet.id , seq = icmp_packet.seq)/new_load
        print("\nModified ICMP Packet:")
        print(f"Source IP: {new_packet[IP].src}")
        print(f"Destination IP: {new_packet[IP].dst}")
        print(f"Type: {new_packet[ICMP].type}")
        print(f"Code: {new_packet[ICMP].code}")
        print(f"ID: {new_packet[ICMP].id}")
        print(f"Sequence: {new_packet[ICMP].seq}")
        print(f"Load: {new_packet[ICMP].load}")
        print("=" * 30)
        send(new_packet)
        
def main():
    sniff(prn=modify_icmp_packet, filter="icmp", store=0)
    
if __name__ == "__main__":
    main()