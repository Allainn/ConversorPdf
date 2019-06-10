def gerar():
    arq = open('Teste.txt', 'r')
    texto = arq.readlines()
    dados = []

    for linha in texto:
        a = linha.split('\n')
        dados += [a[0]]
	
    #print(dados)
    arq.close
    return dados

dados = gerar()
aux = str('')
print(len(dados)-2)
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
            if dados[i+1][-1] != ' ':
                aux+=' '
            aux+=dados[i+2]
            if dados[i+2][-1] != ' ':
                aux+=' '
            try:
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
arq = open('Teste2.txt', 'w')
arq.writelines(texto)
arq.close