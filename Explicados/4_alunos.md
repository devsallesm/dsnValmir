```mermaid
classDiagram
    class Aluno {
        - matricula: string
        - nome: string
        - idade: int
        - notas: list<float>
        - disciplinas_cursadas: list<string>
        + adicionar_nota(nota: float): void
        + calcular_media(): float
        + esta_aprovado(media_minima: float): bool
        + adicionar_disciplina(disciplina: string): void
    }

    class Turma {
        - nome_turma: string
        - ano: int
        - alunos_da_turma: list<Aluno>
        + adicionar_aluno(aluno: Aluno): void
        + listar_alunos_aprovados(media_minima: float): void
    }

    Turma "1" --> "*" Aluno : contém