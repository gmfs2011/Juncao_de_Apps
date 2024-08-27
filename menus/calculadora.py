from module import *

def menuCalculadora() -> int:
    while True:
        limpar_terminal()
        print(f'Bem vindo a {colorir('verde', 'Calculadora')}')
        espaco()
        print(f' 0 - {colorir('vermelho', 'Sair')}')
        print(f' 1 - {colorir('roxo', 'Somar')}')
        print(f' 2 - {colorir('roxo', 'Subtrair')}')
        print(f' 3 - {colorir('roxo', 'Multiplicar')}')
        print(f' 4 - {colorir('roxo', 'Dividir')}')
        espaco()
        
        try:
            escolha: int = int(input('Escolha: '))
            if escolha > 4 or escolha < 0:
                raise TypeError
        except ValueError:
            erro('Escreva um Número')
            continue
        except TypeError:
            erro('Opção inválida')
            continue
        
        if escolha == 0:
            espaco(2)
            print(colorir('amarelo', 'Saindo...'))
            espaco()
            pausar_terminal()
            break
        
        return escolha
    return 0
