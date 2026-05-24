from models.impressao_protocol import Imprimivel

def processar_impressao(item: Imprimivel) -> None:
    """Função global exigida pelo slide que aceita qualquer objeto compatível com o protocolo."""
    print("Enviando para a fila de impressão...")
    resultado = item.imprimir()
    print(resultado)