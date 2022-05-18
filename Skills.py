import random
import Funcoes
def multilacaoRegenerativa (jogador, monstro):
    print("Voce se multila com as unhas e oferece seu sangue a xaoc")
    jogador.mana -= 3
    dano = random.randint(0,2)
    jogador.vida -= dano
    print(f"Você perdeu {dano} pontos de vida")
    if jogador.vida <= 0:
        input("Você morreu... !:")
    else:
        dano = int(jogador.inteligencia/2)+(random.randint(1,jogador.inteligencia)+jogador.ataque)
        jogador.vida += dano - monstro.danoMitigado
        
        if dano - monstro.danoMitigado > 0:
            monstro.vida -= dano - monstro.danoMitigado
            print(f"você inflinge {dano - monstro.danoMitigado} pontos de dano")
        print(f"Você se cura {dano - monstro.danoMitigado} pontos de vida")
        Funcoes.vidaLimite(jogador)
        print(f"Vida atual: {jogador.vida}")