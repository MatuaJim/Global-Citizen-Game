"""Underwater Cleanup — Pygame reference implementation.
An eel collects five pieces of rubbish while avoiding marine life.
Arrow keys/WASD move. Collect all items before the 45-second timer ends.
"""
import random
import pygame

WIDTH, HEIGHT = 900, 600
SEA = (10, 92, 112); SAND = (126, 93, 55); CREAM = (244, 237, 218)
GOLD = (217, 162, 60); CORAL = (185, 73, 63); WHITE = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Underwater Cleanup")
clock = pygame.time.Clock(); font = pygame.font.SysFont("arial", 28, bold=True)

class Actor:
    def __init__(self, x, y, colour, radius): self.pos=pygame.Vector2(x,y); self.colour=colour; self.radius=radius
    def draw(self): pygame.draw.circle(screen,self.colour,self.pos,self.radius)
    def hit(self, other): return self.pos.distance_to(other.pos) < self.radius+other.radius

def new_game():
    eel=Actor(90,HEIGHT//2,GOLD,22)
    rubbish=[Actor(random.randint(160,840),random.randint(100,500),WHITE,13) for _ in range(5)]
    hazards=[Actor(random.randint(180,820),random.randint(110,490),CORAL,25) for _ in range(4)]
    return eel,rubbish,hazards,0,3,pygame.time.get_ticks()

eel,rubbish,hazards,score,lives,start=new_game(); running=True
while running:
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT: running=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_r: eel,rubbish,hazards,score,lives,start=new_game()
    keys=pygame.key.get_pressed(); direction=pygame.Vector2(keys[pygame.K_RIGHT] or keys[pygame.K_d]-(keys[pygame.K_LEFT] or keys[pygame.K_a]), keys[pygame.K_DOWN] or keys[pygame.K_s]-(keys[pygame.K_UP] or keys[pygame.K_w]))
    if direction.length_squared(): eel.pos += direction.normalize()*260*dt
    eel.pos.x=max(25,min(WIDTH-25,eel.pos.x)); eel.pos.y=max(80,min(HEIGHT-25,eel.pos.y))
    seconds=max(0,45-(pygame.time.get_ticks()-start)//1000)
    for item in rubbish[:]:
        if eel.hit(item): rubbish.remove(item); score+=100
    for hazard in hazards:
        if eel.hit(hazard): lives-=1; score=max(0,score-25); eel.pos=pygame.Vector2(90,HEIGHT//2)
    screen.fill(SEA); pygame.draw.rect(screen,SAND,(0,HEIGHT-70,WIDTH,70))
    for x in range(40,WIDTH,120): pygame.draw.line(screen,(48,135,91),(x,HEIGHT-70),(x+25,HEIGHT-145),7)
    for item in rubbish: item.draw(); pygame.draw.line(screen,(30,70,75),item.pos+(-8,-8),item.pos+(8,8),3)
    for hazard in hazards: hazard.draw()
    eel.draw(); pygame.draw.circle(screen,(30,55,60),eel.pos+(8,-4),3)
    screen.blit(font.render(f"Score {score}   Time {seconds}s   Lives {lives}",True,CREAM),(24,22))
    if not rubbish or lives<=0 or seconds==0:
        result="Waterway restored!" if not rubbish else "Press R to try again"
        screen.blit(font.render(result,True,CREAM),(WIDTH//2-130,HEIGHT//2))
    pygame.display.flip()
pygame.quit()
