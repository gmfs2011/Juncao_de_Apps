from module import *
import webbrowser as wb
import pyautogui as pag

pag.PAUSE = 0.5

modos = {
        1: {
                'urls': ['https://www.youtube.com/',
                         'https://github.com/alunogmfs2',
                         'https://www.tabnews.com.br/'
                        ],
                'apps': [
                         'visual studio code',
                         'pycharm'
                        ]
           },
        2: {
                'urls': [
                         'https://www.youtube.com/',
                         'https://www.chunkbase.com/apps/seed-map'
                        ],
                'apps': [
                         'curseforge'
                        ]
           },
        3: {
                'urls': [
                         'https://www.youtube.com/',
                         'https://www.roblox.com/'
                        ],
                'apps': [
                         'roblox'
                        ]
           },
        4: {
                'urls': [
                         'https://www.youtube.com/'
                        ],
                'apps': [
                         'fusion'
                        ]
           },
        5: {
                'urls': [
                         'https://www.youtube.com/'
                        ],
                'apps': [

                        ]
           }
        }


def abrirSites(escolha: int) -> None:
    for url in modos[escolha]['urls']:
        wb.open(url)

def abrirApps(escolha: int) -> None:
    for app in modos[escolha]['apps']:
        pag.press('winleft')
        pag.write(app)
        pag.press('enter')

def abrirTudo(escolha: int) -> None:
    abrirApps(escolha)
    abrirSites(escolha)
