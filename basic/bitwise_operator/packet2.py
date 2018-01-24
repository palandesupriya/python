'''

CRC=3bits
Length=7bits
Data=16bits
Flag=2Bits
Protocol-type=4bits

Need to perform packetization & depaketization.
'''
def Packet(crc, len, data, flag, protocol):
	pack = 0
	crc = ((1<<3)-1) & crc;
	len = ((1<<7)-1) & len;
	data = ((1<<16)-1) & data;
	flag = ((1<<2)-1) & flag;
	protocol = ((1<<4)-1) & protocol;
	pack = (pack | crc)<<7;
	pack = (pack | len)<<16;
	pack = (pack | data)<<2;
	pack = (pack | flag)<<4;
	pack = (pack | protocol);
	return pack

def Depacketisation(pack):
	protocol = ((1<<4)-1) & pack;
	pack >>= 4;
	flag = ((1<<2)-1) & pack;
	pack >>= 2;
	data = ((1<<16)-1) & pack;
	pack >>= 16;
	len = ((1<<7)-1) & pack;
	pack >>= 7;
	crc = ((1<<3)-1) & pack;
	pack >>= 3;
	return crc,len,data,flag,protocol
	
def main():
	crc, len, data, flag, protocol = input("Enter crc, len, data, flag, protocol:")
	packet = Packet(crc, len, data, flag, protocol)
	print("Packet is : {}".format(packet))
	print("\n\nDepackatising :")
	crc, len, data, flag, protocol = Depacketisation(packet)
	print("CRC = {}\nLEN = {}\nDATA = {}\nFLAG = {}\nPROTOCOL = {}".format(crc,len,data,flag,protocol))
	
if __name__ == '__main__':
	main()