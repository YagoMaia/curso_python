pessoa = {
    "nome": "Pessoa 1",
    "idade": 52,
    "endereco": {
        "rua": "Rua A",
        "numero": 1
    },
    "pais": ["Mae", "Pai"]
}

print(pessoa["pais"][0])

lista_pessoas = [
    {
    "nome": "Pessoa 1",
    "idade": 52,
    "endereco": {
        "rua": "Rua A",
        "numero": 1
    },
    "pais": ["Mae", "Pai"]
},
{
    "nome": "Pessoa 2",
    "idade": 2,
    "endereco": {
        "rua": "Rua B",
        "numero": 2
    },
    "pais": ["Mae", "Pai"]
},
{
    "nome": "Pessoa 3",
    "idade": 75,
    "endereco": {
        "rua": "Rua C",
        "numero": 3
    },
    "pais": ["Mae", "Pai"]
}
]

lista_lista = [[1,2,3], [4,5,6], [7,8,9]]

for l in lista_lista:
    print(l[-1])

for pessoa in lista_pessoas:
    print(pessoa)