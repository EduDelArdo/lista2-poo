from typing import Protocol

class Salvavel(Protocol):
    def salvar(self, dado: str) -> str:
        pass 


class ArmazenadorNuvem:
    def salvar(self, dado: str) -> str:
        return f"[NUVEM] Sincronizando e fazendo upload para o servidor: '{dado}'"