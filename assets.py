from ursina import *
from ursina import collider
class helicopter:
  def __init__(self,x,y,use=False) -> None: 
    self.body = Entity(position=(x,y),model="quad",scale=(2.5,1.5),texture='heli',collider='box')
    self.helice = Entity(position=(x,y+1.2),model="cube",scale=(3.5,0.1,0.1))
    self.ligahelice = Entity(position=(x,y+1),model="quad",scale=(0.2,0.5))
    self.use = use
  def update(self):
    self.helice.rotation_y += 30
  def move(self,x,y):
    self.body.position = (x,y)
    self.helice.position = (x,y+1.2)
    self.ligahelice.position = (x,y+1)

class player:
  def __init__(self,x,y) -> None:
    self.hitbox = Entity(position=(x,y,0),model='sphere',color=color.blue,scale =(1,1,1),collider='box')
    self.GRAVITY = 0.09
    self.GRAVITY_JUMP = 2*self.GRAVITY
    self.JUMP_CONTROL = 0
    self.veicleSituation = 0
    self.onBoard = 0

  def jump(self):
    self.JUMP_CONTROL = 40
  
  def update(self):
    self.hitbox.x -= held_keys['a'] * 4*time.dt
    self.hitbox.x += held_keys['d'] * 4*time.dt
    self.colision = self.hitbox.intersects()
    if self.JUMP_CONTROL > 0:
      self.hitbox.y += self.GRAVITY_JUMP
      self.JUMP_CONTROL -= 1
