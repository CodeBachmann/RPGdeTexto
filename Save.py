from mailbox import NotEmptyError
def deletarSave(jogador, salvado):
    caminho = 'C:\\Users\\pcadmin\\Documents\\GitHub\\RPGdeTexto'

    save = open(caminho+'\\save.txt','r')
    listaNumeros = save.read().splitlines()
    save.close()
    save = open(caminho+'\\saveHabilidades.txt','r')
    listaHabilidades = save.read().splitlines()
    save.close()
    save = open(caminho+'\\saveArtefatos.txt','r')
    listaArtefatos = save.read().splitlines()
    save.close()
    cont = 0
    for i in listaNumeros:
        linha = i.split(', ')
        if jogador.nome in linha:
            salvado.contSave = cont
        cont+= 1

    listaNumeros.pop(salvado.contSave)
    listaArtefatos.pop(salvado.contSave)
    listaHabilidades.pop(salvado.contSave)
    textoNovo = ''
    for i in listaNumeros:
        textoNovo += (str(i)+"\n")
    textoNovo = textoNovo.replace("'", "")
    textoNovo = textoNovo.replace("[", "")
    textoNovo = textoNovo.replace("]", "")
    save = open(caminho+'\\save.txt','w+')
    save.write(textoNovo)
    save.close()
    textoNovo = ''
    for i in listaHabilidades:
        textoNovo += (str(i)+"\n")
    textoNovo = textoNovo.replace("'", "")
    textoNovo = textoNovo.replace("[", "")
    textoNovo = textoNovo.replace("]", "")
    save = open(caminho+'\\saveHabilidades.txt','w+')
    save.write(textoNovo)
    save.close()

    textoNovo = ''
    for i in listaArtefatos:
        textoNovo += (str(i)+"\n")
    textoNovo = textoNovo.replace("'", "")
    textoNovo = textoNovo.replace("[", "")
    textoNovo = textoNovo.replace("]", "")
    save = open(caminho+'\\saveArtefatos.txt','w+')
    save.write(textoNovo)
    save.close()

    
def escolherSave(jogador):
    caminho = 'C:\\Users\\pcadmin\\Documents\\GitHub\\RPGdeTexto'
    save = open(caminho+'\\save.txt','r')
    listaNumeros = save.read().splitlines()
    save.close()
    cont = 1
    for i in listaNumeros:
        print(str(cont) +' - '+ i)
        cont+=1
    escolha = int(input('Escolha o save (nmr): '))
    lista = listaNumeros[(escolha-1)].split(', ')
    jogador.nome = lista[0]

