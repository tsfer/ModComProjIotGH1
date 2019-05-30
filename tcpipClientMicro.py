import socket
import pyserial


def Main():
    host = '127.0.0.1'
    port = 5000 

    server = ('127.0.0.1',6666)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
#vai parar a conexão com o servidor em caso de enviar uma mesagem de valor 0

#Chamar o módulo que vai definir a mensagem

    message = '''dados dos sensores'''
    while message != '0':
        s.sendto(message, server)
        data, addr = s.recvfrom(1024)
    #se tiver um display na versão final usamos o print para o display
        print ('Dados recebidos com sucesso')
    #enviar o pacote de dados com comandos para o microcontrolador
        mdata
    #finaliza o envio de dados e define a mensagem
        message = mdata
    s.close()

if __name__ == '__main__':
    Main()