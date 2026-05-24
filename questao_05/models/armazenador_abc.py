from abc import ABC, abstractmethod

class Armazenador(ABC):
    
    @abstractmethod
    def salvar(self, dado: str) -> str:
        """Método abstrato obrigatório para todas as subclasses formais."""
        pass


class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado: str) -> str:
        return f"[ARQUIVO] Dado gravado com sucesso no arquivo .txt: '{dado}'"


class ArmazenadorBanco(Armazenador):
    def salvar(self, dado: str) -> str:
        return f"[BANCO] Executando comando INSERT para salvar: '{dado}'"