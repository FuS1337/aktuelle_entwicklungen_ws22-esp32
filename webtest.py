try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import time
import gc
import binascii

gc.collect()
 
def web_page(text):
    html = """<!doctype html><html><head> <title>ESP Web Server</title> <meta name="viewport/"></head><body> <h1>ESP Web Server</h1><a>Hauptfarbe des Bildes (Rot, Gruen, Blau, weder noch): """ + text + """</a></body></html>"""
    return html
 
def web(text):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.bind(('', 80))
   s.listen(5)
   while True:
     conn, addr = s.accept()
     print('Got a connection from %s' % str(addr))
     request = conn.recv(1024)
     request = str(request)
     print("-----------------------------------------------------")
     print('Content = %s' % request)
     print("-----------------------------------------------------")
     response = web_page(text)
     conn.send('HTTP/1.1 200 OK\n')
     conn.send('Content-Type: text/html\n')
     conn.send('Connection: close\n\n')
     conn.sendall(response)
     conn.close()
