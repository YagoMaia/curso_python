tupla = (1, 2, 3, 4, 5, "Yago", 3.154, True)
lista = [1, 2, 3, 4, 5]

print(type(tupla))
print(type(lista))

lista[2] = 5

print(tupla[0:2])

tupla1 = (1, 2, 3)
tupla2 = (4, 5 ,6)

tupla3 = tupla1 + tupla2

print(tupla3 * 3)

print(10 in tupla3)

tupla_convertida = tuple(lista)

print(type(tupla_convertida))
