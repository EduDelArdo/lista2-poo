from questao_02.models.funcionario import FuncionarioAssalariado, FuncionarioHorista, FuncionarioComissionado
from questao_02.repository.empresa_repository import EmpresaRepository
from questao_02.ui.empresa_ui import EmpresaUI

def main():
    # 1. Inicializa o repositório
    empresa_repo = EmpresaRepository("Tech Solutions ICET")

    # 2. Cria as instâncias de funcionários 
    f1 = FuncionarioAssalariado("Eduardo Carvalho", "123.456.789-00", 6000.00)
    f2 = FuncionarioHorista("Jhemilly Souza", "987.654.321-11", 160, 40.00)
    f3 = FuncionarioComissionado("Nego Ney", "456.789.123-22", 50000.00, 0.06)

    # 3. Salva no repositório
    empresa_repo.cadastrar_funcionario(f1)
    empresa_repo.cadastrar_funcionario(f2)
    empresa_repo.cadastrar_funcionario(f3)

    # 4. Executa a interface de usuário para ver o relatório polimórfico
    view = EmpresaUI(empresa_repo)
    view.gerar_relatorio_folha()

if __name__ == "__main__":
    main()