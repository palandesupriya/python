TCP - It is connection oriented hence what we send is sent is the same order.
		For eg if "Hi" and then "bye" is sent then they are received in same order,
		that is,first "Hi" will reach destination and then "bye"
UDP - Packet are sent irrespective of whether anyone receives it or not.
		It is connectionless.
Socket - it is nothing but a file hence it has return value as a descriptor.
		Difference between pipe and socket is pipe is on local machine but socket is
		between two or more machine.
		SOC_STREAM is for TCP connection
		SOC_DGRAM is for UDP connection
		AF_UNIX - local domain socket
		AF_INET - internet socket
		
Handshaking : 
server			client
-socket			-socket
-bind			-connect
-listen
-accept
