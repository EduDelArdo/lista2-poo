from typing import List
from models.notificador_abc import Notificador

class CentralNotificacoes:
    def __init__(self):
        self._notificadores: List[Notificador] = []

    def adicionar_notificador(self, notificador: Notificador) -> None:
        self._notificadores.append(notificador)

    def enviar_para_todos(self, mensagem: str) -> None:
        print(f"\n --- INICIANDO TRANSMISSÃO DE ALERTA GERAL ---")
        for n in self._notificadores:
            print(n.notificar(mensagem))
        print("------------------------------------------------\n")