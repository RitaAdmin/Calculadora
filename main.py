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
        print("Operação inválida.")
    
    return result


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
         
        try:
            print('Calculadora')
            print('----------------------------------\n')
            print('1-Soma')
            print('1-Subtração')
            print('1-Multiplicação')
            print('1-Divisão')
            print('1-Exponencial')
            print('0-Sair da calculadora')
            
            
            num1 = float(input('Digite o primeiro número: '))
                        
        

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
