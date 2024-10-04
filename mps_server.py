import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connection established with {client_address}")
    
    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"Message from {client_address}: {message}")
            except:
                print(f"Connection lost with {client_address}")
                break
    
    def send_messages():
        while True:
            message = input("Server: ")
            if message.lower() == 'exit':
                client_socket.close()
                break
            client_socket.send(message.encode('utf-8'))
            print("Message sent to client.")

    # Create threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))  # Binds to all available interfaces
    server.listen(5)
    print("Server started, waiting for connections...")
    
    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
