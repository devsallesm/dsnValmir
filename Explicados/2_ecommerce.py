# A classe 'Produto' define o molde para cada produto do nosso sistema.
class Produto:
    # O construtor define as características de um produto.
    def __init__(self, id_produto, nome, preco, quantidade_em_estoque):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    # O método 'vender' tenta subtrair a quantidade vendida do estoque.
    def vender(self, quantidade):
        # O 'if' verifica se há estoque suficiente.
        if self.quantidade_em_estoque >= quantidade:
            # Se sim, subtrai a quantidade do estoque.
            self.quantidade_em_estoque -= quantidade
            # Retorna True para indicar que a venda foi bem-sucedida.
            return True
        else:
            # Se não, retorna False.
            return False

# A classe 'Pedido' é o molde para cada pedido feito no sistema.
class Pedido:
    # O construtor define os atributos iniciais do pedido.
    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self.itens = []  # O pedido começa com uma lista vazia de itens.
        self.valor_total = 0.0
        self.status = "pendente"

    # O método 'adicionar_item' adiciona um produto ao pedido.
    def adicionar_item(self, produto, quantidade):
        # Chama o método 'vender' do OBJETO 'produto'.
        # Isso é um exemplo de como objetos interagem.
        if produto.vender(quantidade):
            # Se a venda foi bem-sucedida, adiciona o item à lista do pedido.
            self.itens.append({'produto': produto, 'quantidade': quantidade})
            # Atualiza o valor total do pedido.
            self.valor_total += produto.preco * quantidade
            print(f"Adicionado {quantidade} de {produto.nome} ao pedido {self.id_pedido}")
            return True
        return False

    # O método 'finalizar_pedido' atualiza o status do pedido.
    def finalizar_pedido(self):
        self.status = "concluido"
        print(f"Pedido {self.id_pedido} finalizado.")

# --- Código principal ---

# Criamos objetos 'Produto' para o nosso "estoque".
smartphone = Produto("P001", "Smartphone X", 1500.00, 10)
camiseta = Produto("P002", "Camiseta Cool", 50.00, 25)

# Criamos um objeto 'Pedido'.
meu_pedido = Pedido("PED001")

# Adicionamos itens ao pedido, chamando o método da classe 'Pedido'.
meu_pedido.adicionar_item(smartphone, 2)
meu_pedido.adicionar_item(camiseta, 5)

# Imprimimos o estoque atual dos produtos para ver a mudança.
print(f"Estoque atual do {smartphone.nome}: {smartphone.quantidade_em_estoque}")
print(f"Estoque atual da {camiseta.nome}: {camiseta.quantidade_em_estoque}")

# Finalizamos o pedido.
meu_pedido.finalizar_pedido()