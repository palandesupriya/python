'''
Server side code:
	Take input command send by client and return response.
'''
import subprocess
import socket
import sys
def main():
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Bind the socket to the port
	server_address = ('localhost', 10003)
	print('starting up on %s port %s'%server_address)
	sock.bind(server_address)
	sock.listen(1)

	while True:
		# Wait for a connection
		print('waiting for a connection')
		connection, client_address = sock.accept()
		try:
			print('connection from {}, connection is {}'.format(client_address, connection))
			data = connection.recv(1024)
			print('received "%s"' % data)
			if data:
				print('sending data back to the client')
				output = subprocess.check_output(data, shell = True)
				connection.sendall(output)
			else:
				print("no more data from", client_address)
				break
		finally:
			# Clean up the connection
			connection.close()

if __name__ == '__main__':
	main()
