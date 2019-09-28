def valorpagamento(valor, diasatraso):
    '''
    função para calcular valor do pagamento
    '''

    if valor < 0:
        return None
    if diasatraso > 0:
        multa = valor * 0.03
        adicionalatraso = valor * diasatraso * 0.01
        return valor + multa + adicionalatraso
    else:
        return valor


'''
# Entrada de Dados
valor = 1
while (valor != 0):
    valor = float(raw_input('Informe o valor da prestacao: '))
    if (valor != 0):
        diasatraso = int(raw_input('Informe a quantidade de dias de atraso: '))
        print ("Valor a ser pago: %.2f" % valorPagamento(valor, diasatraso))
'''
