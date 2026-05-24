from models.notificador_abc import NotificadorEmail, NotificadorSMS, NotificadorApp
from models.central_notificacoes import CentralNotificacoes

def main():
    central = CentralNotificacoes()

    central.adicionar_notificador(NotificadorEmail())
    central.adicionar_notificador(NotificadorSMS())
    central.adicionar_notificador(NotificadorApp())

    central.enviar_para_todos("Manutenção programada no sistema Ecampus às 22h.")

if __name__ == "__main__":
    main()