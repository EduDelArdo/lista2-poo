from models.armazenador_abc import ArmazenadorArquivo, ArmazenadorBanco
from models.armazenador_protocol import ArmazenadorNuvem
from repository.sistema_repository import SistemaRepository
from ui.terminal_ui import TerminalUI

def main():
    repo = SistemaRepository()
    interface = TerminalUI(repo)

    # Instanciando os armazenadores exigidos
    arq = ArmazenadorArquivo()
    banco = ArmazenadorBanco()
    nuvem = ArmazenadorNuvem()

    # Executando os testes conforme os requisitos do slide
    print("\n--- TESTANDO SALVAMENTO FORMAL (ABC) ---")
    interface.executar_salvamento_formal(arq, "Configurações Locais do Sistema")
    interface.executar_salvamento_formal(banco, "id_usuario: 404, nome: Eduardo")
    print("-" * 50)

    print("\n--- TESTANDO SALVAMENTO FLEXÍVEL (PROTOCOL) ---")
    interface.executar_salvamento_flexivel(nuvem, "Código Fonte do Projeto PBL")
    interface.executar_salvamento_flexivel(arq, "Logs de Sessão Temporários")
    print("-" * 50)

    # Exibe o histórico de logs consolidados
    interface.exibir_relatorio_final()

if __name__ == "__main__":
    main()