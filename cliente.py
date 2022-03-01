#from lib2to3.pytree import convert
import _thread
import json
import os
import time
import zmq

IP_ADDRESS = '10.0.1.1'
TOPIC = None
fila_msgs = []

conf = []


def client():

    ri = 'nao'
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.connect(f"tcp://{IP_ADDRESS}:5500")
    opc = None
    # time.sleep(20)

    while opc != "0":
        os.system('clear') or None
        print("################ ACADEMIA POTENAY ################\n")
        print("1 - Log-in")
        print("2 - Inscrever-se")
        print("0 - Sair")
        opc = input('\nDigite uma Opcao: ')

        if opc == '1':
            os.system('clear') or None
            email = input("Digite o nome: ")
            senha = input("Digite o telefone: ")
            msg = {}
            msg['codigo'] = 1
            msg['codigo2'] = 1
            msg['emaill'] = email
            msg['senhaa'] = senha
            msg_json = json.dumps(msg)
            fila_msgs.append(msg_json)
        if opc == '2':
            os.system('clear') or None
            nome = input("Digite o seu nome: ")
            email = input("Digite seu Email: ")
            senha = input("Digite seu telefone: ")
            msg = {}
            msg['codigo'] = 2
            msg['codigo2'] = 2
            msg['nomee'] = nome
            msg['emaill'] = email
            msg['senhaa'] = senha
            msg_json = json.dumps(msg)
            fila_msgs.append(msg_json)
            ri = 'sim'

        if opc == '0':
            print("\nObrigado por utilizar nosso sistema! Volte sempre!!!\n")
            print('Saindo...\n')
            time.sleep(1)
            exit()

        opcEntrada = None
        os.system('clear') or None
        fant = conf

        if(str(fant) == '[\'sim\']'):
            opcEntrada = 10
            conf.pop(0)

        else:
            opcEntrada = None

        if opcEntrada == None:
            if(ri == 'sim'):
                print("Cadastro realizado com sucesso")
                ri = 'nao'
            else:

                print(
                    "Houve um erro de conecçao tente mais tarde ou sua senha/login estao invalidos")

        if opcEntrada == 10:
            print("Login Realizado com Sucesso")
            opcEntrada = 11

        if opcEntrada == 11:
            while opc != 0:
                os.system('clear') or None
                print(" 1 - Ficha")
                print(" 2 - Perfil ")
                print(" 0 - Sair")
                opc = input('Digite sua Opçao: ')
                if opc == '1':
                    os.system('clear') or None
                    print("Ficha")
                    msg = {}
                    msg['codigo'] = 7
                    msg_json = json.dumps(msg)
                    fila_msgs.append(msg_json)
                    opc = input("Digite o Codigo do produto: ")
                    os.system('clear') or None
                    print("Dados do cartao")
                    nomeTitular = input("Digite o nome do titular do cartao: ")
                    codigoCartao = input("Digite o codigo do cartao: ")
                    bandeiraCartao = input("Digite a bandeira: ")

                    msg = {}
                    msg['codigo'] = 9
                    msg['emaill'] = email
                    msg['status'] = 'Enviado_Para_Analise'
                    msg['itencodigo'] = opc
                    msg['nometitu'] = nomeTitular
                    msg['codcart'] = codigoCartao
                    msg['bandeira'] = bandeiraCartao
                    msg_json = json.dumps(msg)
                    fila_msgs.append(msg_json)
                    # Enviar para o servidor
                    opc = None

                if opc == '2':
                    msg = {}
                    msg['codigo'] = 4
                    msg['emaill'] = email
                    msg_json = json.dumps(msg)
                    fila_msgs.append(msg_json)
                    time.sleep(10)

                if opc == '3':
                    msg = {}
                    msg['codigo'] = 13
                    msg['emaill'] = email
                    msg_json = json.dumps(msg)
                    fila_msgs.append(msg_json)
                    os.system('clear') or None
                    print("Lista de historio de compra")
                    time.sleep(10)


if __name__ == "__main__":
    client()
