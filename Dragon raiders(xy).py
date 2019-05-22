#Dragon Raiders
from gamelib import*
game=Game(800,600,"Dragon Raiders")
logo=Image("dr1.png",game)
bk=Animation("Dragon.png",20,game,10240/20,256,3)
bk.resizeTo(800,600)
story = Image("cooltext4.png",game)
howtoplay = Image("cooltext5.png",game)
play = Image("play.png",game)
cave=Image("cave2.png",game) 
game.setBackground(cave)
lose=Sound("lose.wav",2)
logo.y=225
logo.resizeBy(-35)
howtoplay.y=225
howtoplay.resizeBy(-10)
story.y=325
story.resizeBy(-10)
play.y=350
play.resizeBy(-25)
Dragon=Animation("dragon2s.png",4,game,960/4,240,3)
cave.resizeBy(-15)
Dragon.resizeBy(-30)
fire=Animation("fireball.png",4,game,2400/4,300,3)
fire.resizeBy(-30)
impact=Animation("impact4.png",19,game,12800/19,640)
impact.resizeBy(-25)
dragonm=Animation("dragonlich.png",9,game,3096/9,616,3)
dragonm.setSpeed(11,90)
dragonm.resizeBy(-50)
dragonm2=Animation("dragonlich.png",9,game,3096/9,616,3)
dragonm2.setSpeed(11,90)
dragonm2.resizeBy(-50)
dragonm3=Animation("dragonlich.png",9,game,3096/9,616,3)
dragonm3.setSpeed(11,90)
dragonm3.resizeBy(-50)
over=Image("over.jpg",game)
level=Image("leve.png",game)
level.resizeTo(800,600)
over.resizeTo(800,600)

#minion=Animation("minion2.png",4,game,2800/4,400,3)
#minion.resizeBy(-65)
#minion.setSpeed(8,90)
#minion.visible=True
fire.setSpeed(10,270)
#minion.visible=True


    

#mage=Animation("chara_nich_anime.png",44,game,2000/44,2331) isn't working

#Title screen
while not game.over:
    game.processInput()
    bk.draw()
    logo.draw()
    #story.draw()
    #howtoplay.draw()
    play.draw()
    if play.collidedWith(mouse)and mouse.x>play.left and mouse.x<play.right and mouse.y>play.top and mouse.y<play.bottom and mouse.LeftClick:
        game.over = True                                           
    game.update(30)
game.over=False

rocks=[]
for index in range(50):
    rocks.append(Animation("Rock.png",32,game,8192/32,256,5))
for index in range(50):
    x=randint(100,700)
    y=-randint(100,10000)
    rocks[index].moveTo(x,y)
    s=randint(2,8)
    rocks[index].setSpeed(s,180)
    rocks[index].resizeBy(-70)
   


#"minion2.png",4,game,2800/4,400,3 

minion=[]
for index in range(25):
    minion.append(Animation("minion2.png",4,game,2800/4,400,3))
for index in range(25):
    x=randint(100,10000)
    y=randint(100,500)
    minion[index].moveTo(x,y)
    s=randint(8,10)
    minion[index].setSpeed(s,90)
    minion[index].resizeBy(-65)
    minion[index].visible=False




