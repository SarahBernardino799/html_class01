'''

faça um programa que leia a largura e altura da parede em metros e calcule a sua area e a quantidade de tinta

necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area 2m²

'''

largura=float(input("digite a LARGURA da parede:"))

altura=float(input("digite a ALTURA da parede:"))

area=largura*altura

print("a sua parede tem a dimensão de {:2} x {:2} e a sua área é de {:2} m².".format(largura,altura,area))

tinta=area/2

print("-"*70)

print("para pintar a sua parede, você precisara de {:2} litros de tinta.".format(tinta))