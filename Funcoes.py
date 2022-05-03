import random
def recebeDano (vida, dano):
    vida -= dano
    return (vida)

def statusJogador(jogador):
    print(f"STATUS DO JOGADOR\nVida : {jogador.vida}\nAtaque : {jogador.ataque}\nDefesa : {jogador.defesa}")
    return "\b"

def vidaLimite (vida, vidaMax):
    if vida > vidaMax:
        vida = vidaMax
        return vida

def calculaDano(vida, ataque, criticoGarantido, critico,/
                foiCritico, passivaCabeloColorido, danoMitigadoMonstro, danoAumentado):

    dano = ataque + random.randint(1, ataque)
    if criticoGarantido == True:
        dano*=2
        criticoGarantido = False
        print("DANO CRITICO!!!")
        foiCritico = True
    elif random.randint(0, 100) < critico:
        dano *= 2
        print("DANO CRITICO!!!")
        foiCritico = True
    if passivaCabeloColorido == True and foiCritico == True:
        dano += danoMitigadoMonstro
    dano += danoAumentado
    dano -= danoMitigadoMonstro
    vida -= dano
    print(f"Você inflinge {dano}(-{danoMitigadoMonstro}) pontos de dano")
    return vida

def status(vida, ataque, defesa):
    print(f"STATUS DO MONSTRO\nVida : {vida}\nAtaque : {ataque}\nDefesa : {defesa}")
    return "\b"

def continuar():
    input("PRESSIONE ENTER PARA CONTINUAR")