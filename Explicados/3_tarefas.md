```mermaid
classDiagram
    class Tarefa {
        - descricao: string
        - data_vencimento: Date
        - concluida: boolean
        + marcar_como_concluida(): void
        + editar_descricao(nova_descricao: string): void
    }

    class GerenciadorDeTarefas {
        - lista_de_tarefas: list<Tarefa>
        + adicionar_tarefa(descricao: string, data_vencimento: string): Tarefa
        + listar_tarefas(): void
    }

    GerenciadorDeTarefas "1" --> "*" Tarefa : gerencia