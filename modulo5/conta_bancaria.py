class ContaBancaria:
    def __init__(self, saldo_inicial, nome_titular):
        self.__saldo = saldo_inicial
        self.titular = nome_titular

    def depositar(self, valor_deposito):
        self.__saldo += valor_deposito

    def sacar(self, valor_saque):
        if self.__verificar_saldo(valor_saque):
            self.__saldo -= valor_saque
            return
        print("Não é possível realizar esse saque !")

    def __verificar_saldo(self, valor_saque):
        return valor_saque <= self.__saldo

    def mostrar_saldo(self):
        print(f"O saldo atual de {self.titular} é {self.__saldo}")

conta_yago = ContaBancaria(100, "Yago")
conta_pedro = ContaBancaria(500.50, "Pedro")


conta_yago.titular = "Henrique Yago"
print(f"===== Saldo {conta_yago.titular} ======")
conta_yago.depositar(5000)
conta_yago.depositar(200)
conta_yago.sacar(3000)
conta_yago.__saldo = 100000000
# print(conta_yago.__verificar_saldo(10))
conta_yago.mostrar_saldo()

print("===== Saldo Pedro ======")
conta_pedro.depositar(10000)
conta_pedro.mostrar_saldo()