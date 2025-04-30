def imprime_nome(nome):
    print(f"nome: {nome}")

def solicitarnome():
    nome=input("digite seu nome")
    return nome

def piramide(numero):
    for x in range(1,numero+1,1):
        for i in range(0,x):
            print(x,end=" ")
        print()

def contavogais(texto):
        count = 0
        for x in range(len(texto)):
             if texto[x] == "a" or texto[x] == "e" or texto[x] == "i" or texto[x] == "o" or texto[x] == "u":
                count = count + 1
        print(count)

def estoque(produto, quantidade,precounitario):
    valortotal=quantidade*precounitario
    return  valortotal

def numpositivonegativo(num):
    if num > 0:
        print("P")
    elif num == 0:
        print("Z")
    else:
        print("N")

def soma(*a):
    soma=0
    for x in range(len(a)):
        soma=soma+a[x]
    print(soma)