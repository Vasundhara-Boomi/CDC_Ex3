import socket
import threading

# Client function to handle communication with the server
def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    server_port = 9999
    
    client.connect((server_ip, server_port))
    print("Connected to server")
    
    def receive_messages():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"Message from server: {message}")
            except:
                print("Connection to server lost.")
                break
    
    def send_messages():
        while True:
            message = input("Client: ")
            if message.lower() == 'exit':
                client.close()
                break
            client.send(message.encode('utf-8'))
            print("Message sent to server.")

    # Create threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)
    
    receive_thread.start()
    send_thread.start()
    
    receive_thread.join()
    send_thread.join()

if __name__ == "__main__":
    client_program()
