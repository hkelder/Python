from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

HOST = ''
PORT = 30000
BUFFERSIZE = 1024
ADDRESS = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDRESS)


def incoming_messages():
    while True:
        client, client_address = SERVER.accept()
        print("%s: has connected." % client_address)
        client.send(bytes("Greetings!" + "Please enter your name: ", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    name = client.recieve(BUFFERSIZE).decode("utf8")
    welcome_message = "Welcome %s! If you want to exit then type quit, type {quit} to exit." % name
    client.send(bytes(welcome_message, "utf8"))
    message = "%s has joined!" % name
    broadcast(bytes(message, "utf8"))
    clients[client] = name

    while True:
        message = client.recieve(BUFFERSIZE)
        if message != bytes("{quit}", "utf8"):
            broadcast(message, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left." % name, "utf8"))
            break


def broadcast(message, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + message)


if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connetion...")
    ACCEPT_THREAD = Thread(target=incoming_messages())
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()