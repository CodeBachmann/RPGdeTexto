from time import sleep          
import Funcoes


def golpeGanancioso (jogador, monstro):
    if "AGG" in jogador.artefatos:
        if jogador.danoReal > monstro.vida:
            ouroExtra = jogador.danoReal - monstro.vida
            jogador.ouro += int(ouroExtra*1.4)
            print(f"GOLPE GANACIOSO: +{ouroExtra}G")
            sleep(0.5)


def cabeloColorido (jogador):
    if "ACC" in jogador.artefatos and jogador.foiCritico == True:
        danoExtra = int((jogador.dano*2) - (jogador.danoReal))
        jogador.danoReal += danoExtra
        jogador.vida += int(jogador.dano/3)
        print(f"CABELO COLORIDO:  {danoExtra} DANO EXTRA/nCABELO COLORIDO: +{int(jogador.dano/3)}HP")
        sleep(0.5)


def lagrimaBerserker (jogador, efeito):
    if "ALB" in jogador.artefatos:
        jogador.danoAumentado += efeito.tempoCombate
        if efeito.danoAumentado < 1:
            efeito.danoAumentado = 1
        print(f"LAGRIMA DO BERSERKER: +{efeito.tempoCombate} DANO EXTRA")
        sleep(0.5)


def conhecimentoDor (jogador, monstro):
    if "ACD" in jogador.artefatos:
        jogador.mana += int(monstro.danoReal/4)
        print(f"CONHECIMENTO DA DOR: +{int(monstro.danoReal/4)} MP ")
        sleep(0.5)


def masoquistaAcademia (jogador, monstro):
    if "AMDA" in jogador.artefatos:
        jogador.danoAumentado += int(monstro.danoReal/2)
        print(f"MASOQUISTA DA ACADEMIA: +{int(monstro.danoReal/2)} DANO EXTRA")
        sleep(0.5)

def idoloXaoc(jogador, monstro):
    if "AIX" in jogador.artefatos:
        if monstro.vida <= 0:
            jogador.vida += int(jogador.vidaMax/4)
            print(f"+{int(jogador.vidaMax/4)} HP | Xaoc consome o corpo do oponente, você se sente revigorado")
            Funcoes.vidaLimite(jogador)