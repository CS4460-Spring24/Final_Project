from scapy.all import *
from scapy.layers.all import IP, TCP, Ether, DNS, UDP, DNSQR, ARP, ICMP
from scapy.all import wrpcap
from scapy.all import fragment

# Define the flag text
flag = 'ejmCTF{tr1ceratops}'

class Campanian(Packet):
    name="Albian"
    fields_desc=[
        StrField("data", "")
    ]

    def encrypt(self, key):
        encrypted_data = ""
        print(self.data.decode('utf-8'))
        for char in self.data.decode('utf-8'):
            encrypted_char = chr(ord(char) ^ key)  # XOR encryption
            encrypted_data += encrypted_char
        self.data = encrypted_data
        print(encrypted_data)

    def decrypt(self, key):
        decrypted_data = ""
        print(self.data.decode('utf-8'))
        for char in self.data.decode('utf-8'):  # Convert data to a string before XOR decryption
            decrypted_char = chr(ord(char) ^ key)  # XOR decryption
            decrypted_data += decrypted_char
        self.data = decrypted_data
        print(decrypted_data)
class Key(Packet):
    name="key"
    fields_desc = [
        StrField("key", "key{10}")
    ]
def generate_packets(num_packets):
    packets = []
    # Craft ARP request packet
    arp_request = Ether(src= "ff:ff:ff:ff:ff:ff", dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst="192.168.1.1")
    packets.extend([arp_request] * (num_packets+2))

    # Craft UDP packet
    udp_packet = Ether() / IP(dst="192.168.1.4") / UDP(dport=12345) / Raw(b'Hello, UDP!')
    packets.extend([udp_packet] * (num_packets+1))

    # Craft ICMP packet
    icmp_packet = Ether() / IP(dst="192.168.1.3", id=121) / ICMP() / Raw(load='false flag')
    fragments = fragment(icmp_packet, fragsize=12)
    packets.extend(fragments)
    
    # Craft DNS query packet
    dns_query = Ether() / IP(dst="8.8.8.8") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="example.com"))
    packets.extend([dns_query] * (num_packets-1))
    
    # Intersperse ICMP packet fragments with CTF flag among other packets
    for _ in range(10):  # Number of times to intersperse
        # Craft random TCP packet
        tcp_packet = Ether() / IP(dst="192.168.1.2") / TCP(dport=80) / Raw(load="Random TCP payload")
        packets.extend([tcp_packet] * num_packets)

        # Craft ICMP packet
        icmp_packet = Ether() / IP(dst="192.168.1.3", id=123+_) / ICMP() / b'false flag'
        o_fragments = fragment(icmp_packet, fragsize=12)
        packets.extend(o_fragments)

        # Craft random UDP packet
        udp_packet = Ether() / IP(dst="192.168.1.4") / UDP(dport=12345) / Raw(b'Random UDP payload')
        packets.extend([udp_packet] * num_packets)
        
        # Craft random DNS query packet
        dns_query = Ether() / IP(dst="8.8.8.8") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="example.com"))
        packets.extend([dns_query] * num_packets)
        
        # Craft random ARP request packet
        arp_request = Ether(src= "ff:ff:ff:ff:ff:ff", dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst="192.168.1.1")
        packets.extend([arp_request] * num_packets)
    
    packet = Campanian(data=flag)
    bind_layers(Ether, Campanian, type=0x1234)
    packet.encrypt(0x0a)
    packets.append(Ether(type=0x1234)/packet/DNS(rd=1, qd=DNSQR(qname="key={10}")))
    packet.decrypt(0x0a)
    for _ in range(10):  # Number of times to intersperse
        # Craft random TCP packet
        tcp_packet = Ether() / IP(dst="192.168.1.2") / TCP(dport=80) / Raw(load="Random TCP payload")
        packets.extend([tcp_packet] * num_packets)
        
        # Craft random UDP packet
        udp_packet = Ether() / IP(dst="192.168.1.4") / UDP(dport=12345) / Raw(b'Random UDP payload')
        packets.extend([udp_packet] * num_packets)
        
        # Craft random DNS query packet
        dns_query = Ether() / IP(dst="8.8.8.8") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="example.com"))
        packets.extend([dns_query] * num_packets)
        
        # Craft random ARP request packet
        arp_request = Ether(src= "ff:ff:ff:ff:ff:ff", dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst="192.168.1.1")
        packets.extend([arp_request] * num_packets)
        # Craft ICMP packet
        icmp_packet = Ether() / IP(dst="192.168.1.3", id=134+_) / ICMP() / b'false flag'
        o_fragments = fragment(icmp_packet, fragsize=8)
        packets.extend(o_fragments)
    # Craft ICMP packet
    icmp_packet = Ether() / IP(dst="192.168.1.3", id=145) / ICMP() / b'false flag'
    o_fragments = fragment(icmp_packet, fragsize=8)
    packets.extend(o_fragments)
    
    return packets

# Generate packets
num_packets = 20
packets = generate_packets(num_packets)

# Write the packets to a pcap file
wrpcap("ctf_capture3.pcap", packets)
