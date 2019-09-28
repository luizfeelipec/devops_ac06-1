class ContaCorrente:
    '''
    classe para conta corrente
    '''

    def __init__(self, numero, nomecorrentista, saldo=0.0):
        self.numero = numero
        self.alterar_nome(nomecorrentista)
        self.saldo = saldo

    def alterar_nome(self, nomecorrentista):
        '''
        metodo parar o nome
        '''
        self.nomecorrentista = nomecorrentista

    def deposito(self, valor):
        '''
        metodo para fazer deposito
        '''
        self.saldo += valor

    def saque(self, valor):
        '''
        metodo para fazer saque
        '''
        self.saldo -= valor


# TESTE DA CLASSE
'''conta = ContaCorrente(1222, 'pablo')
conta.alterarNome('julio')
conta.deposito(100)
print conta.saldo
conta.saque(100)
print conta.saldo'''
