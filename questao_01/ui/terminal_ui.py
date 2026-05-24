from questao_01.repository.plataforma_repository import PlataformaRepository

class TerminalUI:
    def __init__(self, repository: PlataformaRepository):
        self.repository = repository

    def exibir_catalogo_e_reproduzir(self) -> None:
        print("\n==================================================")
        print("          PLATAFORMA DE MÍDIAS EDUCACIONAIS       ")
        print("==================================================")
        
        midias = self.repository.obter_todas_as_midias()
        
        if not midias:
            print("Nenhuma mídia cadastrada no sistema.")
            return

        print("\n---  EXECUTANDO REPRODUÇÃO POLIMÓRFICA ---")
        for midia in midias:
            print(midia.mostrar_info())
            print(midia.reproduzir())
            print("-" * 50)