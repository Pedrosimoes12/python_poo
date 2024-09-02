from frota import *

def simular_carro(carro: Carro):
            print('1- Ligar motor')
            print('2- Desligar motor')
            print('3- Acelerar')

            op = 0
            while op not in (1, 2, 3):
                op = int(input("Digite as opcoes[1-3]: "))

            if op == 1:
                carro.ligar()
            elif op == 2:
                carro.desligar()
            elif op == 3:
                v = float(input("Informe a velocidade: "))
                t = float(input("Informe o tempo: "))
                carro.acelerar(v, t)

            print('Infos atuais do carro')
            print(carro)
            print("\n")

if __name__ == "__main__":
    print('Cadastre o carro1')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Digite o nivel do tanque: '))
    cm = float(input('Digite o consumo medio do carro: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, cm)

    print('Cadastre o carro2')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros - float(input('Digite o nivel do tanque: '))
    cm = float(input('Digite o consumo medio do carro: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, cm)

    '''
    Controlando o carro até ele atingir 300 Km ou até acabar a gasolina dos 2
    '''
    while carro1.get_odometro() < 300 and carro2.get_odometro() < 300 and \
            (carro1.get_tanque() > 0 or  carro2.get_tanque() > 0):
        try:
            op_carro = 0
            while op_carro not in (1,2):
                op_carro = int(input("Qual carro simular 1 ou 2? "))

            if op_carro == 1:
                simular_carro(carro1)
            else:
                simular_carro(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    try:
        carro1.desligar()
        carro2.desligar()
    except Exception as e :
        print(e)

    if carro1.get_odometro() > carro2.get_odometro():
        print(carro1)
    else:
        print(carro2)

    if carro1.get_tanque() == 0 and carro2.get_tanque() == 0:
        print('Acabou a gasolina dos carros')