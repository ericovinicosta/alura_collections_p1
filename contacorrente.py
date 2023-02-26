class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return '[>>Codigo {} Saldo {}<<]'.format(self.codigo, self.saldo)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)