#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

def sair():
    print("Saindo....")
    time.sleep(1)
    exit(0)

def gerar(nome):
    try:
        if nome[-4:] == ".txt":
            arq = open(nome, 'r')
        else:
            arq = open(nome+'.txt', 'r')
    except:
        print("Arquivo não existente!!!")
        sair()
    print("Arquivo aberto com sucesso!!!")
    texto = arq.readlines()
    dados = []

    for linha in texto:
        a = linha.split('\n')
        dados += [a[0]]
	
    #print(dados)
    arq.close
    return dados

if __name__ == "__main__":
    param = sys.argv[1:]
    if param[0] == '--help':
        print("Aplicativo de ajustar TXT")
        print("Entrada: ")
        print("Nome do arquivo a ser ajeitado")
        print("Nome do arquivo de saida")
        print('\nEx.: ./AjeitarArq.py "Teste 1.txt" Teste 2"')
        exit(0)
    elif len(param) > 2:
        print("Parametros a mais passado!!")
        print("./AjeitarArq.py --help para ajuda")
        sair()

    elif len(param) < 2:
        print("Faltando parametros!!!")
        print("./AjeitarArq.py --help para ajuda")
        sair()

    dados = gerar(param[0])
    
    print("Ajustando o arquivo")
    aux = str('')
    #print(len(dados)-2)
    texto = []
    for i in range(len(dados)-2):
        if(dados[i+1] != ''):
            aux+=dados[i]
            if(dados[i] != '' and dados[i][-1] != ' '):
                texto += [aux.strip()]
                texto += ['\n']
                aux = str('')
            if(i+2 >= len(dados)-2):
                aux+=dados[i+1]
                print(aux)
                if dados[i+1][-1] != ' ':
                    if dados[i+1][-1] == '.':
                        print('entrou')
                        texto += [aux.strip()]
                        texto += ['\n']
                        aux=str('')
                    else:
                        aux+=' '
                try:
                    aux+=dados[i+2]
                    if dados[i+2][-1] != ' ':
                        if dados[i+2][-1] == '.':
                            texto += [aux.strip()]
                            texto += ['\n']
                            aux=str('')
                        else:
                            aux+=' '
                    aux+=dados[i+3]
                except:
                    pass            
                texto += [aux.strip()]
            # print(aux)
        else:
            aux+=dados[i]
            if(dados[i+2].isnumeric()):
                dados[i+2]=' '
                if(dados[i][-1] != '.'):
                    #print('Entrou',i)
                    i += 3
                    continue
            texto += [aux.strip()]
            texto += ['\n']
            aux = str('')
    #print(texto)
    # print('\n\n')
    # print(dados[5][-1])
    if param[1][-4:] == ".txt":
        arq = open(param[1], 'w')
    else:
        arq = open(param[1]+'.txt', 'w')
    arq.writelines(texto)
    arq.close