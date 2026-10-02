import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 5000

cliente.connect((HOST, PORT))

peso = float(input("Digite o peso do paciente em kg: "))
altura = float(input("Digite a altura do paciente em metros: "))

dados = f"Peso: {peso}; Altura: {altura}"
cliente.send(dados.encode())

resposta = cliente.recv(1024).decode()

print(f"Resposta do servidor: {resposta}")

cliente.close()