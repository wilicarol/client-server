import socket

def start_client():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    for _ in range(3):
        question_data = client_socket.recv(1024).decode()
        print("\n" + question_data)

        user_input = input("Digite sua resposta: ").strip()
        client_socket.sendall(user_input.encode())

    result_message = client_socket.recv(1024).decode()
    print("\n" + result_message)

    client_socket.close()

if __name__ == "__main__":
    start_client()
