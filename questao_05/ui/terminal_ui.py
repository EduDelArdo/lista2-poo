from models.armazenador_abc import Armazenador
from models.armazenador_protocol import Salvavel
from repository.sistema_repository import SistemaRepository

class TerminalUI:
    def __init__(self, repository: SistemaRepository):
        self.repository = repository

    def executar_salvamento_formal(self, armazenador: Armazenador, dado: str) -> None:
        """Exige um objeto que pertença estritamente à hierarquia baseada em ABC."""
        print("[Verificação Formal - ABC] Validando herança nominal...")
        resultado = armazenador.salvar(dado)
        self.repository.registrar_operacao(resultado)
        print(resultado)

    def executar_salvamento_flexivel(self, objeto: Salvavel, dado: str) -> None:
        """Aceita qualquer objeto que implemente a assinatura do protocolo Salvavel."""
        print("[Verificação Flexível - Protocol] Validando duck typing...")
        resultado = objeto.salvar(dado)
        self.repository.registrar_operacao(resultado)
        print(resultado)

    def exibir_relatorio_final(self) -> None:
        print("\n==================================================")
        print("          HISTÓRICO GERAL DE SALVAMENTOS          ")
        print("==================================================")
        historico = self.repository.obter_historico()
        for idx, log in enumerate(historico, 1):
            print(f"{idx}. {log}")
        print("==================================================\n")