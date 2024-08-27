from module import *

def menuModos() -> int:
    while True:
        limpar_terminal()
        espaco()
        print(f'Bem vindo ao {colorir('verde', 'Menu de Modos')}')
        print(f'Escolha o seu Modo para o seu uso no Momento')
        espaco()
        print(f' 0 - {colorir('vermelho', 'Sair')}')
        print(f' 1 - {colorir('roxo', 'Programacao')}')
        print(f' 2 - {colorir('roxo', 'Minecraft')}')
        print(f' 3 - {colorir('roxo', 'Roblox')}')
        print(f' 4 - {colorir('roxo', 'CAD')}')
        print(f' 5 - {colorir('roxo', 'Entretenimento')}')
        print(f' 6 - {colorir('roxo', 'Nenhum')}')
        espaco()
        
        try:
            escolha: int = int(input('Escolha: '))
            if escolha > 6 or escolha < 0:
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
