#from lib2to3.pytree import convert
import json
import os
import time
import zmq
import sqlite3

IP_ADDRESS = '10.0.1.1'
TOPIC = None
fila_msgs = []

conf = []


connection = sqlite3.connect('academia.db')

cur = connection.cursor()

cur.execute("SELECT *FROM cliente ")

connection.commit()
connection.close()


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

        listas = [[]]  # uma lista de lista

        if opc == '1':
            os.system('clear') or None
            email = input("Digite seu e-mail: ")
            telefone = input("Digite o telefone: ")

        if opc == '2':
            os.system('clear') or None

            nova = []  # cria uma lista para adicionar o id, nome e idade da pessoa
            nomeCliente = input("Digite o seu nome: ")
            email = input("Digite seu Email: ")
            telefone = input("Digite seu telefone: ")
            nova.append(nomeCliente)
            nova.append(email)
            nova.append(telefone)
            # Adiciona a lista criada com o cadastro da pessoa dentro da lista
            listas.append(nova)

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
                    "Houve um erro. Tente novamente senha ou login nao correspondem")

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


if __name__ == "__main__":
    client()
