from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo: str, duracao: int):
        self.titulo = titulo
        self.duracao = duracao

    def mostrar_info(self) -> str:
        return f"Mídia: {self.titulo} ({self.duracao} min)"

    @abstractmethod
    def reproduzir(self) -> str:
        pass

class Video(Midia):
    def __init__(self, titulo: str, duracao: int, resolucao: str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self) -> str:
        return f"Reproduzindo vídeo '{self.titulo}' na resolução {self.resolucao}..."

class Podcast(Midia):
    def __init__(self, titulo: str, duracao: int, apresentador: str):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self) -> str:
        return f"Tocando podcast '{self.titulo}', apresentado por {self.apresentador}..."

class TextoNarrado(Midia):
    def __init__(self, titulo: str, duracao: int, narrador: str):
        super().__init__(titulo, duracao)
        self.narrador = narrador

    def reproduzir(self) -> str:
        return f"Lendo texto '{self.titulo}', narrado por {self.narrador}..."