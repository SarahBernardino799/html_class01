'''
crie uma lista diga a quantidade de convidados altere o nome 
do convidado do index 4 para alex,
delete o ultimo convidado,
adcione um novo convidado no index 0,
para finalizar crie uma lista de sobrenomes e junte a convidados para formar outros nomes
'''
convidados=["ana",'julia',"andreza",'agnes',"yelena","claudia",'agatha',"sophia",'morgana',"evellyn"]
print(len(convidados))
convidados[4]="alex"
print(convidados)
convidados.pop()
print(convidados)
convidados.insert(0,"roberta")
print(convidados)
sobrenomes=["silva","oliveira","machado","alves","costa","amorim","gomes","nascimento","bernardino","goes"]
for x in convidados:
  for y in sobrenomes:
    print(x, y)