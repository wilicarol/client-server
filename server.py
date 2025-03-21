import socket

# Questões corrigidas
questions = [
    ("Qual filme ganhou o Oscar de Melhor Filme Internacional em 2025?",
     ["Tudo em Todo Lugar ao Mesmo Tempo", "Avatar: O Caminho da Água", "Ainda Estou Aqui", "Top Gun: Maverick"],
     "Ainda Estou Aqui"),

    ("Qual destas bibliotecas do Python é mais utilizada para análise de dados?", 
     ["TensorFlow", "NumPy", "Pandas", "Matplotlib"], 
     "Pandas"),

    ("Qual jogadora brasileira é conhecida como a Rainha do Futebol?", 
     ["Cristiane", "Marta", "Formiga", "Debinha"], 
     "Marta")
]

def start_server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor aguardando conexão na porta {port}...")
    conn, addr = server_socket.accept()
    print(f"Cliente conectado: {addr}")

    score = 0  
    results = []  

    for question, options, correct_answer in questions:
        # Envia a pergunta e as opções para o cliente
        question_data = f"{question}\n" + "\n".join(f"{i+1}. {option}" for i, option in enumerate(options))
        conn.sendall(question_data.encode())

        while True:
            client_answer = conn.recv(1024).decode().strip()

            # Verifica se a entrada do usuário é válida
            if client_answer.isdigit():
                index = int(client_answer) - 1
                if 0 <= index < len(options):
                    user_choice = options[index]
                    break
            conn.sendall("Resposta inválida. Escolha um número entre 1 e 4.".encode())

        # Verifica se a resposta está correta
        if user_choice.lower() == correct_answer.lower():
            score += 1
            results.append(f"✔ {question} - Resposta correta: {correct_answer}")
        else:
            results.append(f"✘ {question} - Resposta correta: {correct_answer}")

    # Envia o resultado final para o cliente
    result_message = f"Você acertou {score}/{len(questions)} questões!\n" + "\n".join(results)
    conn.sendall(result_message.encode())

    conn.close()
    server_socket.close()
    print("Servidor encerrado.")

if __name__ == "__main__":
    start_server()
