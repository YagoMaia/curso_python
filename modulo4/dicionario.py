aluno = {"nome": "Jose", "idade": 43}
print(aluno)
print(type(aluno))

print(aluno["idade"])

aluno["curso"] = "Enfermagem"
aluno["idade"] = 25

# print(aluno["idades"])
print(aluno.get("idades"))

# del aluno["idade"]

idade_aluno = aluno.pop("idade")

print(aluno)
print(idade_aluno)

for chave in aluno.keys():
    print(f"A chave é: {chave}")

for valor in aluno.values():
    print(f"A chave é: {valor}")

for chave, valor in aluno.items():
    print(f"{chave}:{valor}")

aluno.clear()

print(aluno)