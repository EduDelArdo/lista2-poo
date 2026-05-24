from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem: str) -> str:
        pass


class NotificadorEmail(Notificador):
    def notificar(self, mensagem: str) -> str:
        return f"[E-MAIL] Enviando mensagem corporativa: '{mensagem}'"


class NotificadorSMS(Notificador):
    def notificar(self, mensagem: str) -> str:
        return f"[SMS] Disparando torpedo para celular: '{mensagem}'"


class NotificadorApp(Notificador):
    def notificar(self, mensagem: str) -> str:
        return f"[PUSH APP] Alerta flutuante na tela do celular: '{mensagem}'"
