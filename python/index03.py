#faca um programa que leia um valor e depois mostre esse valor com o desconto de 5%

preco=float(input("digite o valor do produto: R$"))

new=preco*5/100

novo=preco-new

print("valor original do produto é R${:2},e seu desconto promocional é de 5%,o seu valor final é de R${:2} . Parabéns você economizou R${:2} Volte Sempre!".format(preco,novo,new))