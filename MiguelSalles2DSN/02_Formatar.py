# Combinação de aspas
print(f'Ele disse: "Olá, mundo!"')

# Escape de caracteres


# Separador e arredondamento
numero = 2.534 # Será arredondado para baixo. Se usar 2.535 será arredondado para cima.
print(f'o numero é {numero:,.2f}')

print() # Para pular uma linha

# Se sua string contém tanto aspas simples quanto aspas duplas, ou se ela tem múltiplas linhas, use aspas triplas.
frase_complexa = "Ele disse: \"Bem-vindo ao mundo do Python's f-strings!\""

# Com aspas triplas, você não precisa escapar nada
print(f'A frase foi: {frase_complexa}')


# Mensagem longa - Variavel nome recebe seu nome
nome = input('Digite seu nome ')
mensagem_longa = f'''
Prezado(a),

Gostaríamos de dar as boas-vindas ao {nome}.
Esperamos que sua experiência seja ótima.

Atenciosamente,
A Equipe
'''
print(mensagem_longa)

# 4. Com aspas triplas duplas (também para múltiplas linhas)
outra_mensagem = f"""
Relatório para o {nome}:
- Status: Ativo
- Nível: 10
"""
print(outra_mensagem)