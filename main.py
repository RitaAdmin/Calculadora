import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
        if num2!=0:
            result=num1/num2
        else:
            raise ZeroDivisionError("Divisão por zero")
    elif operador == '**':
        result = num1 ** num2
    else:
        print("A operação não é válida.")
    


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
         
        print('Calculadora')
        print('----------------------------------\n')
        print('1-Soma')
        print('2-Subtração')
        print('3-Multiplicação')
        print('4-Divisão')
        print('5-Exponencial')
        print('0-Sair da calculadora')
            
        escolha= input("Escolha uma opção: ")
            
        if escolha=="0":
            print("Sair programa com sucesso")
            break
        
        if escolha in("1","2","3","4","5"):
            try:
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
                
                if escolha == '1':
                    opcao = '+'
                elif escolha == '2':
                    opcao = '-'
                elif escolha == '3':
                    opcao = '*'
                elif escolha == '4':
                    opcao = '/'
                elif escolha == '5':
                    opcao = '**'
    
    
                resultado = calculadora(num1, num2, opcao)
                print(f"\n Resultado é: {num1} {opcao}{num2}={resultado}")
        
                        
            except ValueError:
                print('Dados inválidos! -> Tente novamente!')
                time.sleep(2)

            except ZeroDivisionError:
                print('Impossível dividir por zero! -> Tente novamente!')
                time.sleep(2)

        print('\nVolte sempre!\n')
