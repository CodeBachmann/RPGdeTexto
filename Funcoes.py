from asyncio.windows_events import NULL
import random
import Artefacts
from re import S

def vidaLimite (jogador):
    if jogador.vida > jogador.vidaMax:
        jogador.vida = jogador.vidaMax

def manaLimite (jogador):
    if jogador.mana > jogador.manaMax:
        jogador.mana = jogador.manaMax

def adicionarHabilidade (jogador):
    habilidade = []
    if "HRDA" in jogador.habilidades:
        habilidade.append("(HRDA) Custo: [2] Rap de Academia -- Aumenta o dano do proximo ataque, se o inimigo sobreviver o jogador e atordoado ")
    if "HMR" in jogador.habilidades:
        habilidade.append("(HMR) Custo: [5] Multilação Regenerativa -- Perde até 2 de vida, causa dano baseado em INT + ATT, o dano causado é convertido em vida")
    if "HOAM" in jogador.habilidades:
        habilidade.append("(HOAM) Custo: [2] Organizar a Mente -- Recupera um pouco de vida, o proximo ataque será Critico")
    if "HCL" in jogador.habilidades:
        habilidade.append("(HCL) Custo: [2] Cura Leve -- Recupera vida baseado na sua inteligencia")
    for elemento in habilidade:
        if elemento not in jogador.habilidadesDesc:
            jogador.habilidadesDesc.append(elemento)

def calculaDano(atacante, defensor):
    mitiga = (defensor.defesa/100)+1
    vidaReal = defensor.vidaMax*mitiga
    atacante.danoReal = int((atacante.dano * defensor.vidaMax)/vidaReal)
    

def atacar(jogador, monstro, efeito):

    jogador.dano = (jogador.ataque + (random.randint(0, int(jogador.ataque*0.7))))
    calculaDano(jogador, monstro)
    if random.randint(0, 100) < jogador.critico or jogador.criticoGarantido == True:
        jogador.danoReal *= 2
        print("DANO CRITICO!!!")
        jogador.foiCritico = True
    Artefacts.golpeGanancioso(jogador, monstro)        
    Artefacts.cabeloColorido(jogador)
    Artefacts.lagrimaBerserker(jogador, efeito)
    jogador.danoReal += jogador.danoAumentado
    monstro.vida -= jogador.danoReal
    vidaLimite(jogador)
    jogador.danoAumentado = 0
    jogador.criticoGarantido = False
    jogador.foiCritico = False
    jogador.passar = True
    print(f"Você inflinge {jogador.danoReal}(-{jogador.dano-jogador.danoReal}) pontos de dano")

    
def monstroAtacar(jogador, monstro):
    monstro.dano = (monstro.ataque + (random.randint(0, int(monstro.ataque*0.7))))
    calculaDano(monstro, jogador)
    if "ACD" in jogador.artefatos:
        jogador.mana += int(monstro.danoReal/2)
        print(f"você recupera {int(monstro.danoReal/2)} pontos de mana")
    if "AMDA" in jogador.artefatos:
        jogador.danoAumentado = int(monstro.danoReal/2)
        print("A dor te motiva, seu proximo ataque causa dano extra")
    print(f"Você sofreu {int(monstro.danoReal)}(-{int(monstro.dano-monstro.danoReal)}) pontos de dano\n")
    if jogador.vida == NULL:
        jogador.vida = 0
    jogador.vida -= int(monstro.danoReal)
    

def status(jogador):
    print(f"STATUS {jogador.nome} \nVida : {jogador.vida}\nAtaque : {jogador.ataque}\nDefesa : {jogador.defesa}\n")
    return "\b"


def statusMonstro(monstro):
    print(f"STATUS {monstro.nome} \nVida : {monstro.vida}\nAtaque : {monstro.ataque}\nDefesa : {monstro.defesa}\n")
    return "\b"


def continuar():
    input("PRESSIONE ENTER PARA CONTINUAR")

#Loja



def todosOsStatus(jogador):
    print(f"Vida: {jogador.vida}")
    print(f"Ataque: {jogador.ataque}")
    print(f"Inteligencia: {jogador.inteligencia}")
    print(f"Mana: {jogador.mana}")
    print(f"Defesa: {jogador.defesa}")
    print(f"Ouro: {jogador.ouro}")
    print(f"Habilidades: {jogador.habilidades}")
    print(f"Artefatos: {jogador.artefatos}")
    print(f"Critico: {jogador.critico}")

def apresentacaoDeClasse(classe, caracteristica):
  print(f"""{classe.classe}, {caracteristica}
  ATAQUE:       {classe.ataque}
  DEFESA:       {classe.defesa}
  VIDA:         {classe.vida}
  INTELIGENCIA: {classe.inteligencia}
  """)