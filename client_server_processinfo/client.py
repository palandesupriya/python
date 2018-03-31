import socket
import sys
import string
import threading
import time
class ServerInfo(threading.Thread):
	def __init__(self,ip="localhost",port=10004,command="ps",output_file="server1.txt"):
		super.__init__(self)
		self.ip=ip
		self.port=port
		self.command=command
		self.output_file=output_file
		# Create a TCP/IP socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		# Connect the socket to the port where the server is listening
		server_address = (self.ip,self.port)
		print('connecting to %s port %s' % server_address)
		self.sock.connect(server_address)

	def __del__(self):
		print('closing socket')
		self.sock.close()
		
	def run(self):
		try:
			fd=open(self.output_file,"w")
			cnt =5
			while cnt>0:
				#sock.send(bytes(message, 'UTF-8')) # 3 & above
				self.sock.sendall(self.command) # 2.7			
				data = self.sock.recv(50)
				splitData=data.split("@")
				amount_received = len(splitData[1])
				amount_expected = int(splitData[0])
				data=splitData[1]
				while amount_received < amount_expected:
					fd.write( data)
					data = self.sock.recv(50)
					amount_received+=len(data)
				fd.write("\n\n")
				cnt-=1
				time.sleep(10)
		finally:
			fd.close()

def Open(config_file_name):
	fd = open(config_file_name)
	# validate configuration file if any
	return fd
	
def ParseConfig(config_file_handle):
	result = {}
	line = " "
	if config_file_handle != None:
		
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
	
	config_file_handle = Open(config_file_name)
	configurations = ParseSections(config_file_handle)
	config_file_handle.close()	
	return configurations

def main():
	dctIP = {}
	dctPort = {}
	command = ""
	output_file=""
	FileData = GetInfo("config.conf")
	obj = []
	for key in FileData:
		dctServerInfo = FileData[key]
		for subkey in dctServerInfo:
			if subkey == "ip":
				dctIP = dctServerInfo[subkey]
			elif subkey == "port":
				dctPort = dctServerInfo[subkey]
			elif subkey == "status_command":
				command = dctServerInfo[subkey]
			else:
				output_file=dctServerInfo[subkey]
		obj = ServerInfo(dctIP, int(dctPort), command, output_file)
		obj.start()

if __name__ == '__main__':
	main()
