from calculos import *

if __name__ == "__main__":
    '''
    a1 = Adicao(4)
    a2 = Adicao(6)
    s1 = Subtracao(2)
    m1 = Multiplicacao(3)
    d1 = Divisao(2)
    c1 = Calculadora()
    print('------------ Soma ------------')
    print(a1.calcular(6))
    print(a1.calcularinverso(6))
    print('--------- Subtracao ----------')
    print(s1.calcular(6))
    print(s1.calcularinverso(6))
    print('-------- Calculadora ---------')
    #c1.add_operacao(a1)
    #c1.add_operacao(m1)
    #c1.add_operacao(d1)
    #c1.calcular_total()
    #print(c1.resultado)
    #c1.desfazer_ultima()
    #print(c1.resultado)
    '''
    c1 = Calculadora()
    print(f'>> {c1.resultado}')
    t = input('>> ')

    while t != 'q':
        if t == '+' or t == '-' or t == '*' or t == '/':
            x = float(input('>> '))

            if t == '+':
                op = Adicao(x)
            elif t == '-':
                op = Subtracao(x)
            elif t == '*':
                op = Multiplicacao(x)
            elif t == '/':
                op = Divisao(x)

            c1.add_operacao(op)

        elif t == 'z':
            c1.calcular_total()
            c1.desfazer_ultima()
            print(f'>> {c1.resultado}')
        elif t == '=':
            c1.calcular_total()
            print(f'>> {c1.resultado}')

        t = input('>> ')