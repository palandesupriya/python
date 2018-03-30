import socket
import sys
import string
import threading

def Open(config_file_name):
	fd = open(config_file_name)
	# validate configuration file if any
	return fd
	
def ParseConfig(config_file_handle):
	result = {}
	line = " "
	if config_file_handle != None:
		print line
		while line != "":
			line = config_file_handle.readline()
			if line.startswith('['):
				break
			if not line.startswith("#") and "=" in line:
				config_option = line.split("=")
				#print config_option
				if "#" in config_option[1]:
					config_option[1] = config_option[1].split("#")[0]
				result[config_option[0]] = config_option[1][0:-1]
	print result, line
	return result, line

def ParseSections(config_file_handle):
	result = {}
	if config_file_handle != None:
		line = " "
		while line != "":
			#print line
			if line.startswith('['):
				key = line[1:line.index(']')]
				#print key
				dic, line = ParseConfig(config_file_handle)
				result[key] = dic
				#print result
				continue    
			line = config_file_handle.readline()
	return result        
	
def GetInfo(config_file_name):
	#config_file_name = configfilename
	#input("Enter Name of Configuration File:")
	config_file_handle = Open(config_file_name)
	configurations = ParseSections(config_file_handle)
	config_file_handle.close()
	for key in configurations:
		print key,"=", configurations[key]
	return configurations
	
class Process_Thread(threading.Thread):

	def __init__(self, ip, port, msg):
		super(Process_Thread, self).__init__()
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
			print('client {} is sending {}'.format(self.ip, self.msg))
			while 1:
				sock.sendall(self.msg)
				while True:
					data = sock.recv(1024)
					if not data:
						break
					print('"%s"' % data)
		finally:
			print("Closing connection for client:{}".format(self.ip))
			sock.close()
			return
def main():
	dctIP = {}
	dctPort = {}
	msg = {}
	FileData = GetInfo("config.conf")
	obj = []
	for key in FileData:
		dctServerInfo = FileData[key]
		for subkey in dctServerInfo:
			if subkey == "ip":
				dctIP = dctServerInfo[subkey]
			elif subkey == "port":
				dctPort = dctServerInfo[subkey]
			else:
				msg = dctServerInfo[subkey]
		obj = Process_Thread(dctIP, int(dctPort), msg)
		obj.start()
		obj.join()
		
if __name__ == '__main__':
	main()
