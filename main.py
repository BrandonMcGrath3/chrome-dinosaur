import pygame
import os
import random
pygame.init()

# Global Constants
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1300
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#variable keeps track of how many games have been played
global game_count 
game_count = 0
#variable keeps track of whether or not player 1 (green) is dead (True) or alive (False)
global p1_dead
p1_dead = False

#variable keeps track of whether or not player 2 (purple) is dead (True) or alive (False)
global p2_dead
p2_dead = False

START = [pygame.image.load(os.path.join("Assets/Dino", "DinoStartRun1.png"))]
RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

RUNNING1 = [pygame.image.load(os.path.join("Assets/Dino", "Dino2Run1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "Dino2Run2.png"))]
JUMPING1 = pygame.image.load(os.path.join("Assets/Dino", "Dino2Jump.png"))
DUCKING1 = [pygame.image.load(os.path.join("Assets/Dino", "Dino2Duck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "Dino2Duck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

#a limiter that sets the maximum FPS to 30
FPS_Clock = pygame.time.Clock()
FPS = 30
FPS_Clock.tick(FPS)

class Dinosaur:
    X_POS = 60
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_w] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_s] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_s]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

#player 2 class used for purple dino
class Dinosaur2:
    X_POS = 160
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING1
        self.run_img = RUNNING1
        self.jump_img = JUMPING1

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, high_score, high_score1, game_count, p1_dead, p2_dead
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    player2 = Dinosaur2()
    cloud = Cloud()
    game_speed = 18 
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    
    death_count = 0
    
    

    def score():
        global points, game_speed, high_score, high_score1
        points += 1
        if points % 100 == 0:
            game_speed += 2
        #displays high score after the first game played for both players in the top right during gameplay
        if(game_count >= 1):
            text1 = font.render("Green Dino High Score: " + str(high_score), True, (0, 255, 0))
            text1Rect = text1.get_rect()
            text1Rect.center = (1100, 40)
            SCREEN.blit(text1, text1Rect)
            text2 = font.render("Purple Dino High Score: " + str(high_score1), True, (160, 32, 240))
            text2Rect = text2.get_rect()
            text2Rect.center = (1100, 100)
            SCREEN.blit(text2, text2Rect)

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (900, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg, high_score, high_score1
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        #ONLY display player 1 (green dino) if the variable is set to False meaning the player hasn't died yet
        if(p1_dead == False):
            player.draw(SCREEN)
            player.update(userInput)
        #ONLY display player 2 (purple dino) if the variable is set to False meaning the player hasn't died yet
        if(p2_dead == False):
            player2.draw(SCREEN)
            player2.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            #sets collision for player 1 (green dino) only if they're alive and visible on the screen
            if p1_dead == False:
                if player.dino_rect.colliderect(obstacle.rect):
                    pygame.time.delay(2000)
                    death_count += 1
                    game_count += 1
                    #if more than one game has been played adjust the high score
                    if(game_count > 1):
                        if(high_score < points):
                            high_score = points
                    #if this is the first playthrough set the high score for both players to the points earned so far
                    else:
                        high_score = points
                        high_score1 = points
                    #if both players would be dead reset the game and spawn both players in by resetting the p1_dead & p2_dead variables to False (Alive)
                    if(p2_dead == True):
                        p2_dead = False
                        p1_dead = False
                    #if this is the first player to die then set them to dead
                    else:
                        p1_dead = True
                    menu(death_count)
                        
            #sets collision for player 2 (purple dino) only if they're alive and visible on the screen
            if p2_dead == False:
                if player2.dino_rect.colliderect(obstacle.rect):
                    pygame.time.delay(2000)
                    death_count += 1
                    game_count += 1
                    #if more than one game has been played adjust the high score
                    if(game_count > 1):
                        if(high_score1 < points):
                            high_score1 = points
                    #if this is the first playthrough set the high score for both players to the points earned so far
                    else:
                        high_score1 = points
                        high_score = points
                    #if both players would be dead reset the game and spawn both players in by resetting the p1_dead & p2_dead variables to False (Alive)
                    if(p1_dead == True):
                        p2_dead = False
                        p1_dead = False
                    #if this is the first player to die then set them to dead
                    else:
                        p2_dead = True
                    menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global high_score
    #global high_score1
    
    global points
    
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 20)
        
        if death_count == 0:
            text = font.render("Press any Key to Start: Green Dino uses W to jump or S to crouch + Purple Dino uses UP to jump and DOWN to crouch", True, (0, 255, 0))
        elif death_count > 0:
            
            #Display both players high score after one of the two character dies
            text1 = font.render("Green Dino High Score: " + str(high_score), True, (0, 255 , 0))
            text2 = font.render("Purple Dino High Score: " + str(high_score1), True, (160, 32 , 240))
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)

            highscoreRect = text1.get_rect()
            highscoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
            SCREEN.blit(text1, highscoreRect)
            highscoreRect1 = text2.get_rect()
            highscoreRect1.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)
            SCREEN.blit(text2, highscoreRect1)
            
            

        
        #The first screen the user experiences
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)

        

        SCREEN.blit(START[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)
