
def recebeDano (a, b):
    a -= b
    return (a)

def statusJogador(jogador):
    print(f"STATUS DO JOGADOR\nVida : {jogador.vida}\nAtaque : {ataque}\nDefesa : {defesa}")
    return "\b"

def vidaLimite (vida, vidaMax):
    if vida > vidaMax:
        vida = vidaMax
        return vida

