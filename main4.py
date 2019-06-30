import pygame
from pygame.locals import *
from pygame.sprite import (
    Sprite,
    RenderPlain)
from main import generate_question

pygame.init()
screen = pygame.display.set_mode((1200, 480))
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

state = "Initial"

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
        self.question_list = []
        (self.question, self.answer) = generate_question()
        self.font = pygame.font.Font(None, 72)
        self.image = self.font.render(self.question, 1, (10, 10, 10))
        self.rect = self.image.get_rect(
            centerx=background.get_width()/2,
            centery=background.get_height()/2)
        return

    def reset(self):
        self.question_list = []
        return

    def save_question(self, answer):
        self.question_list.append((self.question, self.answer, answer))
        return

    def change(self):
        (self.question, self.answer) = generate_question()
        return

    def update(self):
        global answer
        text = self.question + answer
        self.image = self.font.render(text, 1, (10, 10, 10))
        self.rect = self.image.get_rect(
            centerx=background.get_width()/2,
            centery=background.get_height()/2)
        return

screen.blit(background, (0, 0))
pygame.display.flip()

time_used = 0
clock = pygame.time.Clock()

time_sprite = TimeSprite()
question_sprite = QuestionSprite()
all_sprites = RenderPlain((time_sprite, question_sprite))

right_img = pygame.image.load("right.png")
wrong_img = pygame.image.load("wrong.png")
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
        question_sprite.save_question(answer)
        question_sprite.change()
        answer = ""
    return

going = True
while going:
    clock.tick(60)
    time_used += clock.get_time()
    if state == "Initial":
        screen.blit(background, (0, 0))
        font = pygame.font.Font(None, 72)
        text = "{0}".format("Ready?")
        image = font.render(text, 1, (10, 10, 10))
        screen.blit(
            image,
            (background.get_width()/2, background.get_height()/2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif (event.type == KEYDOWN and event.key == K_RETURN):
                state = "Running"
    elif state == "Running":
        if time_used > 10000:
            state = "Complete"
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
    elif state == "Complete":
        screen.blit(background, (0, 0))
        font = pygame.font.Font(None, 72)
        font2 = pygame.font.Font(None, 32)
        question_lists = question_sprite.question_list
        x = 0
        y = 0
        total = 0
        correct = 0
        for question in question_lists:
            question_img = font2.render(question[0] + question[2], 1, (10, 10, 10))
            screen.blit(
                question_img,
                (x, y)
            )
            total += 1
            try:
                if question[1] == int(question[2]):
                    correct += 1
                    width = question_img.get_width()
                    new_x = x + width + 20
                    screen.blit(right_img, (new_x, y))
                else:
                    width = question_img.get_width()
                    new_x = x + width + 20
                    screen.blit(wrong_img, (new_x, y))
            except:
                width = question_img.get_width()
                new_x = x + width + 20
                screen.blit(wrong_img, (new_x, y))

            y += 32
            if y > 200:
                y = 0
                x += 200
        score_text = "Score: {0}/{1}".format(correct, total)
        score_text_image = font2.render(
            score_text,
            1,
            (10, 10, 10))
        screen.blit(
            score_text_image,
            (x, y)
        )
        text = "{0}".format("Completed!")
        image = font.render(text, 1, (10, 10, 10))
        screen.blit(
            image,
            (background.get_width()/2, background.get_height()/2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False

pygame.quit()
