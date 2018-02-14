'''
Read rtp(wikipe) packet format and de-packetize it.
BITS  - 0 1	| 2 | 3	| 4 5	6 7 | 8 | 9 10	11 12 13 14	15 | 16 17 18	19 20 21 22	23 24 25 26	27 28 29 30 31
FIELD - Ver	| P | X	| CC	    | M | PT	               | Sequence Number
'''
def depacketise(rttpack):
	ver = ((1<<2)-1) & rttpack
	rttpack >>= 2
	padding = ((1<<1)-1) & rttpack
	rttpack >>= 1
	xtension = ((1<<1)-1) & rttpack
	rttpack >>= 1
	cc = ((1<<4)-1) & rttpack
	rttpack >>= 4
	marker = ((1<<1)-1) & rttpack
	rttpack >>= 1
	paddingtype = ((1<<7)-1) & rttpack
	rttpack >>= 7
	seqnum = ((1<<16)-1) & rttpack
	rttpack >>= 16
	return ver, padding, xtension, cc, marker, paddingtype, seqnum
def main():
	pack = input("Enter RTTP packet:")
	ver, padding, xtension, cc, marker, paddingtype, seqnum = depacketise(pack)
	print ver, padding, xtension, cc, marker, paddingtype, seqnum
if __name__ == '__main__':
	main()