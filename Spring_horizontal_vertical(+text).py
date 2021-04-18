import pygame
pygame.init()
screen = pygame.display.set_mode([1000,800])
screen.fill([68,242,244])

img = pygame.image.load("tt.png")
img1= pygame.image.load("text(Ru).png")
img2= pygame.image.load("texts2.png")


#img1=pygame.transform.scale(img1,(550,125))

img0=[]
img_rot,img_flip,img_flip1=[],[],[]
for i in range(400):
    if i<200:
        img0.append(pygame.transform.scale(img,(50,200+i)))
    if i>199:
        img0.append(pygame.transform.scale(img,(50,600-i)))
    img_rot.append(pygame.transform.rotate(img0[i],90))
    img_flip.append(pygame.transform.flip(img_rot[i],True,False))
    img_flip1.append(0)
for n in range(199):
    img_flip1[n]=img_flip[n+200]
for n in range(199,399):
    img_flip1[n]=img_flip[n-200]
timer = pygame.time.Clock()
n,n1=-1,0

running=True
while running:
    n=n+1
    n=n%399
    if n<200:
        n1=n
    if n>199:
        n1=400-n
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill([68,242,244])
    screen.blit(img1,(400,400))
    screen.blit(img2,(550,80))
    #----------------------------------------------------------------
    #Vertical spring
    pygame.draw.line(screen,'black',(250,153),(450,153),10)
    pygame.draw.rect(screen,'black',[290,341+n1,47.6,47.6])
    screen.blit(img0[n],(300,150))
#----------------------------------------------------------------
    #Horizontal spring
    pygame.draw.line(screen,'black',(505,200),(505,385),10)
    pygame.draw.line(screen,'black',(505,380),(950,380),10)
    pygame.draw.rect(screen,'black',[688+n1*0.95,329,47.6,47.6])
    screen.blit(img_rot[n],(500,315))
#----------------------------------------------------------------
    #Horizontal spring  2
    pygame.draw.line(screen,'black',(205,570),(205,755),10)
    pygame.draw.line(screen,'black',(205,750),(830,750),10)
    pygame.draw.rect(screen,'black',[388+n1*0.95,690,60,60])
    screen.blit(img_rot[n],(200,680))
#----------------------------------------------------------------
    #Horizontal spring  3
    pygame.draw.line(screen,'black',(825,570),(825,755),10)
    screen.blit(img_flip1[n1],(430+n1,680))
    
    font=pygame.font.Font(None,40)
    #text=font.render('HARMONIC SPRING OSCILLATIONS',1,'navy')
    text=font.render('ГАРМОНИЧЕСКИЕ КОЛЕБАНИЯ ПРУЖИННОГО МАЯТНИКА',1,'navy')
    X,Y=75,50
    screen.blit(text,(X,Y))
    
    text1=font.render('M',1,'navy')
    X1,Y1=250,360+n1
    screen.blit(text1,(X1,Y1))
    
    text2=font.render('M',1,'navy')
    X2,Y2=690+n1,280
    screen.blit(text2,(X2,Y2))
    
    text3=font.render('2M',1,'navy')
    X3,Y3=380,650
    screen.blit(text3,(X3+n1,Y3))
    
    pygame.display.update()
    timer.tick(200)
pygame.quit()

    
    