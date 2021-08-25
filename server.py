import socket
import asyncio

HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'


def run_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 8000))

        server.listen(4)

        active_users = set() # set of connected users
        cid = 0
        print('Working...')
        while True:
            
            client = accept_client_connection(server, cid) # accept connection with client, print state of connection
            request = client.recv(1024).decode('utf-8') # receive requests from client in utf-8
            
            content = load_page(request)
            client.send(content)
            client.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
    print('Shutdown...')

def accept_client_connection(server_socket, cid):
    client, address = server_socket.accept()
    print(f"Client {cid} has been connected :: {address[0]} {address[1]}")
    return client

def load_page(request_data):
    
    path = request_data.split(' ')[1]
    print(path)
    response = ''
    try:
        with open(f'views{path}', 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return(HDRS_404 + 'Not found!').encode('utf-8')


if __name__ == '__main__':
    main_loop = asyncio.new_event_loop()
    run_server()
    