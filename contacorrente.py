from functools import total_ordering

@total_ordering
class ContaCorrente:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return '[>>Codigo {} Saldo {}<<]'.format(self._codigo, self._saldo)

    def __eq__(self, outro):
        if type(outro) != ContaCorrente:
            return False
        return self._codigo == outro._codigo and  self._saldo == outro._saldo

    def __lt__(self, outro):
        return self._saldo < outro._saldo

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)