import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 5000

servidor.bind((HOST, PORT))
servidor.listen()

print("Servidor aguardando conexões...")

conexao, endereco = servidor.accept()
print(f"Conexão estabelecida com {endereco}")

print("Cliente conectado:", endereco)

dados = conexao.recv(1024).decode()
print("Dados recebidos:", dados)

peso, altura = dados.split(";")

peso = float(peso.replace("Peso: ", ""))
altura = float(altura.replace(" Altura: ", ""))

imc = peso / (altura * altura)

print(f"O IMC do paciente é: {imc:.2f}")

if imc < 25:
    classificacao = "Magro"
    print("Classificação: Magro")
else:
    classificacao = "Gordo"
    print("Classificação: Gordo")

resposta = f"IMC: {imc:.2f};\nClassificação: {classificacao}"

conexao.send(resposta.encode())