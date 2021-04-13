import pygame
import math
#Setup Display
pygame.init()
WIDTH,HEIGHT=800,500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game")

#colors
WHITE= (255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)

#Button Variables
RADIUS =20
GAP_SIZE=15
letters =[]
startX=round((WIDTH-(RADIUS * 2 + GAP_SIZE)*13)/2) #Value =42

# startX= round((WIDTH-((RADIUS*2*13)+(GAP_SIZE*12)))/2) # value = 50
startY=400

A=65
for i in range(26):
    x= startX + GAP_SIZE *2+ ((RADIUS*2 + GAP_SIZE)*(i%13))
    y=startY + ((i//13)* (GAP_SIZE+RADIUS*2))
    letters.append([x,y,chr(A+i),True])

#Fonts
LETTER_FONT= pygame.font.SysFont("comicsans",40)

#Loading Images
images=[]
for i in range(7):
    image=pygame.image.load(f'hangman{i}.png')
    images.append(image)

#Game Variables
hangman_status =0


#SETUP game Loop
FPS = 60
clock=pygame.time.Clock()
running= True

def draw():
    screen.fill(WHITE)
    #draw Buttons
    for letter in letters:
        x,y,ltr,visible = letter
        if visible:

            pygame.draw.circle(screen,BLACK,(x,y),RADIUS,3)
            text=LETTER_FONT.render(ltr,True, BLACK)
            # screen.blit(text,(x-10,y-14)) # this one works too
            screen.blit(text,(x-int(text.get_width()/2),y-int(text.get_height()/2)))





    screen.blit(images[hangman_status],(150,100))
    pygame.display.update()

while running:
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False

        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y= pygame.mouse.get_pos()
            # print(m_x,m_y)
            # print(RADIUS)

            for letter in letters:
                x,y,ltr,visible= letter
                if visible:
                    distance= math.sqrt((x-m_x)**2 + (y-m_y)**2) #Distance formula
                    if distance < RADIUS:
                        letter[3]=False




pygame.quit()
