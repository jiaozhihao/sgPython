import socket

def checkport(address):
	s= socket.socket()
	port=0
	while port<=1024:
		port=port+1
#		print(port)
#		if port>=1024:
#			break
		try:
			s.connect((address,port))
			print('connected')
#			return True
		except socket.error:
			print("canot connect {}".format(port))
#			return False


checkport('127.0.0.1')
