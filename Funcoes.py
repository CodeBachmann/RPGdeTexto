from asyncio.windows_events import NULL
import random
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
        habilidade.append("(HRDA[2]) Rap de Academia -> Aumenta o dano do proximo ataque, se o inimigo sobreviver o jogador e atordoado ")
    if "HMR" in jogador.habilidades:
        habilidade.append("(HMR[5]) Multilação Regenerativa -> Perde até 2 de vida, causa dano baseado em INT + ATT, o dano causado é convertido em vida")
    if "HOAM" in jogador.habilidades:
        habilidade.append("(HOAM[2]) Organizar a Mente -> Recupera um pouco de vida, o proximo ataque será Critico")
    for elemento in habilidade:
        if elemento not in jogador.habilidadesDesc:
            jogador.habilidadesDesc.append(elemento)

def calculaDano(atacante, defensor):
    atacante.dano = (atacante.ataque + (random.randint(0, atacante.ataque)))
    mitiga = (defensor.defesa/100)+1
    vidaReal = defensor.vidaMax*mitiga
    atacante.danoReal = int((atacante.dano * defensor.vidaMax)/vidaReal)
    

def atacar(jogador, monstro):

    calculaDano(jogador, monstro)
    if random.randint(0, 100) < jogador.critico or jogador.criticoGarantido == True:
        jogador.dano *= 2
        print("DANO CRITICO!!!")
        jogador.foiCritico = True
    if "ACC" in jogador.artefatos and jogador.foiCritico == True:
        jogador.danoReal += int(jogador.dano - jogador.danoReal)
        jogador.vida += int(jogador.dano/4)
        print("Você penetra a armadura do oponente e rouba sua vitalidade ")
    jogador.danoReal += jogador.danoAumentado
    monstro.vida -= jogador.danoReal
    vidaLimite(jogador)
    jogador.danoAumentado = 0
    jogador.criticoGarantido = False
    jogador.foiCritico = False
    jogador.passar = True
    print(f"Você inflinge {jogador.danoReal}(-{jogador.dano-jogador.danoReal}) pontos de dano")

    
def monstroAtacar(jogador, monstro):
    calculaDano(monstro, jogador)
    if "ACD" in jogador.artefatos:
        jogador.mana += int(monstro.danoReal/2)
        print(f"você recupera {int(monstro.danoReal/2)} pontos de mana")
    if "AMDA" in jogador.artefatos:
        jogador.danoAumentado = int(monstro.danoReal/2)
        print("A dor te motiva, seu proximo ataque causa dano extra")
    if monstro.danoReal < 0:
        monstro.danoReal = 0
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
def comprarNaLoja (jogador):
    fecharLoja = False
    itemLojaPocao = random.randint(0,100)
    itemLojaArtefato = random.randint(0,100)
    itemLojaMagia = random.randint(0,100)
    pocaoComprado = False
    artefatoComprado = False
    habilidadeComprado = False

    while not fecharLoja:
        compraRealizada = False
        input("Você adentra a loja.. !:")
        print("Sair da loja(S)")
        if itemLojaPocao <= 34:
            print("Pocao de Ataque - 50g(PA)")
            podeComprarPocao = "PA"
            precoPocao = 50
        elif itemLojaPocao <= 67:
            print("Pocao de Defesa - 50g(PD)")
            podeComprarPocao = "PD"
            precoPocao = 50
        elif itemLojaPocao <= 100:
            podeComprarPocao = "PI"
            precoPocao = 50
            print("Pocao de Inteligencia - 50g(PI)")
        if itemLojaArtefato <= 50:
            podeComprarArtefato = "ALG"
            precoArtefato = 120
            print(f"Lagrima do Berserker 120g(ALB)")
        elif itemLojaArtefato <= 100:
            podeComprarArtefato = "AGG"
            precoArtefato = 132
            print(f"Golpe Ganancioso 132g(AGG)")
        if itemLojaMagia <= 100:
            podeComprarHabilidade = "HCL"
            precoMagia = 100
            print(f"Pergaminho de magia Cura Leve (HCL) 100g")
        print("Recuperar 5 pontos de Vida - 25g(RV)")
        while not compraRealizada:
            print(f"Saldo atual: {jogador.ouro}")
            decisao = input("O que você deseja comprar: ")
            if decisao == "RV" and jogador.ouro >= 25:
                jogador.ouro -= 25
                jogador.vida += 5
                vidaLimite(jogador)

            elif decisao == podeComprarPocao and not pocaoComprado:
                if precoPocao <= jogador.ouro:
                    if decisao == "PA":
                        jogador.ataque += 1
                        jogador.ouro -= precoPocao
                        pocaoComprado = True
                        print("Item comprado com sucesso")
                    elif decisao == "PD":
                        jogador.defesa += 10
                        jogador.ouro -= precoPocao
                        pocaoComprado = True
                        print("Item comprado com sucesso")
                    elif decisao == "PI":
                        jogador.inteligencia += 1
                        jogador.ouro -= precoPocao
                        pocaoComprado = True
                        print("Item comprado com sucesso")
                else:
                    print("Você não tem ouro o suficiente")

            elif decisao == podeComprarArtefato and not artefatoComprado:
                if decisao == "ALB":
                    if precoArtefato <= jogador.ouro:
                        jogador.artefatos.append(podeComprarArtefato)
                        jogador.ouro -= precoArtefato
                        artefatoComprado = True
                        print("Item comprado com sucesso")
                elif decisao == "AGG":
                    if precoArtefato <= jogador.ouro:
                        jogador.artefatos.append(podeComprarArtefato)
                        jogador.ouro -= precoArtefato
                        artefatoComprado = True
                        print("Item comprado com sucesso")

            elif decisao == podeComprarHabilidade and not habilidadeComprado:
                if decisao == "HCL":
                    if precoMagia <= jogador.ouro:
                        jogador.habilidades.append(podeComprarHabilidade)
                        jogador.ouro -= precoArtefato
                        habilidadeComprado = True
                        print("Item comprado com sucesso")
            elif decisao == "S":
                compraRealizada = True
                fecharLoja = True
                print("Você sai da loja")

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

