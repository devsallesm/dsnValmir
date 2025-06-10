# Formatação de strings

> Python oferece várias formas de formatar strings. 
> O método mais moderno e recomendado é usando f-strings (formatação literal), que permite inserir variáveis e expressões diretamente na string.

#  F-Strings (Literais de String Formatadas) - O Método Moderno e Preferido
Introduzidas no Python 3.6, as f-strings são a forma mais legível, concisa e rápida de formatar strings.

## Sintaxe:
nome = "Maria"
idade = 30
print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")
Saída: Olá, meu nome é Maria e eu tenho 30 anos.

## O poder das f-strings está nos parâmetros que você pode adicionar após a variável, usando dois pontos (:).
[sign] (Sinal para Números)
+: Exibe o sinal para números positivos e negativos.
-: Exibe o sinal apenas para números negativos (padrão).
 (espaço): Insere um espaço na frente de números positivos e um sinal de menos para negativos.
num1 = 25
num2 = -25
print(f"Número com sinal +: {num1:+} e {num2:+}")
Saída: Número com sinal +: +25 e -25

print(f"Número com sinal ' ': {num1: } e {num2: }")
Saída: Número com sinal ' ':  25 e -25

# Dissecando o Código de Formatação: {numero:,.2f}
## Vamos quebrar o que acontece dentro das chaves:

numero É a variável que queremos formatar.
:  É o caractere especial que diz ao Python: "A formatação começa aqui!".
,  É o parâmetro para o separador de milhar.
.2 É o parâmetro de precisão, indicando que queremos 2 casas decimais.
f  É o parâmetro de tipo, que especifica que o número deve ser formatado como um ponto flutuante (float) de ponto fixo. O arredondamento é feito automaticamente.

A Ordem Correta dos Parâmetros
A "minilinguagem" de formatação tem uma ordem específica. Para os parâmetros mais comuns que você irá combinar, a regra geral é:
:[[alinhamento][largura]][separador][.precisão][tipo]
Isso significa que o separador de milhar (,) deve vir antes da precisão (.2f).