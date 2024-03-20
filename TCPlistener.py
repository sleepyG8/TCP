import socket

def listen_for_reverse_tcp(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", port))
        server_socket.listen(1)
        print(f"Listening on port {port}...")

        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address[0]}:{client_address[1]}")

        while True:
            command = client_socket.recv(1024).decode()
            if 'exit' in command:
                print("Received 'exit' command. Closing connection.")
                break
            # Handle other commands as needed

        # Close the connection
        client_socket.close()
        server_socket.close()

    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    listen_for_reverse_tcp(1234)
