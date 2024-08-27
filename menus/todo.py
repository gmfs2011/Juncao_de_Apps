from module import *


def menuTodo() -> int:
    while True:
        limpar_terminal()
        espaco()
        print(f'Bem vindo ao {colorir('verde', 'Menu TODO')}')
        espaco()
        print(f' 0 - {colorir('vermelho', 'Sair')}')
        print(f' 1 - {colorir('roxo', 'Listar TODOs')}')
        print(f' 2 - {colorir('roxo', 'Adicionar TODO')}')
        print(f' 3 - {colorir('roxo', 'Atualizar TODO')}')
        print(f' 4 - {colorir('roxo', 'Deletar TODO')}')
        print(f' 5 - {colorir('roxo', 'Marcar TODO como \"a fazer\"')}')
        print(f' 6 - {colorir('roxo', 'Marcar TODO como \"em progresso\"')}')
        print(f' 7 - {colorir('roxo', 'Marcar TODO como concluído')}')
        print(f' 8 - {colorir('roxo', 'Marcar TODO como nao importante')}')
        print(f' 9 - {colorir('roxo', 'Marcar TODO como importante')}')
        espaco()
        
        try:
            escolha: int = int(input('Escolha: '))
            if escolha > 9 or escolha < 0:
                raise TypeError
        except ValueError:
            erro('Escreva um Número')
            continue
        except TypeError:
            erro('Escolha uma opcao válida')
            continue
        
        if escolha == 0:
            espaco(2)
            print(colorir('amarelo', 'Saindo...'))
            break
        
        return escolha
    return 0
