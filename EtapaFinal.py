import numpy as np
#Numpy, biblioteca responsável pela matriz
import re 
# regex inclui algumas funções, como replace e sub

#Etapa 1 analiza se tem tudo escrito
def etapa1(frase):
    #replace substitui apenas um caracetere avulso e re.sub substitui todas letras maiúsculas
    saida = frase.replace("(", '')
    saida = saida.replace(")", '')
    saida = saida.replace("^", '')
    saida = saida.replace('~', '')
    saida = saida.replace("→", '')
    saida = saida.replace("↔", '')
    saida = saida.replace("v", '')
    saida = re.sub('[A-Z]', '', saida)

    if saida == '' :
        #Se tá tudo ok, retorna 1
        return 1
    else:
        #Se tem coisa a mais retorna 0
        return 0

def etapa2(frase):
    i = 0
    #Quantidade de parentese abertos começa com 0
    qntdParentesesAbertos = 0
    #Esse while verifica se tudo tá escrito da forma correta
    while(i<len(frase)-1):

        if i== len(frase):
            break

        elif frase[i] == "(":
            #Quando abre um parentese
            qntdParentesesAbertos += 1
        
        elif frase[i].isalpha() and frase[i]!="v" and frase[i] != "^":
            x = i+1
            if frase[x] != "v" and frase[x] != "^" and frase[x]!= ")":
                #Se tiver coisa errada depois da variável
                return 0
                
        
        elif frase[i] == "v":
            x = i+1
            if frase[x] == "v" or frase[x] =="^" or frase[x] == ")":
                #Se o "ou" tiver escrito no lugar errado
                return 0
                
        
        elif frase[i] == ")":
            #Quando fecha um parentese
            qntdParentesesAbertos -= 1
        
        elif frase[i] == "→":
            x = i+1
            if frase[x] == "v" or frase[x] == "^" or frase[x] == "↔" or frase[x] == ")" or frase[x] == "→":
                #Se a condicional tiver no lugar errado
                return 0
                

        elif frase[i] == "↔":
            x = i+1
            if frase[x] == "v" or frase[x] == "^" or frase[x] == "↔" or frase[x] == ")" or frase[x] == "→":
                #Se a bicondicional tiver no lugar errado
                return 0
                
        i+=1
        
        if qntdParentesesAbertos != 0:
            #Se a quantidade de parentese for menor que 0
            return 0
        

    w = len(frase)
    #Tamanho da proposição
    y = w-1
    #tamanho da proposição menos 1
            
    if frase[y] ==")":
    #Se chegou até aqui vai tá tudo ok
        return 1
    elif frase[y].isalpha() and frase[y] != "v":
    #Se chegou até aqui vai tá tudo ok
        return 1
    else:
        return 0
    

#Analiza se é uma tautologia
def etapa3(stringue):
    #Vamo copiar a string passada
    patternstringue = stringue

    #Contadores para a matriz
    i=0
    j=0
    #cont é a quantidade de variáveis
    cont = 0
    #char são as variáveis
    char = []

    while(i<len(stringue)):
        #contando e organizando as variáveis
        if stringue[i].isalpha() and stringue[i] != "v":
            char.append(stringue[i])
            cont+=1
        i+=1
        
    if cont>3:
        #Se tivver mais de 3 variáveis retorna 2
        return 2

    tabelaverdade = np.zeros((2**cont, cont+1), dtype=str)
    #aqui ele cria a matriz com T e F no lugar da variável
    for i in range(len(tabelaverdade)):
        for j in range(len(tabelaverdade[0])-1):
            if j == 0:
                if i <= 2**(cont-1):
                    #Criando variávei 1 com TTTTFFFF
                    tabelaverdade[i][j] = 'T'
                else: 
                    tabelaverdade[i][j] = 'F'
        
            elif j == 1:
                #Criando variável 2 com TTFFTTFF
                if i%4 == 0 or i%4 == 1:
                    tabelaverdade[i][j] = 'T'
                else: 
                    tabelaverdade[i][j] = 'F'
            
            elif j == 2:
                #Criando a variável 3 com TFTFTFTF
                if i%2 == 0:
                    tabelaverdade[i][j] = 'T'
                else: 
                    tabelaverdade[i][j] = 'F'


    for i in range(len(tabelaverdade)):
        #Dicionário das operações
        stringue = patternstringue
        for word, initial in {"A":tabelaverdade[i][0], "B":tabelaverdade[i][1], "C":tabelaverdade[i][2]}.items():
            #Aqui substitui a expressão
            stringue = stringue.replace(word, initial)
        while(len(stringue) != 1):
            #Dicionário propriamente dito
            if "~T" in stringue:
                stringue = stringue.replace("~T", "F")
            elif "~F" in stringue:
                stringue = stringue.replace("~F", "T")
            elif "T^T" in stringue:
                stringue = stringue.replace("T^T", "T")
            elif "TvT" in stringue:
                stringue = stringue.replace("TvT", "T")
            elif "FvF" in stringue:
                stringue = stringue.replace("FvF", "F")
            elif "T^F" in stringue:
                stringue = stringue.replace("T^F", "F")
            elif "F^T" in stringue:
                stringue = stringue.replace("F^T", "F")
            elif "(T)" in stringue:
                stringue = stringue.replace("(T)", "T")
            elif "(F)" in stringue:
                stringue = stringue.replace("(F)", "F")
            elif "TvF" in stringue:
                stringue = stringue.replace("TvF", "T")
            elif "FvT" in stringue:
                stringue = stringue.replace("FvT", "T")
            elif "F^F" in stringue:
                stringue = stringue.replace("F^F", "F")
            elif "T→T" in stringue:
                stringue = stringue.replace("T→T", "T")
            elif "T→F" in stringue:
                stringue = stringue.replace("T→F", "F")
            elif "F→T" in stringue:
                stringue = stringue.replace("F→T", "T")
            elif "F→F" in stringue:
                stringue = stringue.replace("F→F", "T")
            elif "T↔T" in stringue:
                stringue = stringue.replace("T↔T", "T")
            elif "T↔F" in stringue:
                stringue = stringue.replace("T↔F", "F")
            elif "F↔T" in stringue:
                stringue = stringue.replace("F↔T", "F")
            elif "F↔F" in stringue:
                stringue = stringue.replace("F↔F", "T")

            
        tabelaverdade[i][-1] = stringue
                
    
    #Contador para analizar a ultima coluna da Matriz
    k = 0

    #Analise da ultima coluna da Matriz
    while(k<=i):
        if tabelaverdade[k][j+1] == 'F':
            #Se tiver ao menos um false, ele retorna 0
            return 0
        k+=1
    #Se for até o final, ele retorna 1
    return 1


print("Digite sua proposição")
#Input do User
frase = input()
if etapa1(frase) ==1:
    #Se a etapa 1 der certo
    print ("Lexico correto")
    if etapa2(frase) ==1:
        #Se a etapa 2 der certo
        print("Sintaxe correta")
        if etapa3(frase) ==1:
            #Se for uma tautologia
            print("É uma tautologia")
        elif etapa3(frase) ==2:
            #Se for grande demais
            print("Proposição muito grande")
        else:
            #Se não for uma tautologia
            print("Não é uma tautologia")
    
    else:
        print("Sintaxe errada")


else:
    print("Lexico errado")