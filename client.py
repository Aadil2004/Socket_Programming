import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 6000
CLIENT_NAME = "Client of Aa’dil Khamis Ngangila"

def main():
    client_number = int(input("Enter an integer between 1 and 100: "))

    # Create TCP socket using IPv4 and TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to all interfaces on chosen port
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    message = f"{CLIENT_NAME}|{client_number}"
    client_socket.send(message.encode())
    print("[CLIENT] Message sent to server.")

    reply = client_socket.recv(1024).decode()
    print(f"[CLIENT] Reply received: {reply}")

    server_name, server_number = reply.split("|")
    server_number = int(server_number)

    total = client_number + server_number

    print(f"[CLIENT] Client Name: {CLIENT_NAME}")
    print(f"[CLIENT] Server Name: {server_name}")
    print(f"[CLIENT] Client Number: {client_number}")
    print(f"[CLIENT] Server Number: {server_number}")
    print(f"[CLIENT] Sum: {total}")

    #End the connections
    client_socket.close()
    print("[CLIENT] Connection closed.")

if __name__ == "__main__":
    main()