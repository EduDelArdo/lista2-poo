from typing import List
from questao_01.models.midia import Midia

class PlataformaRepository:
    def __init__(self):
        self._catalogo: List[Midia] = []

    def adicionar_midia(self, midia: Midia) -> None:
        self._catalogo.append(midia)

    def obter_todas_as_midias(self) -> List[Midia]:
        return self._catalogo