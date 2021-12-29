from ursina import *
from ursina import collider
import ursina
from ursina import text
from ursina.application import pause
app = Ursina()
import assets
EditorCamera()

p1  = assets.player(0,0)
heli = assets.helicopter(15,1.8)

surface = Entity(position=(0,-3,0),texture='grass',model='cube',color=color.yellow,scale=(10,1,3), collider='box')
block1 = Entity(position=(3,-1,0),model='cube',color=color.yellow,scale=(3,0.5,3), collider='box',texture='brick')
block2 = Entity(position=(11,-1,0),model='cube',color=color.yellow,scale=(3,0.5,2), collider='box',texture='brick')
endGameText = Text(text='Se Fudeu!!!',origin=(0,-2),visible= False,scale=(3,3),color=color.red)
endGameText2 = Text(text='Aperte enter para recomeçar',origin=(0,0),visible= False,scale=(1,1))
heli1 = assets.helicopter(13,4)



def update():
    p1.update()
    heli.update()
    if p1.colision.hit == False:
        p1.hitbox.y -= p1.GRAVITY
        p1.hitbox.color = color.blue
    else:
        p1.hitbox.color = color.red
    if p1.hitbox.y < -4:
        global endGameText,endGameText2
        endGameText2.visible = True
        endGameText.visible = True
        if held_keys['enter'] == 1:
            p1.hitbox.x = 0
            p1.hitbox.y = 0
            endGameText.visible = False
            endGameText2.visible = False
        camera.x = 0
        camera.y = 0
    else:
        camera.x = p1.hitbox.x
        camera.y = p1.hitbox.y
    
    if p1.veicleSituation == 1:
        heli.move(p1.hitbox.x,p1.hitbox.y)
        p1.hitbox.visible = False
        p1.hitbox.y -= p1.GRAVITY
        p1.veicleSituation = 1
        if held_keys['space'] == 1:
            p1.hitbox.y += p1.GRAVITY_JUMP

def input(k):
    p1.update()
    if p1.veicleSituation == 0:
        if k == 'space':
            if p1.colision.hit == True:
                p1.jump()
        elif k == 'enter':
            try:
                if repr(p1.colision.entities[0].texture) == 'heli.jpg':
                    p1.veicleSituation = 1
            except:
                False
    elif p1.veicleSituation == 1:
        if k == 'enter':
            p1.veicleSituation = 0
            p1.hitbox.visible = True


def rerun():
    global p1
    p1.hitbox.x = 0
    p1.hitbox.y = 0
app.run()