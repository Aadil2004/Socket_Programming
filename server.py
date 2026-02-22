import socket

SERVER_NAME = "Server of Aa’dil Khamis Ngangila"
SERVER_PORT = 6000  
SERVER_HOST = "127.0.0.1"

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)

    print(f"[SERVER] {SERVER_NAME} is running on port {SERVER_PORT}...")
    
    while True:
        print("[SERVER] Waiting for client connection...")
        connection_socket, addr = server_socket.accept()
        print(f"[SERVER] Connection established with {addr}")

        message = connection_socket.recv(1024).decode()
        print(f"[SERVER] Message received: {message}")

        try:
            client_name, client_number = message.split("|")
            client_number = int(client_number)

            if client_number < 1 or client_number > 100:
                print("[SERVER] Client sent invalid number. Shutting down server.")
                connection_socket.close()
                server_socket.close()
                break

            server_number = 50  
            total = client_number + server_number

            print(f"[SERVER] Client Name: {client_name}")
            print(f"[SERVER] Server Name: {SERVER_NAME}")
            print(f"[SERVER] Client Number: {client_number}")
            print(f"[SERVER] Server Number: {server_number}")
            print(f"[SERVER] Sum: {total}")

            reply = f"{SERVER_NAME}|{server_number}"
            connection_socket.send(reply.encode())
            print("[SERVER] Reply sent to client.")

        except Exception as e:
            print("[SERVER] Error processing request:", e)

        connection_socket.close()
        print("[SERVER] Connection closed.\n")

if __name__ == "__main__":
    main()