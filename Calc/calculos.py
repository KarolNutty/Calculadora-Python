# Funções para as operações
def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."


# Função principal da calculadora
def calculadora():
    print("Selecione a operação desejada:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Entrada da operação
    operacao = input("Digite o número da operação (1/2/3/4): ")

    # Solicitar os números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realizar a operação
    if operacao == '1':
        print(f"{num1} + {num2} = {soma(num1, num2)}")
    elif operacao == '2':
        print(f"{num1} - {num2} = {subtracao(num1, num2)}")
    elif operacao == '3':
        print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
    elif operacao == '4':
        print(f"{num1} / {num2} = {divisao(num1, num2)}")
    else:
        print("Operação inválida")


# Rodando a calculadora
calculadora()
