class RelatorioSimples:
    def __init__(self, titulo: str):
        self.titulo = titulo

    def imprimir(self) -> str:
        return f"[RELATÓRIO] Título: {self.titulo} - Gerado com sucesso."