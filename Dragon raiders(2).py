#Dragon Raiders
from gamelib import*
game=Game(800,600,"Dragon Raiders")
bk=Image("Dragon_cave.gif",game)
lvl1bk=Image("Dungeon.png",game)
cave=Image("cave2.png",game) 
game.setBackground(cave)
mage=Animation("chara_nich_anime.png",45,game,2000/45,2331/4,3)
Dragon=Animation("dragon2s.png",4,game,960/4,240,3)
lvl1bk.resizeBy(-30)
cave.resizeBy(-15)
Dragon.resizeBy(-30)
fball=Animation("fireball.png",4,game,2400/4,300,3)
fball.resizeBy(-30)
#fball.visible=False
 
#2000/45,2331/45

#Title screen  
rock=[]
for index in range(100):
    rock.append(Animation("rock.png",32,game,8192/32,256)

while not game.over:
    game.processInput()
    game.scrollBackground("left",5)
    cave.draw()
    Dragon.draw()
    #for index in range(100):
        #rocks[index].move()
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
#game.over=False

#Level 1
while not game.over:
    game.processInput()
   # game.scrollBackground("left",2)
   # mage.draw()
    





    game.update(30)
game.over=False

#Level 2
while not game.over:
    game.processInput()
    





    game.update(30)
game.over=False

