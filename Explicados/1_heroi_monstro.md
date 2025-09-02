```mermaid
classDiagram
    class Personagem {
        - nome: string
        - vida: int
        - forca: int
        + atacar(alvo: Personagem): void
        + esta_vivo(): bool
    }

    