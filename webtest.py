import camerafunctions
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import gc

gc.collect()

# Funktion um Html für die Website zu generieren
#   text          - String der auf der Website dargestellt werden soll
#   farberkennung - Boolean, ob Farberkennung genutzt werden soll (Alternative Hell-Dunkel-Erkennung)
def web_page(text,farberkennung):
    html = ""
    if farberkennung:
        html = """<!doctype html><html><head> <title>ESP Web Server</title> <meta name="viewport/"></head><body> <h1>ESP Web Server</h1><a>""" + text + camerafunctions.whatIsTheMainColor() +"""</a></body></html>"""
    else:
        html = """<!doctype html><html><head> <title>ESP Web Server</title> <meta name="viewport/"></head><body> <h1>ESP Web Server</h1><a>""" + text + camerafunctions.isItLightOrDark() +"""</a></body></html>"""
    return html

# Webserver für die Kamerafunktionen
#   text          - String der auf der Website dargestellt werden soll
#   farberkennung - Boolean, ob Farberkennung genutzt werden soll (Alternative Hell-Dunkel-Erkennung)
def web(text, farberkennung):
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
     response = web_page(text, farberkennung)
     conn.send('HTTP/1.1 200 OK\n')
     conn.send('Content-Type: text/html\n')
     conn.send('Connection: close\n\n')
     conn.sendall(response)
     conn.close()


