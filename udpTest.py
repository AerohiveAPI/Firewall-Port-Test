import socket#for sockets
import sys#for exit
import array

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = 'redirector.aerohive.com'
port = 12222


message = "70408000000000000000012c040045000009f61900001f4000380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
hexMessage = bytearray(message.decode("hex")) #.decode("hex");


try :
        #Set the whole string
    s.sendto(hexMessage, (host, port))

    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    reply = d[0]
    addr = d[1]

    print 'Server reply : ' + reply

except socket.error, msg:
    print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
