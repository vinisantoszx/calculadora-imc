import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "0.0.0.0" ## IP do pc servidor
PORT = 5000 ## Porta que vamos utilizar para a comunicação

servidor.bind((HOST, PORT)) ## Associa o socket a um endereço e porta específicos
servidor.listen() ## Coloca o socket em modo de escuta, aguardando conexões de clientes

print("Servidor aguardando conexões...")

conexao, endereco = servidor.accept() ## Aceita a conexão de um cliente e retorna um novo socket para comunicação e o endereço do cliente
print(f"Conexão estabelecida com {endereco}")

print("Cliente conectado:", endereco) ## Imprime o endereço do cliente conectado

dados = conexao.recv(1024).decode() ## Recebe os dados do cliente
print("Dados recebidos:", dados) ## Imprime os dados recebidos do cliente

peso, altura = dados.split(";") ## Divide a string de dados em duas partes, separadas pelo ponto e vírgula, e atribui cada parte a uma variável

peso = float(peso.replace("Peso: ", "")) ## Remove a parte "Peso: " da string e converte para float
altura = float(altura.replace(" Altura: ", "")) ## Remove a parte " Altura: " da string e converte para float

imc = peso / (altura * altura)

print(f"O IMC do paciente é: {imc:.2f}")

if imc < 25: ## Condicional para verificar o IMC
    classificacao = "Magro"
    print("Classificação: Magro")
else:
    classificacao = "Gordo"
    print("Classificação: Gordo")

resposta = f"IMC: {imc:.2f};\nClassificação: {classificacao}" ## Variável para armazenar a resposta do servidor em uma string formatada

conexao.send(resposta.encode()) ## Envia a resposta para o cliente