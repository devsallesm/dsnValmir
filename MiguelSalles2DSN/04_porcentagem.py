# Porcentagem na programação se calcula com decimal.
# 100% == 1
#  50% == 0.5
#  10% == 0.1
#   5% == 0.05

# Exibindo com print
print(f'desconto de {0.05 : .0%}')

# decimais em porcentagem para uma taxa de 3.27% 
taxa =  0.0234
print(f'desconto de {taxa : .1%}')

# Recebendo valor do usuário, calculando e exibindo
vendaCartao = float(input("Vendas no Cartao: R$ "))
taxaCartao = float(vendaCartao * 0.025)
print(f'Com taxa de {0.025: .1%} do o juros total é de {taxaCartao}')