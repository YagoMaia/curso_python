# nome_usuario = "Jose"

# def saudacao(nome="Visitante"):
#     print("Bem Vindo!", nome)

# saudacao()

# numero = 5 #Variavel fora do escopo

# def mostrar_numero():
#     numero = 10 #Variavel dentro do espoco da função
#     print(f"(Função) O número é {numero}")

# mostrar_numero()
# print(f"O número é {numero}")

def soma(numero1, numero2):
    return numero1 + numero2

numero1 = 5
numero2 = 4

# soma_numeros = soma(numero1, numero2)

print(soma(numero1, numero2))

# def numeros(*args):
#     print(args)

# numeros(1,2,3, 5, 6, 7 ,8, [21,4,5], "Striung")

def exibir_informacoes(**kwargs):
    print(kwargs)
    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")

exibir_informacoes(nome = "Yago", idade= 52)

def funcao_geral(arg1, arg2 = "nome", *args, **kwargs):
    print(arg1, arg2, args, kwargs)

funcao_geral(1, "Y", 1,2,3,4,5, idade = 10)