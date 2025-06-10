# Formatando números decimais e valores monetários
nome = "Pedro"
idade = 30
altura = 1.75
salario = 3000.5

print(f'O nome é: {nome}')
print(f'A idade é: {idade}')
print(f'A altura é: {altura}')


valorUS = f'{salario:,.2f}'

print(f'O salario em US é {valorUS}')

valorBR = valorUS.replace(".", "a").replace(",",".").replace("a", ",")

print(f'O salario BR é: {valorBR}')

 # Formatando número decimal
 # Formatando valor monetário

# Incluir essa vírgula para separar milhares


# Substituições com .replace
# 1. Trocar vírgula por placeholder #
# 2. Trocar ponto por vírgula
# 3. Trocar placeholder por ponto
