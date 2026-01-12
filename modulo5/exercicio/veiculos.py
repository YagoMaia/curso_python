class Carro:
    def __init__(self, veiculo, diaria):
        self.veiculo = veiculo
        self.diaria = diaria

    def simular_aluguel(self, qtd_dias):
        total = self.diaria * qtd_dias
        return f"O valor total de {qtd_dias} dias será de {total}"

    def exibir_informacoes(self):
        return f"O veículo {self.veiculo} custa R$ {self.diaria} de diária."

    def aplicar_desconto(self, desconto):
        return self.diaria * (1 - desconto)

