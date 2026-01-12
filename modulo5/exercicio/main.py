from veiculos import Carro
# import veiculos

def exibir_informacoes(carro):
    return f"O veículo {carro.veiculo} custa R$ {carro.diaria} de diária."

veiculo1 = Carro("Fiat Uno", 85.9)
veiculo2 = Carro("Gol", 54.2)

print(veiculo1.simular_aluguel(5))
print(exibir_informacoes(veiculo1))
print(veiculo1.exibir_informacoes())
print(veiculo1.aplicar_desconto(0.4))

# print(veiculo2.simular_aluguel(5))
# print(veiculo2.aplicar_desconto(0.6))