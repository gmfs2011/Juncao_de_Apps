from module import *
import os
import json
import datetime


def criarArquivo() -> None:
    with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'w') as f:
        f.write('[]')

def existeArquivo() -> bool:
    return os.path.exists('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json')

def lerArquivo() -> list:
    with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'r') as f:
        return json.loads(f.read())

def adicionarTodoEmArquivo(todo: str) -> None:
    if not existeArquivo():
        criarArquivo()
    with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'r') as f:
        todos = json.load(f)

    if not lerArquivo():
        id = 1
    else:
        id = lerArquivo()[-1]['id'] + 1
    
    tarefa = {
        'id': id,
        'todo': todo,
        'progresso': 'to do',
        'data_criacao': f'{datetime.datetime.now()}',
        'data_atualizacao': f'{datetime.datetime.now()}',
        'importante': False
    }
    
    
    todos.append(tarefa)
    
    with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'w') as f:
        t = json.dumps(todos)
        f.write(t)

def perguntarTodo() -> str:
    limpar_terminal()
    todo: str = input('Digite o nome do TODO: ')
    return todo

def adicionarTodo() -> None:
    todo: str = perguntarTodo()
    adicionarTodoEmArquivo(todo)
    espaco()
    print(f'{colorir('rosa', 'TODO')} adicionado')
    espaco()
    pausar_terminal()

def listarTodos() -> None:0
    limpar_terminal()
    try:
        todos = lerArquivo()
    except:
        erro('Escreva algum TODO primeiro')
        return
    
    if not len(lerArquivo()):
        erro('Escreva algum TODO primeiro')
        return
    
    for todo in todos:
        if todo['importante']:
            if todo['progresso'] == 'to do':
                print(f'{colorir('azul', todo['id'])} - {colorir('vermelho', todo['todo'])} - {colorir('roxo', todo['progresso'])}')
            elif todo['progresso'] == 'doing':
                print(f'{colorir('azul', todo['id'])} - {colorir('vermelho', todo['todo'])} - {colorir('amarelo', todo['progresso'])}')
            else:
                print(f'{colorir('azul', todo['id'])} - {colorir('vermelho', todo['todo'])} - {colorir('verde', todo['progresso'])}')
    
    espaco()
    
    for todo in todos:
        if not todo['importante']:
            if todo['progresso'] == 'to do':
                print(f'{colorir('azul', todo['id'])} - {colorir('rosa', todo['todo'])} - {colorir('roxo', todo['progresso'])}')
            elif todo['progresso'] == 'doing':
                print(f'{colorir('azul', todo['id'])} - {colorir('rosa', todo['todo'])} - {colorir('amarelo', todo['progresso'])}')
            else:
                print(f'{colorir('azul', todo['id'])} - {colorir('rosa', todo['todo'])} - {colorir('verde', todo['progresso'])}')
    
    espaco()
    pausar_terminal()

def atualizarTodo() -> None:
    while True:
        limpar_terminal()
        
        try:
            todos = lerArquivo()
        except:
            erro('Escreva algum TODO primeiro')
            return
        
        if not len(lerArquivo()):
            erro('Escreva algum TODO primeiro')
            return
        
        listarTodos()
        
        espaco()
        todos = lerArquivo()
        try:
            tarefa = int(input('ID do TODO: '))
        except ValueError:
            erro('Escreva um Número')
            continue
        
        espaco()
        for todo in todos:
            if todo['id'] == tarefa:
                novoTodo = input('Como você deseja chamar o TODO: ')
                todo['todo'] = novoTodo
                with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'w') as f:
                    t = json.dumps(todos)
                    f.write(t)
                return
        
        erro('TODO nao achado')
        espaco()
        pausar_terminal()
    erro('Escreva um TODO primeiro')

def deletarTodo() -> None:
    while True:
        limpar_terminal()
        
        try:
            todos = lerArquivo()
        except:
            erro('Escreva algum TODO primeiro')
            return
        
        if not len(lerArquivo()):
            erro('Escreva algum TODO primeiro')
            return
        
        listarTodos()
        espaco()
        try:
            id = int(input('Digite o ID do TODO: '))
        except ValueError:
            erro('Escreva um Número')
            continue
        
        for todo in todos:
            print(todo)
            if todo['id'] == id:
                todos.remove(todo)
                with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'w') as f:
                    t = json.dumps(todos)
                    f.write(t)
                return
        
        erro('ID nao achado')

def marcarFazer() -> None:
    while True:
        limpar_terminal()
        
        try:
            todos = lerArquivo()
        except:
            erro('Escreva algum TODO primeiro')
            return
        
        if not len(lerArquivo()):
            erro('Escreva algum TODO primeiro')
            return
        
        listarTodos()
        espaco()
        
        try:
            id = int(input('DIgite o ID do TODO: '))
        except ValueError:
            erro('Escreva um Número')
            continue
        
        for todo in todos:
            if todo['id'] == id:
                todo['progresso'] = 'to do'
                with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'w') as f:
                    t = json.dumps(todos)
                    f.write(t)
                return
        
        erro('ID nao achado')

def marcarProgresso() -> None:
    while True:
        limpar_terminal()
        
        try:
            todos = lerArquivo()
        except:
            erro('Escreva algum TODO primeiro')
            return
        
        if not len(lerArquivo()):
            erro('Escreva algum TODO primeiro')
            return
        
        listarTodos()
        espaco()
        
        try:
            id = int(input('DIgite o ID do TODO: '))
        except ValueError:
            erro('Escreva um Número')
            continue
        
        for todo in todos:
            if todo['id'] == id:
                todo['progresso'] = 'doing'
                with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'w') as f:
                    t = json.dumps(todos)
                    f.write(t)
                return
        
        erro('ID nao achado')

def marcarPronto() -> None:
    while True:
        limpar_terminal()
        
        todos = lerArquivo()
        
        listarTodos()
        espaco()
        
        try:
            id = int(input('DIgite o ID do TODO: '))
        except ValueError:
            erro('Escreva um Número')
            continue
        
        for todo in todos:
            if todo['id'] == id:
                todo['progresso'] = 'done'
                with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'w') as f:
                    t = json.dumps(todos)
                    f.write(t)
                return
        
        erro('ID nao achado')

def marcarNaoImportante() -> None:
    while True:
        limpar_terminal()
        
        try:
            todos = lerArquivo()
        except:
            erro('Escreva algum TODO primeiro')
            return
        
        if not len(lerArquivo()):
            erro('Escreva algum TODO primeiro')
            return
        
        listarTodos()
        espaco()
        
        try:
            id = int(input('DIgite o ID do TODO: '))
        except ValueError:
            erro('Escreva um Número')
            continue
        
        for todo in todos:
            if todo['id'] == id:
                todo['importante'] = False
                with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'w') as f:
                    t = json.dumps(todos)
                    f.write(t)
                return
        
        erro('ID nao achado')

def marcarImportante() -> None:
    while True:
        limpar_terminal()
        
        try:
            todos = lerArquivo()
        except:
            erro('Escreva algum TODO primeiro')
            return
        
        if not len(lerArquivo()):
            erro('Escreva algum TODO primeiro')
            return
        
        listarTodos()
        espaco()
        
        try:
            id = int(input('DIgite o ID do TODO: '))
        except ValueError:
            erro('Escreva um Número')
            continue
        
        for todo in todos:
            if todo['id'] == id:
                todo['importante'] = True
                with open('E:\\Programacao\\Projetos\\Meu_Computador\\arquivos\\todos.json', 'w') as f:
                    t = json.dumps(todos)
                    f.write(t)
                return
        
        erro('ID nao achado')
