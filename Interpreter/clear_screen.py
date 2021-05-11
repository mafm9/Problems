import os

def clear_screen():
    #posix is for mac and linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        #cls is for windows
        _ = os.system('cls')

clear_screen()
