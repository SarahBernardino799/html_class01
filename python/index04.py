'''

escreva um programa que pergunte a quantidade de horas que o computador alugado foi usado e

a quantidade de dias pelo qual foi alugado calcule o preço a pagar sabendo que o computador

custa 60 reais o dia, e 0,25 real a hora.

'''

horas=float(input("digite a quantidade de horas que o computador alugado foi utilizado: "))

dias=int(input("digite a quantidade de DIAS que o computador foi alugado: "))

pago=(dias*60)+(horas*0.25)

print("total a pagar R${:.2f}".format(pago))

print("-"*55)

print("Obrigada por alugar na Tec+")