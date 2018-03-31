import socket
import sys
import threading
import subprocess
def SendRecv(connection, client_address):
    try:
        print('connection from, connection is', client_address, connection)
        # Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(30)
			print('received "%s"' % data)
			cmd=data.split(" ")
			if data:
				print('sending data back to the client')
				data=subprocess.check_output(tuple(cmd))
				connection.sendall(str(len(data))+"@"+data)
			else:
				print("no more data from", client_address)
				break  
    finally:
        # Clean up the connection
        connection.close()
def main():

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Bind the socket to the port
	port_num = input("Enter port number:")
	server_address = ('localhost', port_num)
	print('starting up on %s port %s'%server_address)
	sock.bind(server_address)
	sock.listen(5)

	#while True:
	# Wait for a connection
	print('waiting for a connection')
	connection, client_address = sock.accept()
	t1 = threading.Thread(target=SendRecv, args=(connection,client_address))
	t1.start()
if __name__=="__main__":
	main()
