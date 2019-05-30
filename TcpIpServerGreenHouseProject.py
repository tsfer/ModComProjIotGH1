import socket

def Main():
    host = '127.0.0.1'
    port = 6666

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print "Conexão de  " + str(addr)

    while True:
        data = c.recv(1024)
        if not data:
            print("Falha de conexão \n nenhum dado não recebido")
            break
        #Parte para comfirmar o recebimento de dados, coloquei repetir os dados pra saber se deu certin
        print "Recebido do programa cliente: " + str(data)

        #processamento vai aqui.. o server tem que executar 2 tarefas:
        #1) Passar os dados dos sensores para o SO
        #2) Receber e salvar os comandos do SO e enviar para o microcontrolador

        data1=data
        data1=5+4

        #fim do processamento

        #envio dos dados processados
        print "sending: " + str(data)
        c.send(data)

    c.close()

if __name__ == '__main__':
    Main()