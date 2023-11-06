#crie um programa que leia quanto dinheiro a pessoa tem e mostre quantos dolares ela pode comprar

#CONSIDERE US$ 1,00= R$5,03// Libras 1,00= R$6,13// Euros1,00=R$5,34

real=float(input("quanto dinheiro você tem?"))

dolar=real/5.03

libras=real/6.13

euros=real/5.34

print("com R${} você pode comprar {:.00f} dolares, {:.00f} libras ou {:.00f} euros.".format(real,dolar,libras,euros))
print("-"*100)
print("obrigada por utilizar a Tecpay, volte sempre!")