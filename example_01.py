import socket
from select import select

to_monitor = []

serer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serer_socket.bind(('localhost', 5000))
serer_socket.listen()


def accept_connection(server_socket):
    client_socket, addr = serer_socket.accept()
    print('Connection from', addr)
    to_monitor.append(client_socket)


def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        responce = 'Hello world\n'.encode()
        client_socket.send(responce)
    else:
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])


        for sock in ready_to_read:
            if sock is serer_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(serer_socket)
    event_loop()