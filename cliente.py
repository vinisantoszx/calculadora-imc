import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "192.168.0.7" ## IP do pc servidor
PORT = 5000 ## Porta que vamos utilizar para a comunicação

cliente.connect((HOST, PORT))

peso = float(input("Digite o peso do paciente em kg: ")) ## Variável para armazenar o peso do paciente
altura = float(input("Digite a altura do paciente em metros: ")) ## Variável para armazenar a altura do paciente

dados = f"Peso: {peso}; Altura: {altura}" ## Variável para armazenar os dados do paciente em uma string formatada
cliente.send(dados.encode()) ## Envia os dados para o servidor

resposta = cliente.recv(1024).decode() ## Recebe a resposta do servidor

print(f"Resposta do servidor: {resposta}") ## Imprime a resposta do servidor na tela

cliente.close() ## Fecha a conexão com o servidor