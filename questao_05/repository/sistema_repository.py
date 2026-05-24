from typing import List

class SistemaRepository:
    def __init__(self):
        self._historico_operacoes: List[str] = []

    def registrar_operacao(self, log: str) -> None:
        self._historico_operacoes.append(log)

    def obter_historico(self) -> List[str]:
        return self._historico_operacoes