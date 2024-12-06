import pyshark

capture = pyshark.FileCapture('capture.pcap', display_filter='udp.dstport == 22')

source_ports = []

for packet in capture:
	try:
		source_port = int(packet.udp.srcport) - 5000
		source_ports.append(source_port)
	except AttributeError as e:
		continue

flag = ''
for number in source_ports:
	flag += chr(number)

print(flag)