def apresentacaoDeClasses1(classes):

  cabeca = f'Classe - Ata - Def - Vid - Int'
  atributos = ''
  nome = ''

  for c in classes:
    espacoAtributo = 4
    espacoClasse = 8 - len(c[0].classe)

    # Ifs para que o tamanho, em string, das variáveis seja o mesmo
    # caso o valor seja menor q 10, ou seja, tenha apenas um digito, é adicionado um espaço antes
    ataque       = '' if c[0].ataque > 9 else ' '  
    defesa       = '' if c[0].defesa > 9 else ' '  
    vida         = '' if c[0].vida > 9 else ' '  
    inteligencia = '' if c[0].inteligencia > 9 else ' '  

    nome         += f'{c[0].classe}{" "*espacoClasse}'
    ataque       += f'{c[0].ataque}{" "*espacoAtributo} '
    defesa       += f'{c[0].defesa}{" "*espacoAtributo} '
    vida         += f'{c[0].vida}{" "*espacoAtributo} '
    inteligencia += f'{c[0].inteligencia}\n'

    atributos += nome + ataque + defesa + vida + inteligencia


  print('\n')
  print(cabeca)
  print(atributos)
  print('\n')


def apresentacaoDeClasses2(classes):

  cabeca       = f'CLASSES:   '
  ataque       = f'Ata:       '
  defesa       = f'Def:       '
  vida         = f'Vid:       '
  inteligencia = f'Int:       '

  for classe in classes:
    espaco = len(classe[0].classe) + 5
    
    # ifs para que o tamanho, em string, das variáveis seja o mesmo
    # caso o valor seja menor q 10, ou seja, tenha apenas um digito, é adicionado um espaço antes 
    ataque       += '' if classe[0].ataque > 9 else ' '  
    defesa       += '' if classe[0].defesa > 9 else ' '  
    vida         += '' if classe[0].vida > 9 else ' '  
    inteligencia += '' if classe[0].inteligencia > 9 else ' '  

    cabeca       += f'{classe[1]} {classe[0].classe} - '
    ataque       += f'{classe[0].ataque}{" "*espaco}'
    defesa       += f'{classe[0].defesa}{" "*espaco}'
    vida         += f'{classe[0].vida}{" "*espaco}'
    inteligencia += f'{classe[0].inteligencia}{" "*espaco}'


  print(f"""{cabeca}
  {ataque}  
  {defesa}  
  {vida}
  {inteligencia}
  """)
  print('\n')
  print('\n')





print('\n ~~teste apresentacaoDeClasses1 apresentacaoDeClasses2~~~~')
import personagens
apresentacaoDeClasses1( [[personagens.Sabel, '(S)'], 
                        [personagens.Santos, '(SA)'], 
                        [personagens.Reisch, '(R)']] )

apresentacaoDeClasses2( [[personagens.Sabel, '(S)'], 
                        [personagens.Santos, '(SA)'], 
                        [personagens.Reisch, '(R)']] )                        