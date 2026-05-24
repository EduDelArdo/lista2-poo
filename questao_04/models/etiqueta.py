class Etiqueta:
    def __init__(self, destinatario: str, endereco: str):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> str:
        return f"[ETIQUETA] Para: {self.destinatario} | Endereço: {self.endereco}"