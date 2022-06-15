from mailbox import NotEmptyError


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


    save = open(r'C:\Users\Aluno\Documents\GitHub\RPGdeTexto\save.txt','r')
    listaNumeros = save.read().splitlines()
    save.close()
    save = open(r'C:\Users\Aluno\Documents\GitHub\RPGdeTexto\saveHabilidades.txt','r')
    listaHabilidades = save.read().splitlines()
    save.close()
    save = open(r'C:\Users\Aluno\Documents\GitHub\RPGdeTexto\saveArtefatos.txt')
    listaArtefatos = save.read().splitlines()
    save.close()
    cont = 0
    for i in listaNumeros:
        listaNumeros[cont] = i.replace("'", "")
        listaNumeros[cont] = listaNumeros[cont].replace("[","")
        listaNumeros[cont] = listaNumeros[cont].replace("]","")
        print(listaNumeros[cont])
        cont+=1
    for i in listaHabilidades:
        listaHabilidades[cont] = i.replace("'", "")
        listaHabilidades[cont] = listaHabilidades[cont].replace("[","")
        listaHabilidades[cont] = listaHabilidades[cont].replace("]","")
        print(listaHabilidades[cont])
        cont+=1
    for i in listaArtefatos:
        listaArtefatos[cont] = i.replace("'", "")
        listaArtefatos[cont] = listaArtefatos[cont].replace("[","")
        listaArtefatos[cont] = listaArtefatos[cont].replace("]","")
        print(listaArtefatos[cont])
    cont = 0
    nome = jogador.nome
    print(nome)
    for i in listaNumeros:
        linha = i.split(', ')
        if nome in linha:
            salvado.contSave = cont
        cont+= 1

    for i in listaHabilidades:
        linha = i.split(', ')
        if nome in linha:
            salvado.contSave = cont
        cont+= 1

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
        for i in salvado.listaNumerosSave:
            texto2 += (str(i)+', ')
        listaArtefatos[salvado.contSave] = texto2
    else:
        listaArtefatos.append(salvado.listaNumerosSave)
    
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
    save = open(r'C:\Users\Aluno\Documents\GitHub\RPGdeTexto\save.txt','w+')
    save.write(textoNovo)
    save.close()

    textoNovo = ''
    for i in listaHabilidades:
        textoNovo += (str(i)+"\n")
    textoNovo = textoNovo.replace("'", "")
    textoNovo = textoNovo.replace("[", "")
    textoNovo = textoNovo.replace("]", "")
    save = open(r'C:\Users\Aluno\Documents\GitHub\RPGdeTexto\saveHabilidades.txt','w+')
    save.write(textoNovo)
    save.close()

    textoNovo = ''
    for i in listaArtefatos:
        textoNovo += (str(i)+"\n")
    textoNovo = textoNovo.replace("'", "")
    textoNovo = textoNovo.replace("[", "")
    textoNovo = textoNovo.replace("]", "")
    save = open(r'C:\Users\Aluno\Documents\GitHub\RPGdeTexto\saveArtefatos.txt','w+')
    save.write(textoNovo)
    save.close()

'''
def carregar(jogador, salvado):
    save = open(r'C:\Users\Aluno\Documents\GitHub\RPGdeTexto\save.txt','r')
    listasNumeros = save.read().splitlines()
    save.close()

    for i in listaNumeros:
        listaNumeros[i] = i.replace("'", "")
        #listaNumeros[i] = i.replace("[", "")
        #listaNumeros[i] = i.replace("]", "")
        
    
    for i in listaNumeros:
        print(i)
    cont = 0
    for i in listaNumeros:
        linha = i.split(', ')
        if jogador.nome in linha:
            salvado.contSave = cont
        cont+= 1
    
    texto2 = linha[salvado.contSave]
    lista2 = texto2.split(', ')

    lista2 = texto2
    jogador.nome = lista2[0]
    jogador.vida = int(lista2[1])
    jogador.vidaMax = int(lista2[2])
    jogador.ataque = int(lista2[3])
    jogador.defesa = int(lista2[4])
    jogador.classe = lista2[5]
    jogador.critico = int(lista2[6])
    jogador.inteligencia = int(lista2[7])
    jogador.mana = int(lista2[8])
    jogador.manaMax = int(lista2[9])
    jogador.regenMana = int(lista2[10])

    jogador.ouro = int(lista2[11])
    jogador.caminhado = int(lista2[12])
'''
    