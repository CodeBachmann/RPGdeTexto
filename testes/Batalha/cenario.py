import os 

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def cenario(vida, vidaM, j, m):
  os.system('cls') 
  print("(A)ataque: 3 dano   --  (R)recuperar: 2 vida\n")  
  print(f" {vida} ❤                 {vidaM} ❤ ")    
  print(f" {j.aparencia[0]}                 {m.aparencia[0]}  ")
  print(f" {j.aparencia[1]}                 {m.aparencia[1]}  ")
  print(f" {j.aparencia[2]}                 {m.aparencia[2]}  ")  


def normal(j, m):
  cenario(j.vida, m.vida, j, m)

def Atacado(j, m):
  cenario(RED+str(j.vida)+RESET, m.vida, j, m)

def Atacando(j, m):
  cenario((j.vida), RED+str(m.vida)+RESET, j, m)

def Recuperando(j, m):
  cenario(GREEN+str(j.vida)+RESET, m.vida, j, m)
