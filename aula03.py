from biblioteca import estoque

nome=input("digite o nome do produto:")
valor=float(input("qual o valor unitario:"))
quantidade= int(input("quantos tem:"))

print(estoque(nome, quantidade, valor))
print(estoque)