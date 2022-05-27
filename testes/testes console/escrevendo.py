
import os
import sys
import time

os.system('cls') or None

frase = 'Você morreu...'

for i in list(frase):
    print(i, end='')
    #O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
    sys.stdout.flush()
    time.sleep(0.3)
    

