import time
import keyboard # pip3 install keyboard
import os

RED   = "\033[1;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

os.system('cls') or None


vidaJogador = 3
vidaMonstro = 30

def limpaTela():
  os.system('cls') or None 

def mostraCenario(vidaJogador, vidaMonstro):
  limpaTela()  
  print("(A)ataque: 3 dano   --  (R)recuperar: 2 vida\n")  
  print(f" {vidaJogador} ❤                 {vidaMonstro} ❤ ")    
  print(f"  O                   O   ")
  print(f" /|\                 /|\  ")
  print(f" / \                 / \  ")  

def cenarioAtacado(vidaJogador, vidaMonstro):
  mostraCenario(RED+str(vidaJogador)+RESET, vidaMonstro)

def cenarioAtacando(vidaJogador, vidaMonstro):
  mostraCenario((vidaJogador), RED+str(vidaMonstro)+RESET)

def cenarioRecuperando(vidaJogador, vidaMonstro):
  mostraCenario(GREEN+str(vidaJogador)+RESET, vidaMonstro)

def atacaMonstro(vidaJogador, vidaMonstro):
  for a in range(17):
    time.sleep(0.01) 
    limpaTela()
    b = 16-a
    print("(A)ataque: 3 dano   --  (R)recuperar: 2 vida\n")  
    print(f" {vidaJogador} ❤                 {vidaMonstro} ❤ ")              
    print(f"  O                   O   ")
    print(f" /|\{a*' '}-{b*' '  }/|\  ")
    print(f" / \                 / \  ") 
  vidaMonstro -= 3    
  cenarioAtacando(vidaJogador, vidaMonstro)
  time.sleep(0.5)  
  return vidaMonstro

def atacaJogador(vidaJogador, vidaMonstro):
  for a in range(17):
    time.sleep(0.01) 
    limpaTela()
    b = 16-a
    print("(A)ataque: 3 dano   --  (R)recuperar: 2 vida\n")  
    print(f" {vidaJogador} ❤                 {vidaMonstro} ❤ ")              
    print(f"  O                   O   ")
    print(f" /|\{b*' '}-{a*' '  }/|\  ")
    print(f" / \                 / \  ") 
  vidaJogador -= 1   
  cenarioAtacado(vidaJogador, vidaMonstro)
  time.sleep(0.5)  
  return vidaJogador 

def recuperaVida(vidaJogador, vidaMonstro):
  for a in range(5):
    time.sleep(0.4) 
    limpaTela()
    b = 6-a
    print("(A)ataque: 3 dano   --  (R)recuperar: 2 vida\n")  
    print(f" {vidaJogador} ❤                 {vidaMonstro} ❤ ")              
    print(f"  O {GREEN+a*'|'+RESET}{b*' '  }            O   ")
    print(f" /|\{GREEN+a*'|'+RESET}{b*' '  }           /|\  ")
    print(f" / \{GREEN+a*'|'+RESET}{b*' '  }           / \  ")  
  cenarioRecuperando(vidaJogador, vidaMonstro)
  time.sleep(0.7)  
  return vidaJogador   


while vidaJogador > 0:  
  time.sleep(0.3) 
  limpaTela()
  mostraCenario(vidaJogador, vidaMonstro) 
  while True:
      if keyboard.read_key() == "A":
          print("ATAQUE")          
          vidaMonstro = atacaMonstro(vidaJogador, vidaMonstro)       
          break
      if keyboard.read_key() == "R":
          print("RECUPERAR")   
          vidaJogador = recuperaVida(vidaJogador, vidaMonstro)  
          break
  vidaJogador = atacaJogador(vidaJogador, vidaMonstro)    
  
        
