import random
import Funcoes
from time import sleep

def multilacaoRegenerativa (jogador, monstro):
    print("Voce se multila com as unhas e oferece seu sangue a xaoc")
    jogador.mana -= 3
    dano = random.randint(1,int(jogador.inteligencia/3))
    jogador.vida -= dano
    print(f"Você perdeu {dano} pontos de vida")
    if jogador.vida <= 0:
        input("Você morreu... !:")
    else:
        jogador.dano = int(jogador.inteligencia/2)+(random.randint(1,int(jogador.inteligencia/2)))+jogador.ataque
        Funcoes.calculaDano(jogador, monstro)
        jogador.vida += int(jogador.danoReal/1.4)
        monstro.vida -= jogador.danoReal
        print(f"você inflinge {jogador.danoReal} pontos de dano")
        print(f"Você se cura {int(jogador.danoReal/2)} pontos de vida")
        Funcoes.vidaLimite(jogador)
        print(f"Vida atual: {jogador.vida}")
        jogador.passar = True
        jogador.dano = 0

def rapDeAcademia (jogador, efeito):
    jogador.danoAumentado = jogador.ataque + int(jogador.defesa/7)
    efeito.danoAumentado = 1
    print("Apos ouvir o RAP DO SAITAMA você sente que tem que dar tudo de si em um golpe final!!!")
    sleep(1)
    efeito.monstroAgir = 1
    efeito.podeAgir = 5
    jogador.passar = True

def organizarAMente (jogador):
    jogador.vida += int(jogador.inteligencia/2)
    input("Você organiza sua mente, sua resiliencia aumenta e seu proximo golpe será critico ")
    sleep(1)
    jogador.criticoGarantido = True
    jogador.passar = True

def curaLeve (jogador):
    jogador.mana -= 2
    cura = 2+jogador.inteligencia+random.randint(1, jogador.inteligencia)
    print(f" +{cura}HP \n")