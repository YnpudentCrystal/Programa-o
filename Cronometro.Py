import tkinter as tk
import time

class Cronometro:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Cronômetro")
        self.janela.geometry("200x100")

        self.label_tempo = tk.Label(self.janela, text="00:00:00", font=("Arial", 24))
        self.label_tempo.pack(pady=10)

        self.botao_iniciar = tk.Button(self.janela, text="Iniciar", command=self.iniciar_cronometro)
        self.botao_iniciar.pack(side=tk.LEFT, padx=10)

        self.botao_parar = tk.Button(self.janela, text="Parar", command=self.parar_cronometro)
        self.botao_parar.pack(side=tk.RIGHT, padx=10)

        self.iniciado = False
        self.tempo_inicial = 0

    def iniciar_cronometro(self):
        if not self.iniciado:
            self.tempo_inicial = time.time()
            self.atualizar_cronometro()
            self.iniciado = True

    def parar_cronometro(self):
        self.iniciado = False

    def atualizar_cronometro(self):
        if self.iniciado:
            tempo_atual = int(time.time() - self.tempo_inicial)
            horas = tempo_atual // 3600
            minutos = (tempo_atual % 3600) // 60
            segundos = (tempo_atual % 3600) % 60

            tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            self.label_tempo.configure(text=tempo_formatado)

        self.janela.after(1000, self.atualizar_cronometro)

cronometro = Cronometro()
cronometro.janela.mainloop()