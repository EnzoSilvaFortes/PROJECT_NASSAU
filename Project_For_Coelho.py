from typing import List, Dict, Optional

# Cada produto é um dicionário com descrição, quantidade e valor
Produto = Dict[str, object]

# Estoque inicial vazio
estoque: List[Produto] = []

# Função para adicionar produto
def adicionar_produto(descricao: str, quantidade: int, valor: float) -> None:
    for produto in estoque:
        if produto["descricao"] == descricao:
            print(f"Produto '{descricao}' já existe no estoque!")
            return
    estoque.append({"descricao": descricao, "quantidade": quantidade, "valor": valor})
    print(f"Produto '{descricao}' adicionado com sucesso.")

# Função para consultar estoque
def consultar_estoque(descricao: str) -> Optional[Produto]:
    for produto in estoque:
        if produto["descricao"] == descricao:
            return produto
    print(f"Produto '{descricao}' não encontrado.")
    return None

# Função para atualizar preço
def atualizar_preco(descricao: str, novo_valor: float) -> None:
    for produto in estoque:
        if produto["descricao"] == descricao:
            produto["valor"] = novo_valor
            print(f"Preço do produto '{descricao}' atualizado para {novo_valor}.")
            return
    print(f"Produto '{descricao}' não encontrado. Não foi possível atualizar o preço.")

# --- Aqui um exemplo de uso ---
if __name__ == "__main__":
    adicionar_produto("Camiseta", 10, 39.90)
    adicionar_produto("Caneta", 100, 1.50)
    adicionar_produto("Camiseta", 5, 42.00)  # Tenta adicionar produto já existente

    print(consultar_estoque("Camiseta"))
    print(consultar_estoque("Lápis"))  # Produto que não existe

    atualizar_preco("Caneta", 1.80)
    atualizar_preco("Lápis", 0.50)  # Produto que não existe