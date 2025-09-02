# A classe 'Aluno' é o molde para cada aluno.
class Aluno:
    # O construtor define as informações iniciais de um aluno.
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.notas = []  # Lista para armazenar as notas.
        self.disciplinas_cursadas = []  # Lista para armazenar as disciplinas.

    # O método 'adicionar_nota' adiciona uma nota à lista.
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)

    # O método 'calcular_media' usa a lista de notas para calcular a média.
    def calcular_media(self):
        if not self.notas:
            return 0.0
        # 'sum' soma os itens da lista, 'len' conta quantos itens há na lista.
        return sum(self.notas) / len(self.notas)

    # O método 'esta_aprovado' verifica se a média do aluno atinge o mínimo.
    def esta_aprovado(self, media_minima):
        # Chama o método 'calcular_media' do próprio objeto 'aluno'.
        return self.calcular_media() >= media_minima

# A classe 'Turma' é o molde para cada turma.
class Turma:
    # O construtor define o nome e ano da turma.
    def __init__(self, nome_turma, ano):
        self.nome_turma = nome_turma
        self.ano = ano
        self.alunos_da_turma = []  # Lista para armazenar objetos 'Aluno'.

    # O método 'adicionar_aluno' adiciona um objeto 'Aluno' à lista da turma.
    def adicionar_aluno(self, aluno):
        self.alunos_da_turma.append(aluno)
        print(f"{aluno.nome} adicionado(a) à turma {self.nome_turma}.")

    # O método 'listar_alunos_aprovados' percorre a lista de alunos da turma.
    def listar_alunos_aprovados(self, media_minima):
        print(f"\n--- Alunos Aprovados na Turma {self.nome_turma} ---")
        for aluno in self.alunos_da_turma:
            # Chama o método 'esta_aprovado' de cada objeto 'aluno'.
            if aluno.esta_aprovado(media_minima):
                print(f"- {aluno.nome} (Média: {aluno.calcular_media():.2f})")

# --- Código principal ---

# Criamos objetos 'Aluno' para os nossos "alunos".
aluno_maria = Aluno("2025001", "Maria Silva", 16)
aluno_joao = Aluno("2025002", "João Souza", 17)

# Adicionamos notas aos alunos chamando o método de cada objeto.
aluno_maria.adicionar_nota(8.5)
aluno_maria.adicionar_nota(7.0)

aluno_joao.adicionar_nota(6.0)
aluno_joao.adicionar_nota(5.5)

# Criamos um objeto 'Turma'.
turma_a = Turma("3A - Técnico em TI", 2025)

# Adicionamos os alunos à turma.
turma_a.adicionar_aluno(aluno_maria)
turma_a.adicionar_aluno(aluno_joao)

# Listamos os alunos aprovados da turma, usando o método da turma que, por sua vez,
# chama os métodos de cada objeto 'aluno'.
turma_a.listar_alunos_aprovados(7.0)