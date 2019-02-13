import socket 

from datetime import datetime

print('#### Questão 2 ####\n')
print( '--- Criando serverUDP ---')



addr = '192.168.122.1'
porta = 5005

#CRIANDO SOCKET TCP
TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

end_port = (addr, porta)

TCP.bind(end_port)

TCP.listen()

print('Servidor TCP aguardadno conexões na porta %s, para encerrar pressione Ctrl+C' %porta)

while True: 
    
    con, cliente = TCP.accept()
    print("Conectado por: ", cliente)
    mensagem = con.recv(2048).decode('utf-8')
    print("Mensagem recebida: %s" %mensagem)
    
    tempo = datetime.now().hour
    
    if tempo < 12:
        msg ='Bom Dia, '+mensagem
        #msg.encode()
        con.send(msg.encode())
    elif tempo < 18:
        msg ='Boa Tarde, '+mensagem
        #msg.encode()
        con.send(msg.encode())
    else:
        msg ='Boa Tarde, '+mensagem
        #msg.encode()
        con.send(msg.encode())

        
    print("Finalizando conexão com o cliente: ", cliente)
con.close()