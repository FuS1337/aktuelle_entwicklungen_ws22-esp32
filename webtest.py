try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import gc
gc.collect()
 
def web(text):
   html = """<!doctype html><html><head> <title>ESP Web Server</title> <meta name="viewport"></head><body> <h1>ESP Web Server</h1></body></html>"""
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.bind(('', 80))
   s.listen(5)
   while True:
     conn, addr = s.accept()
     print('Got a connection from %s' % str(addr))
     conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
     conn.send(html)
     conn.close()