#Level 1
while not game.over:
    game.processInput()
    game.scrollBackground("left",4)
    cave.visible=True
    Dragon.draw()
    fire.move()
    dragonm.move()
    dragonm2.move()
    dragonm3.move()
    over.visible=False
    
    if keys.Pressed[K_LEFT]:
        Dragon.x-=10
    if keys.Pressed[K_RIGHT]:
        Dragon.x+=10
        
    if keys.Pressed[K_UP]:
        Dragon.y-=10
    if keys.Pressed[K_DOWN]:
        Dragon.y+=10

    if keys.Pressed[K_SPACE] and fire.visible==False:
        fire.visible = True
        fire.x = Dragon.x
        fire.y = Dragon.y
        fire.move()
       
        
    if fire.x >= 900:
        fire.visible = False

   

    

   


    for index in range(len(rocks)):
        rocks[index].move()
        if game.score>50:
            rocks[index].visible=False
        if rocks[index].collidedWith(Dragon):
            Dragon.health-=5
            rocks[index].visible=False
            
    for index in range(len(rocks)):
        if rocks[index].collidedWith(fire)and rocks[index].visible==True and fire.visible==True:
            fire.visible=False
            rocks[index].visible=False
            game.score+=5
           



    for index in range(len(minion)):
        minion[index].move()
        minion[index].visible=False
        if game.score>50:
            minion[index].visible=True
        if minion[index].collidedWith(Dragon)and game.score>50:
            Dragon.health-=5
            minion[index].visible=False
            minion[index].moveTo(-1000,-1000)
        if minion[index].collidedWith(fire)and game.score>50 and minion[index].visible==True and fire.visible==True:
            fire.visible=False
            game.score+=5
            minion[index].visible=False
            minion[index].moveTo(-1000,-1000)
        if game.score>195:
            minion[index].visible=False
        if game.score>199 and minion[index].collidedWith(Dragon) and minion[index].collidedWith(fire):
            game.score+=0
            Dragon.health+=0

        
    dragonm.visible=False    
    dragonm2.visible=False
    dragonm3.visible=False

    if minion[index].isOffScreen("left"):
        x=randint(100,10000)
        y=randint(100,500)
        minion[index].moveTo(x,y)
        minion[index].visible=True

    if dragonm.isOffScreen("left"):
        y=randint(50,100)
        dragonm.moveTo(800,50)
        dragonm.move()
   
    if dragonm2.isOffScreen("left"):
        y=randint(250,300)
        dragonm2.moveTo(900,y)
        dragonm2.move()

    if dragonm3.isOffScreen("left"):
        y=randint(550,600)
        dragonm3.moveTo(1000,550)
        dragonm3.move()

    if game.score>75:
        dragonm.visible=True    
        dragonm2.visible=True
        dragonm3.visible=True

    if dragonm.collidedWith(Dragon)and dragonm.visible==True:
            Dragon.health-=5
            dragonm.visible=False
            dragonm.moveTo(-1000,-1000)
    if dragonm2.collidedWith(Dragon)and dragonm2.visible==True:
            Dragon.health-=5
            dragonm2.visible=False
            dragonm2.moveTo(-1000,-1000)
    if dragonm3.collidedWith(Dragon)and dragonm3.visible==True:
            Dragon.health-=5
            dragonm3.visible=False
            dragonm3.moveTo(-1000,-1000)
    if dragonm.collidedWith(fire)and dragonm.visible==True and fire.visible==True :
        fire.visible=False
        game.score+=5
        dragonm.visible=False
        dragonm.moveTo(-1000,-1000)
    if dragonm2.collidedWith(fire)and dragonm2.visible==True and fire.visible==True:
        fire.visible=False
        game.score+=5
        dragonm2.visible=False
        dragonm2.moveTo(-1000,-1000)
    if dragonm3.collidedWith(fire)and dragonm3.visible==True and fire.visible==True:
        fire.visible=False
        game.score+=5
        dragonm3.visible=False
        dragonm3.moveTo(-1000,-1000)

    if game.score>95:
        dragonm.visible=False    
        dragonm2.visible=False
        dragonm3.visible=False

    if game.score>120:
        dragonm.visible=True    
        dragonm2.visible=True
        dragonm3.visible=True

    if game.score>145:
        dragonm.visible=False    
        dragonm2.visible=False
        dragonm3.visible=False
    if game.score>170:
        dragonm.visible=True    
        dragonm2.visible=True
        dragonm3.visible=True
    if game.score>195:
        dragonm.visible=False     
        dragonm2.visible=False
        dragonm3.visible=False
    if game.score>200:
        dragonm.visible=False    
        dragonm2.visible=False
        dragonm3.visible=False
        boss.move()
     
    if dragonm.visible==False:
        dragonm.moveTo(-1000,-1000)
    if dragonm.visible==False:
        dragonm.moveTo(-1000,-1000)
    if dragonm.visible==False:
        dragonm.moveTo(-1000,-1000)

    if Dragon.health<=0:
        over.visible=True
        over.draw()
        game.over=True
        lose.play()

    if game.score==100 and keys.Pressed[K_SPACE]:
        Dragon.health+=3

    if game.score==125 and keys.Pressed[K_SPACE]:
        Dragon.health+=3

    if game.score==150 and keys.Pressed[K_SPACE]:
        Dragon.health+=3
    if game.score==200 and keys.Pressed[K_SPACE]:
        Dragon.health+=3

    

    if game.score>199 and dragonm.collidedWith(Dragon):
        Dragon.health+=0
    if game.score>199 and dragonm2.collidedWith(Dragon):
        Dragon.health+=0    
    if game.score>199 and dragonm3.collidedWith(Dragon):
        Dragon.health+=0

    if game.score>=200:
        level.visible=True
        level.draw()
        game.over=True
        
        

    game.drawText(" Health:"+str(Dragon.health),Dragon.x-25,Dragon.y+40)
    game.drawText
    
    game.displayScore()

  
  
        
    game.update(30)
