import pygame
from pygame.locals import *
from pygame.sprite import (
    Sprite,
    RenderPlain)
from main import generate_question

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

class TimeSprite(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        global time_used
        self.font = pygame.font.Font(None, 72)
        text = "{0}".format(time_used)
        self.image = self.font.render(text, 1, (10, 10, 10))
        self.rect = self.image.get_rect(centerx=background.get_width()/2)
        return

    def update(self):
        global time_used
        text = "{0}".format(time_used)
        self.image = self.font.render(text, 1, (10, 10, 10))
        self.rect = self.image.get_rect(centerx=background.get_width()/2)
        return

class QuestionSprite(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.question = generate_question()
        self.font = pygame.font.Font(None, 72)
        self.image = self.font.render(self.question, 1, (10, 10, 10))
        self.rect = self.image.get_rect(
            centerx=background.get_width()/2,
            centery=background.get_width()/2)
        return

    def change(self):
        self.question = generate_question()
        return

    def update(self):
        global answer
        text = self.question + answer
        self.image = self.font.render(text, 1, (10, 10, 10))
        self.rect = self.image.get_rect(
            centerx=background.get_width()/2,
            centery=background.get_width()/2)
        return

screen.blit(background, (0, 0))
pygame.display.flip()

time_used = 0
clock = pygame.time.Clock()

time_sprite = TimeSprite()
question_sprite = QuestionSprite()
all_sprites = RenderPlain((time_sprite, question_sprite))

answer = ""
def process_key(event):
    global answer
    if event.key == K_0:
        answer += "0"
    elif event.key == K_1:
        answer += "1"
    elif event.key == K_2:
        answer += "2"
    elif event.key == K_3:
        answer += "3"
    elif event.key == K_4:
        answer += "4"
    elif event.key == K_5:
        answer += "5"
    elif event.key == K_6:
        answer += "6"
    elif event.key == K_7:
        answer += "7"
    elif event.key == K_8:
        answer += "8"
    elif event.key == K_9:
        answer += "9"
    elif event.key == K_RETURN:
        question_sprite.change()
        answer = ""
    return

going = True
while going:
    clock.tick(60)
    time_used += clock.get_time()
    if time_used > 60000:
        screen.blit(background, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
        continue
    for event in pygame.event.get():
        if event.type == QUIT:
            going = False
        elif event.type == KEYDOWN:
            process_key(event)

    all_sprites.update()
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
