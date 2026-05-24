from typing import Protocol

class Imprimivel(Protocol):
    def imprimir(self) -> str:
        """Contrato estrutural usando Protocol. Qualquer objeto com este método é compatível."""
        pass