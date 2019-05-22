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
tamanho = 20
placar  = 60 

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
    pos_x   = randrange(0, largura-tamanho, 20)
    pos_y   = randrange(0, altura-tamanho-placar, 20)
    maca_x  = randrange(0, largura-tamanho, 20)
    maca_y  = randrange(0, altura-tamanho-placar, 20)
    velocidade_x = 0
    velocidade_y = 0
    CobraXY     = []
    cont = 0

    #Comprimento da cobra, a variável vai limitar o comprimento da cobra
    CobraComp   = 1


    pontos = 0


#Loop principal
    while sair:
#Menu
        while menu:
            fundo.fill(blue)
            texto("JOOJ", white, 100, 400, 100 )
            
            texto("Iniciar", white, 30, 405, 255)
            
            texto("Instruções", white, 30, 405, 295)
            
            texto("Sair", white, 30, 405, 335)
            if cont == 0: 
                pygame.draw.rect(fundo, red, [380, 260, 10, 10])
            elif cont == 1:
                pygame.draw.rect(fundo, red, [380, 300, 10, 10])
            elif cont == 2:
                pygame.draw.rect(fundo, red, [380, 340, 10, 10])
            elif cont == 3:
                cont = 0
            elif cont == -1:
                cont = 2
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                    menu = False
                    instruçoes = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        cont += 1
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        cont -= 1
                    if event.key == pygame.K_RETURN:
                        if cont == 0:
                            menu = False
                            fimdejogo = False
                            sair = True
                            instruçoes = False 
                        elif cont == 1:
                            sair = True
                            fimdejogo = False
                            menu = False
                            instruçoes = True
                        elif cont == 2:
                            sair = False
                            fimdejogo = False
                            menu = False
                            instruçoes = False

            pygame.display.update()
        while instruçoes:
            fundo.fill(blue)
            texto("made by Cainhu69", black, 30, 0, 0)
            texto("Você é um quadrado preto (cobrinha) que tem que comer um quadrado vermelho(maçã)", black, 30, 0, 30)
            texto("Conforme você vai comendo maçãs, o tamanho da cobrinha e os pontos aumentam", black, 30, 0, 60)
            texto("Você não pode ir diretamente pra uma direção contrária a que estava antes(ex: cima e baixo)", black, 30, 0, 90)
            texto("Você não pode bater nas paredes", black, 30, 0, 120)

            
            texto("Voltar", white, 30, 25, 605)
            pygame.draw.rect(fundo, red, [5, 610, 10, 10])
            for event in pygame.event.get():        
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                    menu = False
                    instruçoes = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        instruçoes = False
                        menu = True
                        sair = True
                        fimdejogo = False
            pygame.display.update()
            cont = 0
#Game over
        while fimdejogo:
            fundo.fill(blue)
            texto('Game over', black, 50, 65, 30)
            
            texto("Continuar", white, 30, 405, 255)
            
            texto("Sair",white, 30, 405, 295)
            texto("Pontuação final: "+str(pontos), black, 30, 70, 80)
            if cont == 0: 
                pygame.draw.rect(fundo, red, [380, 260, 10, 10])
            elif cont == 1:
                pygame.draw.rect(fundo, red, [380, 300, 10, 10])
            elif cont == 2:
                cont = 0
            elif cont == -1:
                cont = 1
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                    menu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        cont += 1
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        cont -= 1
                    if event.key == pygame.K_RETURN:
                        if cont == 0:
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
                        if cont == 1:
                            sair = False
                            fimdejogo = False
                            menu = False


#In game
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                sair = False
                menu = False
                fimdejogo = False
                instruçoes = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT and velocidade_x != tamanho) or (event.key == pygame.K_a and velocidade_x != tamanho):
                    velocidade_y = 0    
                    velocidade_x = - tamanho
                if (event.key == pygame.K_RIGHT and velocidade_x != -tamanho) or (event.key == pygame.K_d and velocidade_x != -tamanho):
                    velocidade_y = 0
                    velocidade_x = tamanho
                if (event.key == pygame.K_UP and velocidade_y != tamanho) or (event.key == pygame.K_w and velocidade_y != tamanho):
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if (event.key == pygame.K_DOWN and velocidade_y != -tamanho) or (event.key == pygame.K_s and velocidade_y != -tamanho):
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
            texto("Pontuação: "+str(pontos), white, 40, 10, altura-40)
            
            if pos_x == maca_x and pos_y == maca_y:
                maca_x  = randrange(0, largura-tamanho, 20)
                maca_y  = randrange(0, altura-tamanho-placar, 20)
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