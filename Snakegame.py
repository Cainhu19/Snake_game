import pygame
from random import randrange

#Cores
white = (255, 255, 255)
black = (0, 0, 0)
red   = (255, 0, 0) 
blue  = (0, 0, 255)
umacor = (115, 205, 252)

pygame.init()


#Variáveis globais:
largura = 1000
altura  = 700
tamanho = 10
placar  = 40 
#Definindo clock
clock = pygame.time.Clock()

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")

def texto(msg, cor, tam, x, y):
    fonte = pygame.font.SysFont(None, tam)
    texto1 = fonte.render(msg, True, cor)
    fundo.blit(texto1, [x, y])


def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, black, [XY[0], XY[1], tamanho, tamanho])

def maca(maca_x, maca_y):
    pygame.draw.rect(fundo, red, [maca_x, maca_y, tamanho, tamanho])

def jogo():
    sair = True
    menu = True
    fimdejogo = False
    instruçoes = False
    pos_x   = randrange(0, largura-tamanho, 10)
    pos_y   = randrange(0, altura-tamanho-placar, 10)
    maca_x  = randrange(0, largura-tamanho, 10)
    maca_y  = randrange(0, altura-tamanho-placar, 10)
    velocidade_x = 0
    velocidade_y = 0
    CobraXY     = []

    #Comprimento da cobra, a variável vai limitar o comprimento da cobra
    CobraComp   = 1


    pontos = 0


#Loop principal
    while sair:
#Menu
        while menu:
            fundo.fill(umacor)
            texto("JOOJ", white, 100, 400, 100 )
            pygame.draw.rect(fundo, black, [400, 250, 125, 27])
            texto("Iniciar(I)", white, 30, 405, 255)
            pygame.draw.rect(fundo, black, [400, 290, 135, 27])
            texto("Instruções(P)", white, 30, 405, 295)
            pygame.draw.rect(fundo, black, [400, 330, 75, 27])
            texto("Sair(S)", white, 30, 405, 335)
            #pygame.draw.circle(fundo, red, [440, 200], 5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                    menu = False
                    instruçoes = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        menu = False
                        fimdejogo = False
                        sair = True
                        instruçoes = False 
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
                        menu = False
                        instruçoes = False
                    if event.key == pygame.K_p:
                        sair = True
                        fimdejogo = False
                        menu = False
                        instruçoes = True
                '''if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 45 and y > 120 and x < 180 and y < 147:
                        menu = False
                        fimdejogo = False
                        sair = True
                        instruçoes = False
                    elif x > 190 and y > 120 and x < 265 and y < 147:
                        sair = False
                        fimdejogo = False
                        menu = False
                        instruçoes = False 
                    elif x > 45 and y > 120 and x < 205 and y < 187:
                        sair = True
                        fimdejogo = False
                        menu = False
                        instruçoes = True'''
        
            pygame.display.update()
        while instruçoes:
            fundo.fill(umacor)
            texto("made by Cainhu69", black, 30, 0, 0)
            texto("Você é um quadrado preto", black, 30, 0, 30)
            texto("(cobrinha) que tem que comer um ", black, 29, 0, 60)
            texto("quadrado vermelho(maçã)", black,  29, 0, 90)
            texto("Você não pode ir diretamente pra uma direção contrária a que estava antes(ex: cima e baixo)", black, 30, 0, 120)
            texto("Você não pode bater nas paredes", black, 30, 0, 150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                    menu = False
                    instruçoes = False
            pygame.display.update()
#Game over
        while fimdejogo:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                    menu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        menu = False
                        sair = True
                        fimdejogo = False
                        pos_x   = randrange(0, largura-tamanho, 10)
                        pos_y   = randrange(0, altura-tamanho-placar, 10)
                        maca_x  = randrange(0, largura-tamanho, 10)
                        maca_y  = randrange(0, altura-tamanho-placar, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY     = []
                        CobraComp   = 1
                        pontos = 0
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
                        menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 45 and y > 120 and x < 180 and y < 147:
                        menu = False
                        sair = True
                        fimdejogo = False
                        pos_x   = randrange(0, largura-tamanho, 10)
                        pos_y   = randrange(0, altura-tamanho-placar, 10)
                        maca_x  = randrange(0, largura-tamanho, 10)
                        maca_y  = randrange(0, altura-tamanho-placar, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY     = []
                        CobraComp   = 1
                        pontos = 0
                    elif x > 190 and y > 120 and x < 265 and y < 147:
                        sair = False
                        fimdejogo = False
                        menu = False
            fundo.fill(blue)
            texto('Game over', black, 50, 65, 30)
            pygame.draw.rect(fundo, black, [45, 120, 135, 27])
            texto("Continuar(C)", white, 30, 50, 125)
            pygame.draw.rect(fundo, black, [190, 120, 75, 27])
            texto("Sair(S)", white, 30, 195, 125)
            texto("Pontuação final: "+str(pontos), black, 30, 70, 80)
            pygame.display.update()
#In game
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                sair = False
                menu = False
                fimdejogo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = - tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho
        if sair:
            

            fundo.fill(white)
            pos_x+=velocidade_x
            pos_y+=velocidade_y

            #Lista da cobra
            CobraCabeca = []

            #A cabeça da cobra vai mudar de posição, devido a mudança da pos_x e pos_y
            CobraCabeca.append(pos_x)
            CobraCabeca.append(pos_y)
            
            CobraXY.append(CobraCabeca)
            cobra(CobraXY)

            maca(maca_x, maca_y)
            pygame.draw.rect(fundo, black, [0, altura-placar, largura, placar])
            texto("Pontuação: "+str(pontos), white, 20, 10, altura-30)
            
            if pos_x == maca_x and pos_y == maca_y:
                maca_x  = randrange(0, largura-tamanho, 10)
                maca_y  = randrange(0, altura-tamanho-placar, 10)
                CobraComp += 1
                pontos += 100

            if len(CobraXY) >= CobraComp:
                del CobraXY[0]
            
            if any(Bloco == CobraCabeca for Bloco in CobraXY[:-1]):
                fimdejogo = True

            
            if pos_x > largura - tamanho:
                fimdejogo = True
            if pos_x < 0:
                fimdejogo = True        
            if pos_y > altura - tamanho - placar:
                fimdejogo = True
            if pos_y < 0:
                fimdejogo = True


            pygame.display.update()
            clock.tick(15)

jogo()