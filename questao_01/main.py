from questao_01.models.midia import Video, Podcast, TextoNarrado
from questao_01.repository.plataforma_repository import PlataformaRepository
from questao_01.ui.terminal_ui import TerminalUI

def main():
    repo = PlataformaRepository()

    video_aula = Video("Casa automatica Minecraft", 45, "1080p")
    podcast_dev = Podcast("Vasco e Palmeiras, a união sinistra", 60, "Prof. Alternei")
    audiobook_clean = TextoNarrado("Naruto - Capítulo 1", 25, "Voz do Google")

    repo.adicionar_midia(video_aula)
    repo.adicionar_midia(podcast_dev)
    repo.adicionar_midia(audiobook_clean)

    interface = TerminalUI(repo)
    interface.exibir_catalogo_e_reproduzir()

if __name__ == "__main__":
    main()