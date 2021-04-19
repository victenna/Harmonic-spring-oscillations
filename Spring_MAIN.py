import pygame,math,sys
pygame.init()
timer = pygame.time.Clock()
screen = pygame.display.set_mode([1000,800])
screen.fill([68,242,244])
keep_going = True
img = pygame.image.load("tt.png")
img1=pygame.transform.rotate(img,90)
imag,imag1,imag2=[0]*400,[0]*400,[0]*400
    
for i in range(400):
    i1=i%400
    i1=int(i1)
    i2=150*math.sin(6.28*(i1/200))
    i2=int(i2)
    imag[i1]=pygame.transform.scale(img,(50,200+i2))
    imag1[i1]=pygame.transform.scale(img1,(200+i2,50))
    imag2[i1]=pygame.transform.scale(img1,(200-i2,50))

img_text1= pygame.image.load("text(Ru).png")
img_text2= pygame.image.load("texts2.png")

i=0
while True:
    i=i+1
    i1=i%400
    i2=150*math.sin(6.28*(i1/200))
    i2=int(i2)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill([68,242,244])
    screen.blit(img_text1,(400,400))
    screen.blit(img_text2,(550,80))
#--------------------------------------------
     #Vertical spring
    pygame.draw.line(screen,'black',(240,102),(440,102),10)
    pygame.draw.rect(screen,'black',[290,290+i2,47.6,47.6])
    screen.blit(imag[i1],(300,100))
#----------------------------------------------------------------
    #Horizontal spring
    pygame.draw.line(screen,'black',(505,200),(505,385),10)
    pygame.draw.line(screen,'black',(505,380),(950,380),10)
    pygame.draw.rect(screen,'black',[688+i2*0.95,329,47.6,47.6])
    screen.blit(imag1[i1],(500,315))
    
#----------------------------------------------------------------
    #Horizontal spring  2
    pygame.draw.line(screen,'black',(205,570),(205,755),10)
    pygame.draw.line(screen,'black',(205,750),(630,750),10)
    pygame.draw.rect(screen,'black',[388+i2*0.95,690,60,60])
    screen.blit(imag1[i1],(200,690))
#----------------------------------------------------------------
    #Horizontal spring  3
    pygame.draw.line(screen,'black',(625,570),(625,755),10)
    screen.blit(imag2[i1],(430+i2*0.95,690,60,60))
    
#--------------------------------------------
    font=pygame.font.Font(None,40)
    #text=font.render('HARMONIC SPRING OSCILLATIONS',1,'navy')
    text=font.render('ГАРМОНИЧЕСКИЕ КОЛЕБАНИЯ ПРУЖИННОГО МАЯТНИКА',1,'navy')
    X,Y=75,50
    screen.blit(text,(X,Y))
    
    text1=font.render('M',1,'navy')
    X1,Y1=250,310+i2
    screen.blit(text1,(X1,Y1))
    
    text2=font.render('M',1,'navy')
    X2,Y2=700+i2,280
    screen.blit(text2,(X2,Y2))
    
    text3=font.render('2M',1,'navy')
    X3,Y3=390,650
    screen.blit(text3,(X3+i2,Y3))

    pygame.display.update()
    timer.tick(50)
