import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

def launch98(systemlevel, systembadge, systempro):
    clear()
    print('P r o g r e s s b a r  9 8')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    beginMenu("98", systemlevel, systempro)
