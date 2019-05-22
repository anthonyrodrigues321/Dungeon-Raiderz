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
logo.y=100
logo.resizeBy(-10)
howtoplay.y=225
howtoplay.resizeBy(-10)
story.y=325
story.resizeBy(-10)
play.y=435
play.resizeBy(-10)
Dragon=Animation("dragon2s.png",4,game,960/4,240,3)
cave.resizeBy(-15)
Dragon.resizeBy(-30)
fball=Animation("fireball.png",4,game,2400/4,300,3)
fball.resizeBy(-30)

#mage=Animation("chara_nich_anime.png",44,game,2000/44,2331) isn't working

#Title screen
while not game.over:
    game.processInput()
    bk.draw()
    logo.draw()
    story.draw()
    howtoplay.draw()
    play.draw()
    
    if play.collidedWith(mouse)and mouse.x>play.left and mouse.x<play.right and mouse.y>play.top and mouse.y<play.bottom and mouse.LeftClick:
        game.over = True
    game.update(30)
game.over=False

#Level 1
while not game.over:
    game.processInput()
    game.scrollBackground("left",4)
    cave.visible=True
    Dragon.draw()
    if keys.Pressed[K_LEFT]:
        Dragon.x-=10
    if keys.Pressed[K_RIGHT]:
        Dragon.x+=10
        
    if keys.Pressed[K_UP]:
        Dragon.y-=10
    if keys.Pressed[K_DOWN]:
        Dragon.y+=10

    if keys.Pressed[K_SPACE]:
        fball.moveTo(Dragon.x+150,Dragon.y)
        fball.draw()
        fball.setSpeed(90,Dragon.getAngle())
    
    
    





    game.update(30)
game.over=False

#Level 2
while not game.over:
    game.processInput()
    





    game.update(30)
game.over=False

