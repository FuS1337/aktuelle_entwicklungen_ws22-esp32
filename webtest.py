try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import gc
gc.collect()
 
def web(text):
   html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
.button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1></body></html>"""
   print(html)
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.bind(('', 80))
   s.listen(5)
   while True:
     conn, addr = s.accept()
     print('Got a connection from %s' % str(addr))
     conn.sendall(html)
     conn.close()