def salvar (jogador, salvado):
    salvado.listaNumerosSave = []
    salvado.listaHabilidades = []
    salvado.listaArtefatos = []
    salvado.listaNumerosSave.append(jogador.nome)
    salvado.listaNumerosSave.append(jogador.vida)
    salvado.listaNumerosSave.append(jogador.vidaMax)
    salvado.listaNumerosSave.append(jogador.ataque)
    salvado.listaNumerosSave.append(jogador.defesa)
    salvado.listaNumerosSave.append(jogador.classe)
    salvado.listaNumerosSave.append(jogador.critico)
    salvado.listaNumerosSave.append(jogador.inteligencia)
    salvado.listaNumerosSave.append(jogador.mana)
    salvado.listaNumerosSave.append(jogador.manaMax)
    salvado.listaNumerosSave.append(jogador.regenMana)
    salvado.listaNumerosSave.append(jogador.ouro)
    salvado.listaNumerosSave.append(jogador.caminhado)
    salvado.listaHabilidades.append(jogador.nome)
    salvado.listaHabilidades.append(jogador.habilidades)
    salvado.listaArtefatos.append(jogador.nome)
    salvado.listaArtefatos.append(jogador.artefatos)

    caminho = 'C:\\Users\\pcadmin\\Documents\\GitHub\\RPGdeTexto'
    save = open(caminho+'\\save.txt','r')
    listaNumeros = save.read().splitlines()
    save.close()
    save = open(caminho+'\\saveHabilidades.txt','r')
    listaHabilidades = save.read().splitlines()
    save.close()
    save = open(caminho+'\\saveArtefatos.txt','r')
    listaArtefatos = save.read().splitlines()
    save.close()
    cont = 0
    for i in listaNumeros:
        listaNumeros[cont] = i.replace("'", "")
        listaNumeros[cont] = listaNumeros[cont].replace("[","")
        listaNumeros[cont] = listaNumeros[cont].replace("]","")
        cont+=1
    cont = 0
    for i in listaHabilidades:
        listaHabilidades[cont] = i.replace("'", "")
        listaHabilidades[cont] = listaHabilidades[cont].replace("[","")
        listaHabilidades[cont] = listaHabilidades[cont].replace("]","")
        cont+=1
    cont = 0
    for i in listaArtefatos:
        listaArtefatos[cont] = i.replace("'", "")
        listaArtefatos[cont] = listaArtefatos[cont].replace("[","")
        listaArtefatos[cont] = listaArtefatos[cont].replace("]","")
        cont+=1
    cont = 0
    nome = jogador.nome
    for i in listaNumeros:
        linha = i.split(', ')
        if nome in linha:
            salvado.contSave = cont
        cont+= 1

    if salvado.contSave != 50:
        texto2 = ''
        for i in salvado.listaNumerosSave:
            texto2 += (str(i)+', ')
        listaNumeros[salvado.contSave] = texto2
    else:
        listaNumeros.append(salvado.listaNumerosSave)
    
    if salvado.contSave != 50:
        texto2 = ''
        for i in salvado.listaArtefatos:
            texto2 += (str(i)+', ')
        listaArtefatos[salvado.contSave] = texto2
    else:
        listaArtefatos.append(salvado.listaArtefatos)
    
    if salvado.contSave != 50:
        texto2 = ''
        for i in salvado.listaHabilidades:
            texto2 += (str(i)+', ')
        listaHabilidades[salvado.contSave] = texto2
    else:
        listaHabilidades.append(salvado.listaHabilidades)
    
    textoNovo = ''
    for i in listaNumeros:
        textoNovo += (str(i)+"\n")
    textoNovo = textoNovo.replace("'", "")
    textoNovo = textoNovo.replace("[", "")
    textoNovo = textoNovo.replace("]", "")
    save = open(caminho+'\\save.txt','w+')
    save.write(textoNovo)
    save.close()

    textoNovo = ''
    for i in listaHabilidades:
        textoNovo += (str(i)+"\n")
    textoNovo = textoNovo.replace("'", "")
    textoNovo = textoNovo.replace("[", "")
    textoNovo = textoNovo.replace("]", "")
    save = open(caminho+'\\saveHabilidades.txt','w+')
    save.write(textoNovo)
    save.close()

    textoNovo = ''
    for i in listaArtefatos:
        textoNovo += (str(i)+"\n")
    textoNovo = textoNovo.replace("'", "")
    textoNovo = textoNovo.replace("[", "")
    textoNovo = textoNovo.replace("]", "")
    save = open(caminho+'\\saveArtefatos.txt','w+')
    save.write(textoNovo)
    save.close()

def carregar(jogador, salvado):
    
    caminho = 'C:\\Users\\pcadmin\\Documents\\GitHub\\RPGdeTexto'
    save = open(caminho+'\\save.txt','r')
    listaNumeros = save.read().splitlines()
    save.close()
    save = open(caminho+'\\saveHabilidades.txt','r')
    listaHabilidades = save.read().splitlines()
    save.close()
    save = open(caminho+'\\saveArtefatos.txt','r')
    listaArtefatos = save.read().splitlines()
    
    cont = 0
    nome = jogador.nome
    for i in listaNumeros:
        linha = i.split(',')
        if nome in linha:
            salvado.contSave = cont
        cont+= 1
    numeros = listaNumeros[salvado.contSave].split(', ')
    habilidades = listaHabilidades[salvado.contSave].split(', ')
    artefatos = listaArtefatos[salvado.contSave].split(', ')
    numeros[-1].replace(',','')
    artefatos[-1].replace(',','')
    habilidades[-1].replace(',','')
    jogador.vida = int(numeros[1])
    jogador.vidaMax = int(numeros[2])
    jogador.ataque = int(numeros[3])
    jogador.defesa = int(numeros[4])
    jogador.classe = (numeros[5])
    jogador.critico = int(numeros[6])
    jogador.inteligencia = int(numeros[7])
    jogador.mana = int(numeros[8])
    jogador.manaMax = int(numeros[9])
    jogador.regenMana = int(numeros[10])
    jogador.ouro = int(numeros[11])
    jogador.caminhado = int(numeros[12])
    jogador.habilidades = []
    jogador.artefatos = []
    cont = 1
    for i in range((len(artefatos)-2)):
        jogador.artefatos.append(artefatos[cont])
        cont+=1
    cont = 1
    for i in range((len(habilidades)-2)):
        
        jogador.habilidades.append(habilidades[cont])
        cont+=1