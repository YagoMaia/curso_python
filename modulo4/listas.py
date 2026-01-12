valores = [1, 2, 3, 4, 5]
nomes = ["Yago", "Lucas", "José"]

conjunto = [1, 2, 3, "Yago", "Andre", 3.14, 2.5, True, False]

# print(type(valores))
print(conjunto)

# print(conjunto[-1])
# print(conjunto[0:5])

conjunto[0] = 20
conjunto[5] = 50

print(conjunto)

nomes = ["Yago"]
print(nomes)
nomes.append(5)
print(nomes)
nomes.insert(0, "Jose")

print(nomes)

nomes.pop()
nomes.remove("Jose")
del nomes[0]


print(nomes)

for elemento in conjunto:
    print(f"ELEMENTO: {type(elemento)}")


print(conjunto)
print(len(conjunto))

i = 0

while (i <= len(conjunto) - 1):
    print(f"ELEMENTO: {type(conjunto[i])}")
    # i = i + 1
    i+=1