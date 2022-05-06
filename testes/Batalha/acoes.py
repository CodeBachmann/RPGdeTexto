import os
from re import A
import poderes
import cenario
import time
import monstros as m


def acaoVai(poder, jogador, monstro):
  for a in range(17):
    time.sleep(0.01) 
    os.system('cls')
    b = 16-a
    print("(A)ataque: 3 dano   --  (R)recuperar: 2 vida\n")  
    print(f" {jogador.vida} ❤                 {monstro.vida} ❤ ")              
    print(f"  O {a*' '}{poder[0]}{b*' '  }{m.aranha.aparencia[0]}")
    print(f" /|\{a*' '}{poder[1]}{b*' '  }{m.aranha.aparencia[1]}")
    print(f" / \{a*' '}{poder[2]}{b*' '  }{m.aranha.aparencia[2]}") 

def acaoVolta(poder, jogador, monstro):
  for a in range(17):
    time.sleep(0.01) 
    os.system('cls')
    b = 16-a
    print("(A)ataque: 3 dano   --  (R)recuperar: 2 vida\n")  
    print(f" {jogador.vida} ❤                 {monstro.vida} ❤ ")              
    print(f"  O {b*' '}{poder[0]}{a*' '  }{m.aranha.aparencia[0]}")
    print(f" /|\{b*' '}{poder[1]}{a*' '  }{m.aranha.aparencia[1]}")
    print(f" / \{b*' '}{poder[2]}{a*' '  }{m.aranha.aparencia[2]}") 

def atacaMonstro(jogador, monstro):
  acaoVai([' ','*',' '], jogador, monstro)
  monstro.vida -= 3    
  cenario.Atacando(jogador, monstro)
  time.sleep(0.5)  

def atacaJogador(jogador, monstro):
  acaoVolta([' ','-',' '], jogador, monstro)
  jogador.vida -= 1   
  cenario.Atacado(jogador, monstro)
  time.sleep(0.5)  

def recuperaVida(jogador, monstro):
  acaoVai(['|','|','|'], jogador, monstro)
  jogador.vida += 1
  cenario.Recuperando(jogador, monstro)
  time.sleep(0.7)  
