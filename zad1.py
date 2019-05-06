import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.bind((HOST, PORT))
   s.listen()
   conn, addr = s.accept()
   print('Connected by', addr)
   try:
       conn.sendall(bytes('to wysyła serwer', 'utf-8'))
       data = conn.recv(1024)
       data = data.decode('utf-8')
       print(data)
   finally:
       conn.close()
finally:
   s.close()
