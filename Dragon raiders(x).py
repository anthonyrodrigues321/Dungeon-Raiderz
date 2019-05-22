#Dragon Raiders
from gamelib import*
game=Game(800,600,"Dragon Raiders")
logo = Image("cooltext6.png",game)
bk=Image("background.jpg",game)
story = Image("cooltext4.png",game)
howtoplay = Image("cooltext5.png",game)
play = Image("cooltext3.png",game)
cave=Image("cave2.png",game) 
game.setBackground(cave)
logo.y=290
logo.resizeBy(-10)
howtoplay.y=225
howtoplay.resizeBy(-10)
story.y=325
story.resizeBy(-10)
play.y=375
play.resizeBy(-10)
Dragon=Animation("dragon2s.png",4,game,960/4,240,3)
cave.resizeBy(-15)
Dragon.resizeBy(-30)
fire=Animation("fireball.png",4,game,2400/4,300,3)
fire.resizeBy(-30)
minion=Animation("minion2.png",4,game,2800/4,400,3)
minion.resizeBy(-65)
minion.setSpeed(8,90)
minion.visible=True
fire.setSpeed(10,270)
minion.visible=True


    

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

#minion=[]
#for index in range(50):
 #   rocks.append(Animation("minion2.png",4,game,2800/4,400,3))
#for index in range(50):
  #  x=randint(100,700)
   # y=randint(100,10000)
    #minion[index].moveTo(x,y)
    #s=randint(5,10)
    #minion[index].setSpeed(s,180)
    

#Level 1
while not game.over:
    game.processInput()
    game.scrollBackground("left",4)
    cave.visible=True
    Dragon.draw()
    fire.move()
    
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
        #fire.setSpeed(180,Dragon.getAngle())
        #fire.x+=500
        
    if fire.x >= 800:
        fire.visible = False

    #for index in range(50):
        #minion[index].move()

    for index in range(len(rocks)):
        rocks[index].move()
        if rocks[index].collidedWith(Dragon):
            Dragon.health-=5
            rocks[index].visible=False
            #impact.moveTo(Dragon.x,Dragon.y-30)
           # impact.visible=True
    for index in range(len(rocks)):
        if rocks[index].collidedWith(fire):
            rocks[index].visible=False
            game.score+=5

    
        
    minion.move()

   # if rocks[index].collidedWith(Dragon):#and rocks[index]>Dragon.left and rocks[index]<Dragon.right and rocks[index]>Dragon.top and rocks[index]<Dragon.bottom)
        #Dragon.health-=5

    #if minion.collidedWith(fire) and minion.visible==True:
        #game.score+=10
        #minion.visible=False

   #if minion.collidedWith(Dragon)and minion.visible==True:
        #minion.move()
        #Dragon.health-=10
        #minion.visible=False

    for index in range(len(rocks)):
     if minion.collidedWith(fire):
            minion.visible=False
            game.score+=5

    if minion.isOffScreen("left")and minion.visible==False:
        minion.x=game.width+50
        minion.y=randint(100,500)
        minion.visible=True

        

    game.drawText(" Health:"+str(Dragon.health),Dragon.x-25,Dragon.y+40)
    #game.drawText("Magic Power: " + str(Dragon.ammo),Dragon.x-25,Dragon.y+20)

    #if fball.collidedWith(rocks[index]) and mouse.LeftClick:
        #minion.visible=False

    game.displayScore()

  
  
        
    game.update(30)
game.over=False

#Level 2
while not game.over:
    game.processInput()
    





    game.update(30)
game.over=False

