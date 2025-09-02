```mermaid
classDiagram
    class Produto {
        - id_produto: string
        - nome: string
        - preco: float
        - quantidade_em_estoque: int
        + vender(quantidade: int): bool
    }

    class Pedido {
        - id_pedido: string
        - itens: list<Produto>
        - valor_total: float
        - status: string
        + adicionar_item(produto: Produto, quantidade: int): bool
        + finalizar_pedido(): void
    }

    Pedido "1" --> "*" Produto : contém