# Operações básicas numeros (int e float)

idade = 25
saldo = 500.50

soma_idade = idade + 10
soma_saldo = saldo + 100

sub_idade = idade - 10
sub_saldo = saldo - 500

mult_idade = idade * 4
mult_saldo = saldo * 2

div_idade = idade / 24 # 25/24 -> 1
div_saldo = saldo / 10 # 500.25 -> 50.03

div_idade_int = idade // 24 # 25//24 -> 1
div_idade_resto = idade % 24 # 25/24 -> 1

# print(2**3)

# Operações com Booleanos

verdadeiro = True
falso = False

# AND, OR, NOT

# AND -> Analisa se os dois/todos os valores são verdadeiros

# print(True and True)
# print(True and False)


# Or ele analisa se existe algum valor verdadeiro

# print(True or False)
# print(False or False)

# Not opostos do que estou analisando

print(not True)

# Operações com strings

string_1 = "Olá"
string_2 = "Mundo"

print(string_1 + "-=-" + string_2)
print(string_1*3)

exemplo = "12345"

print(exemplo[0])

print(exemplo[0:3])

print(exemplo[-1])