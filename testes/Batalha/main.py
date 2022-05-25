import time
#import keyboard # pip3 install keyboard
import os
import monstros as m
import cenario
import acoes

print(m.esqueleto)

RED   = "\033[1;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

os.system('cls') or None

class p:
  j = [' o ', '/|\\', '/ \\']
  m = [' O ', '/M\\', '/ \\']
  a = ['          ', '//(o,,o)\\\\', '          ']
    
jogador = m.esqueleto
monstro = m.aranha

"""
while jogador.vida > 0:  
  time.sleep(0.3) 
  os.system('cls') 
  cenario.normal(jogador, monstro) 
  while True:
      if keyboard.read_key() == "A":
          print("ATAQUE")          
          acoes.atacaMonstro(jogador, monstro)       
          break
      if keyboard.read_key() == "R":
          print("RECUPERAR")   
          acoes.recuperaVida(jogador, monstro)  
          break
"""
acoes.atacaJogador(jogador, monstro)    
  
        
