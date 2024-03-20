import socket
import subprocess

def connect():
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port number: "))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))

    while True:
        command = input("Enter a command: ")  # Get user input
        s.send(command.encode())  # Send the command
        output = s.recv(1024).decode()  # Receive the output
        print(output)  # Print the output

    s.close()

if __name__ == "__main__":
    connect()

