# A classe 'Personagem' é o nosso molde
class Personagem:
    # O método '__init__' é o construtor.
    # Ele é chamado automaticamente quando criamos um novo objeto.
    # 'self' se refere ao próprio objeto que está sendo criado.
    # 'nome', 'vida' e 'forca' são os parâmetros que passamos.
    def __init__(self, nome, vida, forca):
        # 'self.nome = nome' cria um atributo 'nome' para o objeto
        # e atribui o valor do parâmetro 'nome' a ele.
        # O mesmo acontece para 'vida' e 'forca'.
        self.nome = nome
        self.vida = vida
        self.forca = forca

    # O método 'atacar' é a ação do personagem.
    # 'alvo' é o objeto 'Personagem' que está sendo atacado.
    def atacar(self, alvo):
        dano = self.forca
        # A vida do 'alvo' é reduzida pela força do atacante.
        alvo.vida -= dano
        # A função 'print' exibe uma mensagem no console.
        # Usamos f-strings (f"...") para incluir variáveis na string.
        print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano!")

    # O método 'esta_vivo' verifica se a vida do personagem é maior que zero.
    # 'return' retorna um valor (True ou False, neste caso).
    def esta_vivo(self):
        return self.vida > 0

# --- A partir daqui, o código principal do programa é executado ---

# Criamos o primeiro objeto, 'heroi', passando os valores para o construtor.
heroi = Personagem("Sir Lancelot", 100, 20)
# Criamos o segundo objeto, 'monstro', também passando seus valores.
monstro = Personagem("Dragão de Fogo", 150, 15)

# O laço 'while' continua a execução enquanto a condição for verdadeira.
# Aqui, a condição é que tanto o herói quanto o monstro estejam vivos.
while heroi.esta_vivo() and monstro.esta_vivo():
    # O herói chama seu próprio método 'atacar', passando o 'monstro' como alvo.
    heroi.atacar(monstro)
    # Se o monstro sobreviveu ao ataque, ele contra-ataca.
    if monstro.esta_vivo():
        monstro.atacar(heroi)
    print(f"Situação atual: {heroi.nome} Vida: {heroi.vida} | {monstro.nome} Vida: {monstro.vida}")
    print("========//========")

# Após o laço 'while' terminar, verificamos quem venceu.
if heroi.esta_vivo():
    print(f"\n{heroi.nome} venceu a batalha!")
else:
    print(f"\n{monstro.nome} venceu a batalha!")