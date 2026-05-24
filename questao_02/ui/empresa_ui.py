from questao_02.repository.empresa_repository import EmpresaRepository

class EmpresaUI:
    def __init__(self, repository: EmpresaRepository):
        self.repository = repository

    def gerar_relatorio_folha(self) -> None:
        print(f"\n==================================================")
        print(f"    FOLHA FINANCEIRA - {self.repository.nome_empresa.upper()} ")
        print("==================================================")
        
        colaboradores = self.repository.obter_todos_os_funcionarios()
        
        if not colaboradores:
            print("Nenhum funcionário cadastrado no sistema.")
            return

        total_custo_folha = 0.0
        
        for f in colaboradores:
            print(f.obter_dados())
            # Chamada polimórfica: o Python decide o cálculo com base na subclasse real
            pagamento = f.calcular_pagamento()
            print(f"Saldo Líquido a Receber: R$ {pagamento:.2f}")
            print("-" * 50)
            total_custo_folha += pagamento
            
        print(f"CUSTO TOTAL DA FOLHA DE PAGAMENTO: R$ {total_custo_folha:.2f}\n")