from module import *

def menuPrincipal() -> int:
    while True:
        limpar_terminal()
        espaco()
        print(f'Bem vindo ao {colorir('verde', 'Meu Computador')}')
        espaco()
        print(f' 0 - {colorir('vermelho', 'Sair')}')
        print(f' 1 - {colorir('roxo', 'Calculadora')}')
        print(f' 2 - {colorir('roxo', 'TODO')}')
        
        espaco()
        try:
            escolha = int(input('Escolha: '))
            if escolha > 2 or escolha < 0:
                raise TypeError
        except ValueError:
            erro('Escreva um Número')
            continue
        except TypeError:
            erro('Escolha inválida')
            continue
        
        if escolha == 0:
            espaco(2)
            print(colorir('amarelo', 'Saindo...'))
            break
        
        return escolha
    return 0
