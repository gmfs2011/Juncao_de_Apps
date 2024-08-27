from os import system


def espaco(vezes: int = 1) -> None:
    for i in range(vezes):
        print()

def limpar_terminal() -> None:
    system('cls')

def pausar_terminal() -> None:
    system('pause')

def erro(erro: str) -> None:
    espaco()
    print(f'{colorir('vermelho', f'Erro: {erro}')}')
    espaco()
    pausar_terminal()

def colorir(cor: str,
          texto: str,
          cor_de_fundo: str | None = None,
          special: str | None = None
          ) -> str:
    
    cores = {
        'vermelho': '31',
        'verde': '32',
        'amarelo': '33',
        'azul': '34',
        'rosa': '35',
        'roxo': '36',
        'cinza': '37'
    }
    
    speciais = {
        'negrito': '1',
        'sublinhado': '4',
    }
    
    cores_de_fundo = {
        'preto': '40',
        'vermelho': '41',
        'verde': '42',
        'amarelo': '43',
        'azul': '44',
        'rosa': '45',
        'roxo': '46',
        'cinza': '47'
    }
    
    if cor_de_fundo and special:
        if special in speciais and cor_de_fundo in cores_de_fundo:
            return f'\033[{speciais[special]};{cores[cor]};{cores_de_fundo[cor_de_fundo]}m{texto}\033[m'
    
    if cor_de_fundo:
        if cor_de_fundo in cores_de_fundo:
            return f'\033[0;{cores[cor]};{cores_de_fundo[cor_de_fundo]}m{texto}\033[m'
    
    if special:
        if special in speciais:
            return f'\033[{speciais[special]};{cores[cor]};40m{texto}\033[m'
    
    if cor in cores:
        return f'\033[{cores[cor]}m{texto}\033[m'
