#QUESTAO 1 calcular fatorial 

def f(n):
    if (n == 0 or n == 1):
        return 1
    if n > 1:
        return f(n - 1) * n

#QUESTAO 2 Informar se um numero inteiro diferente de zero e um numero primo.

def p(n):
    if(n<1):
        return "Numero invalido, insira um valor positivo"
    for i in range(1,n+1):
        if(n%(i+1) == 0):
            return "Nao eh primo"
        else:
            return "Eh primo"
        
#QUESTAO 3 Calcular o MDC de tres numeros inteiros maiores que zero.

def mdc(m,n,o):
    a = m
    b = n
    c = o
    resto = 0
    for i in range (0,1):
        if(b%a == 0):
            b=a
        else:
            while(a%b != 0):
                resto = a%b
                if(resto != 0):
                    a = b
                    b = resto
            b=resto
            a=c
    return b


            

#QUESTAO 4 Calcular o MMC de tres numeros inteiros maiores que zero.

def mmc(m,n,o):
    a = m
    b = n
    c = o
    cont = 1
    aux = 2
    mmc = 1
    
    while ((a != 1) or (b != 1) or (c != 1)): #nao me pergunte o porque de
                                              #funcionar com or, a logica seria
                                              #and, mas ele para na hora que ve
                                              #o primeiro 1

        if(a%aux != 0 and b%aux != 0 and c%aux != 0):
            aux+=1
        if(a%aux == 0 or b%aux == 0 or c%aux == 0):

            if(a%aux == 0):
                a=a/aux
            if(b%aux == 0):
                b=b/aux
            if(c%aux == 0):
                c=c/aux
            mmc=aux*mmc
            
    return mmc

#QUESTAO 5 Calcular PA dado 3 numeros, primeiro termo, razao e o numero de termos



def pa(m,n,o):

    if(m<1 or n<1 or o<1):
        return ("Insira os tres digitos maiores que zero")
        

    print m,", "
    for i in range (o-1):
        m=m+n
        print m,", "


#QUESTAO 6 Calcular PG dado 3 numeros, primeiro termo, razao e o numero de termo
def pg(m,n,o):

    if(m<1 or n<1 or o<1):
        return ("Insira os tres digitos maiores que zero")
        

    print m,", "
    for i in range (o-1):
        m=m*n
        print m,", "

#QUESTAO 7 Calcular Media do aluno
def media(m,n,o):
    media=(m+n+o)/3

    if(media<4):
        return "reprovado"
    elif(media>=4 and media<7):
        return "Final"
    else:
        return "Aprovado"



#QUESTAO 8 Calcular multiplicacao so usando soma

def mult(m,n):
    fator=m
    for i in range(n-1):
        m=m+fator
    return m


#QUESTAO 9 Dividir somente com subtracao

def div(m,n):
    div=0
    while(m>=n):
        m=m-n
        div+=1
    return div


#QUESTAO 10 calcular o resto somente com subtracao

def resto(m,n):
    div=0
    while(m>=n):
        m=m-n
        div+=1
    return m




    
