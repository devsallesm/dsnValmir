# Entrada de dados
vendaCartaoX = float(input('Vendas no cartão X: '))
vendaCartaoY = float(input('Vendas no cartão Y: '))
vendaPIX = float(input('Vendas no PIX: '))
transacoesPIX = float(input('Transacoes no PIX: '))
vendaDinheiro = float(input('Vendas no dinheiro: '))

# Cálculos das taxas
taxaCartaoX = vendaCartaoX * 0.025
taxaCartaoY = vendaCartaoY * 0.03
taxaPIX = vendaPIX * 0.90
# Valor bruto total
vendasBruto = vendaCartaoX + vendaCartaoY + vendaPIX + vendaDinheiro
# Cálculos financeiros
impostos = float(vendasBruto * 0.09)
custoFixo =  float(vendasBruto * 0.17)
totalTaxas = taxaCartaoX + taxaCartaoY + taxaPIX
vendasLiquido = vendasBruto - totalTaxas - custoFixo - impostos
# Relatório
print(f'o valor bruto das vendas é: {vendasBruto}')
print(f'a taxa total do cartão X é: {taxaCartaoX}')
print(f'a taxa total do cartão Y é: {taxaCartaoY}')
print(f'o valor total dos impostos é: {impostos}')
print(f'o valor total dos custos fixos é: {custoFixo}')
print(f'o valor Liquido das vendas é: {vendasLiquido}')
