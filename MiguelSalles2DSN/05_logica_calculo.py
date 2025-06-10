# Contexto: Subtrair impostos e custos fixos do valor bruto
# Não posso calcular o valor líquido sem calcular os impostos e as taxas antes.
valorBruto = int(input("digite um valor bruto"))
impostos = float(valorBruto * 0.09)
custoFixo =  float(valorBruto * 0.15)

valorLiquido = valorBruto - (impostos + custoFixo)

print()