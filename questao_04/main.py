from models.boleto import Boleto
from models.etiqueta import Etiqueta
from models.relatorio import RelatorioSimples
from ui.terminal_ui import processar_impressao

def main():
    print("\n==================================================")
    # 1. Criar os objetos exigidos no slide
    boleto = Boleto("34191.79001 01043", 250.50)
    etiqueta = Etiqueta("Jhemilly Sousa", "Av. Principal, 123 - Centro")
    relatorio = RelatorioSimples("Relatório de Desempenho PBL 01")

    # 2. Passar todos para a função de impressão genérica
    print("--- INICIANDO PROCESSAMENTO DE IMPRESSÃO ---")
    processar_impressao(boleto)
    print("-" * 50)
    processar_impressao(etiqueta)
    print("-" * 50)
    processar_impressao(relatorio)
    print("==================================================\n")

if __name__ == "__main__":
    main()