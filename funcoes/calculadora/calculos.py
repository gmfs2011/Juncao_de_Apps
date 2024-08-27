from module import *

r: int = None

def numeros() -> tuple[float]:
    while True:
        limpar_terminal()
        try:
            if r:
                n1 = r
                print(f'Primeiro Número: {colorir('azul', str(n1))}')
            else:
                n1 = int(input('Escreva o primeiro número: '))
            n2 = int(input('Escreva o segundo número: '))
        except ValueError:
            erro('Escreva um Número')
            continue

        return n1, n2

def perguntarContinuarComResultado(res) -> None:
    global r
    while True:
        limpar_terminal()
        escolha = input(f'Você gostaria de continuar a calcular com {colorir('rosa', str(res))} [Y/N]? ').lower()
        
        if escolha != 'y' and escolha != 'n':
            erro('Escolha uma opcao válida')
            continue
        if escolha == 'y':
            r = res
            break
        if escolha == 'n':
            break

def somar() -> None:
    n1, n2 = numeros()
    resultado: float = n1 + n2
    
    espaco()
    print(f'{n1} + {n2} = {colorir('rosa', str(resultado))}')
    espaco()
    
    perguntarContinuarComResultado(resultado)
    pausar_terminal()

def subtrair() -> None:
    n1, n2 = numeros()
    resultado: float = n1 - n2
    
    espaco()
    print(f'{n1} - {n2} = {colorir('rosa', str(resultado))}')
    espaco()
    
    perguntarContinuarComResultado(resultado)
    pausar_terminal()

def multiplicar() -> None:
    n1, n2 = numeros()
    resultado: float = n1 * n2
    
    espaco()
    print(f'{n1} x {n2} = {colorir('rosa', str(resultado))}')
    espaco()
    
    perguntarContinuarComResultado(resultado)
    pausar_terminal()

def dividir() -> None:
    while True:
        n1, n2 = numeros()
        try:
            resultado: float = n1 / n2
        except ZeroDivisionError:
            erro('Não é possível dividir por zero')
            continue
        
        espaco()
        print(f'{n1} / {n2} = {colorir('rosa', f'{resultado:.5f}')}')
        espaco()
        
        perguntarContinuarComResultado(resultado)
        pausar_terminal()
        break
