# Importa o módulo 'datetime' para trabalhar com datas.
import datetime

# A classe 'Tarefa' é o molde para cada tarefa no nosso app.
class Tarefa:
    # O construtor define a descrição, data de vencimento e um status inicial.
    def __init__(self, descricao, data_vencimento):
        self.descricao = descricao
        # Converte a string de data para um objeto de data.
        self.data_vencimento = datetime.datetime.strptime(data_vencimento, "%Y-%m-%d").date()
        self.concluida = False

    # O método 'marcar_como_concluida' altera o status da tarefa.
    def marcar_como_concluida(self):
        self.concluida = True
        print(f"Tarefa '{self.descricao}' marcada como concluída.")

    # O método 'editar_descricao' muda a descrição da tarefa.
    def editar_descricao(self, nova_descricao):
        self.descricao = nova_descricao
        print(f"Descrição da tarefa atualizada para: '{self.descricao}'.")

# A classe 'GerenciadorDeTarefas' é o molde do nosso aplicativo.
class GerenciadorDeTarefas:
    # O construtor cria a lista que irá armazenar os objetos 'Tarefa'.
    def __init__(self):
        self.lista_de_tarefas = []

    # O método 'adicionar_tarefa' cria um novo objeto 'Tarefa' e o adiciona à lista.
    def adicionar_tarefa(self, descricao, data_vencimento):
        nova_tarefa = Tarefa(descricao, data_vencimento)
        self.lista_de_tarefas.append(nova_tarefa)
        return nova_tarefa

    # O método 'listar_tarefas' percorre a lista e exibe cada tarefa.
    def listar_tarefas(self):
        print("\n--- Minhas Tarefas ---")
        # O 'for' percorre cada objeto 'tarefa' dentro da 'lista_de_tarefas'.
        for tarefa in self.lista_de_tarefas:
            # Verifica o status da tarefa para decidir qual texto imprimir.
            status = "✅ Concluída" if tarefa.concluida else "⏳ Pendente"
            print(f"- {tarefa.descricao} (Vencimento: {tarefa.data_vencimento}) - Status: {status}")
        print("----------------------")

# --- Código principal ---

# Criamos um objeto 'GerenciadorDeTarefas', que será nosso app.
meu_app_tarefas = GerenciadorDeTarefas()

# Adicionamos tarefas usando o método do gerenciador, que por sua vez cria objetos 'Tarefa'.
tarefa1 = meu_app_tarefas.adicionar_tarefa("Comprar pão", "2025-07-28")
tarefa2 = meu_app_tarefas.adicionar_tarefa("Estudar POO em Python", "2025-08-05")

# Listamos as tarefas.
meu_app_tarefas.listar_tarefas()

# Acessamos um objeto 'Tarefa' específico e chamamos seu método.
tarefa1.marcar_como_concluida()

# Listamos novamente para ver a mudança.
meu_app_tarefas.listar_tarefas()