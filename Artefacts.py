from time import sleep          
import Funcoes


def golpeGanancioso (jogador, monstro, efeito):
    if "AGG" in jogador.artefatos:
        if jogador.danoReal > monstro.vida:
            ouroExtra = jogador.danoReal - monstro.vida
            jogador.ouro += int(ouroExtra*1.4)
            print(f"Golpe ganancioso: +{ouroExtra}G")
            sleep(0.5)


def cabeloColorido (jogador, monstro, efeito):
    if "ACC" in jogador.artefatos and jogador.foiCritico == True:
        danoExtra = int((jogador.dano*2) - (jogador.danoReal))
        jogador.danoReal += danoExtra
        jogador.vida += int(jogador.dano/3)
        print(f"Cabelo colorido:  {danoExtra} dano extra\nCabelo colorido: +{int(jogador.dano/3)}HP")
        sleep(0.5)


def lagrimaBerserker (jogador, monstro, efeito):
    if "ALB" in jogador.artefatos:
        jogador.danoAumentado += efeito.tempoCombate
        if efeito.danoAumentado < 1:
            efeito.danoAumentado = 1
        print(f"Lagrima do berserker: +{efeito.tempoCombate} dano extra")
        sleep(0.5)


def conhecimentoDor (jogador, monstro, efeito):
    if "ACD" in jogador.artefatos:
        jogador.mana += int(monstro.danoReal/4)
        print(f"Conhecimento de academia: +{int(monstro.danoReal/4)} MP ")
        sleep(0.5)


def masoquistaAcademia (jogador, monstro, efeito):
    if "AMDA" in jogador.artefatos:
        jogador.danoAumentado += int(monstro.danoReal/2)
        print(f"Masoquista da academia: +{int(monstro.danoReal/2)} dano extra")
        sleep(0.5)

def idoloXaoc(jogador, monstro, efeito):
    if "AIX" in jogador.artefatos:
        if monstro.vida <= 0:
            jogador.vida += int(jogador.vidaMax/4)
            print(f"+{int(jogador.vidaMax/4)} HP | Xaoc consome o corpo do oponente, você se sente revigorado")
            Funcoes.vidaLimite(jogador)

def pikemanPatience(jogador, monstro, efeito):
    if "APP" in jogador.artefatos:
        if efeito.tempoCombate != 1 and efeito.tempoCombate%3 == 0:
            jogador.danoReal += jogador.dano-jogador.danoReal
            print("Pikeman Patience: you spot a weak point in your opponent")

def hardSnakeSkin(jogador, monstro, efeito):
    if "AHSS" in jogador.artefatos:
        mitigado =  int(jogador.defesa*0.05)
        monstro.dano -= mitigado
        print("Hard Snake Skin: mitigate some damage")

