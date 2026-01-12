numeros = {1, 2, 2, 3, 3, 4, 5, 5}
lista_numeros = [1, 2, 2, 3, 3, 4, 5, 5]

print(set(lista_numeros))

print(numeros)

frutas = {"maçã", "banana", "uva"}

frutas.add("abacaxi")
frutas.add("uva")

print(frutas)

frutas.remove("banana")

print(frutas)

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

print(conjunto1 | conjunto2)
print(conjunto1 & conjunto2)
print(conjunto1 - conjunto2)
print(conjunto2 - conjunto1)

for fruta in frutas:
    print(fruta)