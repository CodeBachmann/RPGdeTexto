def atordoar (jogador, efeito):
    if efeito.podeAgir != 0 and efeito.podeAgir != 5:
        jogador.podeAgir = False
        efeito.podeAgir -= 1
    elif efeito.podeAgir == 0:
        jogador.podeAgir = True
    elif efeito.podeAgir == 5:
        jogador.podeAgir = True
        efeito.podeAgir = 1