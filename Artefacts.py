def golpeGanancioso (jogador, monstro):
    if "AGG" in jogador.artefatos:
        if jogador.dano == monstro.vida:
            jogador.ouro += 30
            print("GOLPE GANACIOSO: +30G")


def cabeloColorido (jogador):
    if "ACC" in jogador.artefatos and jogador.foiCritico == True:
        jogador.danoReal += int((jogador.dano*2) - jogador.danoReal)
        jogador.vida += int(jogador.dano/4)
        print("Você penetra a armadura do oponente e rouba sua vitalidade ")


def lagrimaBerserker (jogador, efeito):
    if "ALB" in jogador.artefatos:
        jogador.danoAumentado += efeito.tempoCombate
        if efeito.danoAumentado < 1:
            efeito.danoAumentado = 1
        print(f"Lagrima do Berserker: +{efeito.tempoCombate} dano")

def conhecimentoDor (jogador, monstro):
    if "ACD" in jogador.artefatos:
        jogador.mana += int(monstro.danoReal/3)
        print(f"você recupera {int(monstro.danoReal/3)} pontos de mana")