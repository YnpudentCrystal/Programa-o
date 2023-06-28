# Importe as bibliotecas necessárias
import pygame
import random

# Inicialize o Pygame
pygame.init()

# Defina as configurações do jogo
largura = 640
altura = 480
tamanho_bloco = 20
velocidade = 15

# Defina as cores
cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)

# Crie a janela do jogo
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")

# Defina a classe Snake
class Snake:
    def __init__(self):
        self.tamanho = 1
        self.posicao = [(largura / 2, altura / 2)]
        self.direcao = random.choice(['cima', 'baixo', 'esquerda', 'direita'])
    
    def mover(self):
        x, y = self.posicao[0]
        if self.direcao == 'cima':
            y -= tamanho_bloco
        elif self.direcao == 'baixo':
            y += tamanho_bloco
        elif self.direcao == 'esquerda':
            x -= tamanho_bloco
        elif self.direcao == 'direita':
            x += tamanho_bloco
        
        self.posicao.insert(0, (x, y))
        if len(self.posicao) > self.tamanho:
            self.posicao.pop()
    
    def mudar_direcao(self, nova_direcao):
        if nova_direcao == 'cima' and self.direcao != 'baixo':
            self.direcao = nova_direcao
        elif nova_direcao == 'baixo' and self.direcao != 'cima':
            self.direcao = nova_direcao
        elif nova_direcao == 'esquerda' and self.direcao != 'direita':
            self.direcao = nova_direcao
        elif nova_direcao == 'direita' and self.direcao != 'esquerda':
            self.direcao = nova_direcao
    
    def desenhar(self):
        for posicao in self.posicao:
            pygame.draw.rect(janela, cor_cobra, (posicao[0], posicao[1], tamanho_bloco, tamanho_bloco))

# Defina a classe Comida
class Comida:
    def __init__(self):
        self.posicao = (random.randint(0, largura - tamanho_bloco) // tamanho_bloco * tamanho_bloco,
                        random.randint(0, altura - tamanho_bloco) // tamanho_bloco * tamanho_bloco)
    
    def desenhar(self):
        pygame.draw.rect(janela, cor_comida, (self.posicao[0], self.posicao[1], tamanho_bloco, tamanho_bloco))

# Crie a cobra e a comida
cobra = Snake()
comida = Comida()

# Inicialize o relógio
relogio = pygame.time.Clock()

# Execução do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                cobra.mudar_direcao('cima')
            elif evento.key == pygame.K_DOWN:
                cobra.mudar_direcao('baixo')
            elif evento.key == pygame.K_LEFT:
                cobra.mudar_direcao('esquerda')
            elif evento.key == pygame.K_RIGHT:
                cobra.mudar_direcao('direita')

    cobra.mover()
    
    # Verifique se a cobra colidiu com a comida
    if cobra.posicao[0] == comida.posicao:
        cobra.tamanho += 1
        comida = Comida()
    
    # Verifique se a cobra colidiu consigo mesma ou com as bordas da janela
    if (cobra.posicao[0][0] < 0 or cobra.posicao[0][0] >= largura or
        cobra.posicao[0][1] < 0 or cobra.posicao[0][1] >= altura or
        cobra.posicao[0] in cobra.posicao[1:]):
        pygame.quit()
        quit()
    
    # Limpe a janela
    janela.fill(cor_fundo)
    
    # Desenhe a cobra e a comida
    cobra.desenhar()
    comida.desenhar()
    
    # Atualize a janela
    pygame.display.update()
    
    # Defina a taxa de quadros por segundo
    relogio.tick(velocidade)
