import socket
import sys
import string
import threading

class Process_Thread(threading.Thread):
	def __init__(ip, port, msg):
		self.ip = ip
		self.port = port
		self.msg = msg
		
	def run(self):
		# Create a TCP/IP socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Connect the socket to the port where the server is listening
		server_address = (self.ip, self.port)
		print('connecting to %s port %s' % server_address)
		sock.connect(server_address)

		try:
			# Send data
			print('sending "%s"' % self.msg)
			while 1:
				sock.sendall(self.msg)
				while True:
					data = sock.recv(1024)
					if not data:
						break
					print('received "%s"' % data)
		finally:
			sock.close()
			return
def main():
	dctIP = ["localhost", "localhost", "localhost"]
	dctPort = ["10003", "10004", "10005"]
	msg = "dir"
	for i in range(len(dctPort)):
		obj[i] = Process_Thread(dctIP[i], dctPort[i], msg)
		obj[i].start()
	
if __name__ == '__main__':
	main()
