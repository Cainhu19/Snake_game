import pygame
from random import randrange

#Cores
white = (255, 255, 255)
black = (0, 0, 0)
red   = (255, 0, 0) 
blue  = (0, 0, 255)
green = (0, 255, 0)
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
    config = False
    pos_x   = randrange(0, largura-tamanho, 20)
    pos_y   = randrange(0, altura-tamanho-placar, 20)
    maca_x  = randrange(0, largura-tamanho, 20)
    maca_y  = randrange(0, altura-tamanho-placar, 20)
    velocidade_x = 0
    velocidade_y = 0
    CobraXY     = []
    cont = 0
    contx = 0
    dificuldade = 0
    foud = 2
    sansundertale = 0
    

    #Comprimento da cobra, a variável vai limitar o comprimento da cobra
    CobraComp   = 1


    pontos = 0


#Loop principal
    while sair:
    
#Menu
        while menu:
            fundo.fill(blue)
            texto("Snake", white, 100, 400, 100 )
            
            texto("Iniciar", white, 30, 405, 255)
            
            texto("Instruções", white, 30, 405, 295)
    
            texto("Configurações", white, 30, 405, 335 )
            
            texto("Sair", white, 30, 405, 375)

            if cont == 0: 
                pygame.draw.rect(fundo, red, [380, 260, 10, 10])
            elif cont == 1:
                pygame.draw.rect(fundo, red, [380, 300, 10, 10])
            elif cont == 2:
                pygame.draw.rect(fundo, red, [380, 340, 10, 10])
            elif cont == 3:
                pygame.draw.rect(fundo, red, [380, 380, 10, 10])
            elif cont == 4:
                cont = 0
            elif cont == -1:
                cont = 3
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
                            config = False
                        elif cont == 1:
                            sair = True
                            fimdejogo = False
                            menu = False
                            instruçoes = True
                            config = False
                        elif cont == 2:
                            sair = True
                            fimdejogo = False
                            menu = False
                            instruçoes = False
                            config = True
                        elif cont == 3:
                            sair = False
                            fimdejogo = False
                            menu = False
                            instruçoes = False
                            config = False


            pygame.display.update()

        while instruçoes:

            fundo.fill(blue)
            texto("made by Cainhu", black, 30, 0, 0)
            texto("Você controla uma cobrinha e deve comer as maçãs para aumentar o tamanho e ganhar pontos", black, 30, 0, 40)
            texto("A cobra não pode colidir com o próprio corpo ou com uma parede, se não o jogo acaba", black, 30, 0, 80)

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
                        config = False
            pygame.display.update()
            cont = 0
#Configuraçoes
        cont = 0
        while config:
            fundo.fill(blue)
            texto("Configurações", black, 50, 350, 70)
            texto("Escolha a dificuldade: ", black, 30, 350, 200)
            texto("Fácil", black, 30, 600, 200)
            texto("Difícil", black, 30, 680, 200)
            texto("Voltar", black, 30, 25, 605)
            
            if cont == 0:
                pygame.draw.rect(fundo, red, [330, 205, 10, 10])
                if contx == 0:
                    pygame.draw.rect(fundo, white, [620, 225, 10, 10])
                    texto("Fácil", white, 30, 600, 200)
                    if foud == 0:
                        texto("Fácil", umacor, 30, 600, 200)
                        texto("Difícil", black, 30, 680, 200)
                    elif foud == 1:
                        texto("Fácil", black, 30, 600, 200)
                        texto("Difícil", umacor, 30, 680, 200)
                    
                if contx == 1:
                    pygame.draw.rect(fundo, white, [700, 225, 10, 10])
                    texto("Difícil", white, 30, 680, 200)
                    if foud == 0:
                        texto("Fácil", umacor, 30, 600, 200)
                        texto("Difícil", black, 30, 680, 200)
                    elif foud == 1:
                        texto("Fácil", black, 30, 600, 200)
                        texto("Difícil", umacor, 30, 680, 200)

                if contx == 2:
                    contx = 0
                if contx == -1:
                    contx = 1

            if cont == 1:
                pygame.draw.rect(fundo, red, [5, 610, 10, 10])

            if cont == 2:
                cont = 0 

            if cont == -1:
                cont = 1
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    menu = False
                    fimdejogo = False
                    instruçoes = False 
                    config = False
                if event.type == pygame.KEYDOWN:
                    if cont == 0:
                        if event.key == pygame.K_RIGHT:
                            contx += 1
                        if event.key == pygame.K_LEFT:
                            contx -= 1
                        if contx == 0 and event.key == pygame.K_RETURN:
                            dificuldade = 0
                            foud = 0
                        if contx == 1 and event.key == pygame.K_RETURN:
                            dificuldade = 1
                            foud = 1

                    if cont == 1 and event.key == pygame.K_RETURN:
                        if sansundertale == 0:
                            instruçoes = False
                            menu = True
                            sair = True
                            fimdejogo = False
                            config = False
                        if sansundertale == 1:
                            instruçoes = False
                            menu = False    
                            sair = True
                            fimdejogo = True
                            config = False
                    if event.key == pygame.K_DOWN:
                        cont += 1
                    if event.key == pygame.K_UP:
                        cont -= 1


            pygame.display.update()

#Game over
        while fimdejogo:
            fundo.fill(blue)
            texto('Game over', black, 50, 65, 30)
            texto("Tentar de novo", white, 30, 405, 255)
            texto("Configurações", white, 30, 405, 295)
            texto("Sair",white, 30, 405, 335)
            texto("Pontuação final: "+str(pontos), black, 30, 70, 80)
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
                            pos_x   = randrange(0, largura-tamanho, 20)
                            pos_y   = randrange(0, altura-tamanho-placar, 20)
                            maca_x  = randrange(0, largura-tamanho, 20)
                            maca_y  = randrange(0, altura-tamanho-placar, 20)
                            velocidade_x = 0
                            velocidade_y = 0
                            CobraXY     = []
                            CobraComp   = 1
                            pontos = 0
                        if cont == 1:
                            sair = True
                            fimdejogo = False
                            menu = False
                            instruçoes = False
                            config = True
                            sansundertale = 1
                        if cont == 2:
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

            if dificuldade == 1:
                clock.tick(35)  
            if dificuldade == 0:
                clock.tick(20)

jogo()