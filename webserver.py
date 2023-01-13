import gc

try:
    import usocket as socket
except ImportError:
    import socket

gc.collect()


def web_page(text, result_function):
    """ Funktion um das Html für die Website zu generieren.

    :param text: String der auf der Website dargestellt werden soll
    :type: str
    :param result_function: Funktion zum Berechnen eines Wertes, der angezeigt werden soll
    :type: function
    :return: HTML-String
    """

    value = result_function()
    print(f"Calculated Value: {value}.")

    return f"""
    <!doctype html>
    <html>
        <head>
            <title>ESP Web Server</title>
            <meta charset="ISO-8859-1"> 
            <meta name="viewport/">
        </head>
        <body>
            <h1>ESP Web Server</h1>
            <h2>
                {text}
                <span style="">{value}</span>
            </h2>
        </body>
    </html>
    """


def start_webserver(text, result_function):
    """ Webserver-Loop für die Kamerafunktionen.

    :param text: String der auf der Website dargestellt werden soll
    :type: str
    :param result_function: Funktion zum Berechnen eines Wertes, der angezeigt werden soll
    :type: function
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print(f'Got a connection from {str(addr)}')
        request = conn.recv(1024)
        request = str(request)
        # print("-----------------------------------------------------")
        # print(f'Content = {request}')
        # print("-----------------------------------------------------")
        response = web_page(text, result_function)
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

