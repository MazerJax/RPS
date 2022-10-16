from re import S
import pygame, random, sys
import os

'''class RPS:
    def __init__(self, type, position, rock_image):
        self.position = position 
        self.type = type
        self.rock = rock_image
        #self.paper = paper_image
        #self.scissors = scissors_image
        self.rectangle = self.rock.get_rect()
        self.rectangle.center = position
    
    def draw(self, screen):
        if self.type == "rock":
            screen.blit(self.rock, self.rectangle)
        if self.type == "paper":
            screen.blit(self.rock, self.rectangle)
        if self.type == "scissors":
            screen.blit(self.rock, self.rectangle)

    def move(self):
        x_change = random.randint(-RPS.speed, RPS.speed)
        y_change = random.randint(-RPS.speed, RPS.speed)
        self.rectangle.move_ip(x_change, y_change)
        self.health -= 0.15'''

'''class Rock:
    speed = 5
    def __init__(self, rock_image, position):
        self.position = position 
        self.type = type
        self.image = rock_image
        self.rectangle = self.image.get_rect()
        self.rectangle.center = position
    
    def draw(self, screen):
            screen.blit(self.image, self.rectangle)

    def move(self):
        x_change = random.randint(-Rock.speed, Rock.speed)
        y_change = random.randint(-Rock.speed, Rock.speed)
        self.rectangle.move_ip(x_change, y_change)'''

'''class Paper:
    speed = 5
    def __init__(self, rock_image, position):
        self.position = position 
        self.type = type
        self.image = rock_image
        self.rectangle = self.image.get_rect()
        self.rectangle.center = position
    
    def draw(self, screen):
            screen.blit(self.image, self.rectangle)

    def move(self):
        x_change = random.randint(-Paper.speed, Paper.speed)
        y_change = random.randint(-Paper.speed, Paper.speed)
        self.rectangle.move_ip(x_change, y_change)'''

'''class Scissors:
    speed = 5
    def __init__(self, rock_image, position):
        self.position = position 
        self.type = type
        self.image = rock_image
        self.rectangle = self.image.get_rect()
        self.rectangle.center = position
    
    def draw(self, screen):
            screen.blit(self.image, self.rectangle)

    def move(self):
        x_change = random.randint(-Scissors.speed, Scissors.speed)
        y_change = random.randint(-Scissors.speed, Scissors.speed)
        self.rectangle.move_ip(x_change, y_change)'''


class play_obj:
    speed = 5
    def __init__(self, rock_image, position):
        self.position = position 
        self.type = type
        self.image = rock_image
        self.rectangle = self.image.get_rect()
        self.rectangle.center = position
    
    def draw(self, screen):
            screen.blit(self.image, self.rectangle)

    def move(self):
        x_change = random.randint(-play_obj.speed, play_obj.speed)
        y_change = random.randint(-play_obj.speed, play_obj.speed)
        self.rectangle.move_ip(x_change, y_change)




def main():
    
    #debugging to check images are in directory
    path = 'D:\Programming\Github\RPS'
    print(os.path.isfile(path))

    print(os.getcwd()) 
    
    #main program
    #
    #

    pygame.init()
    size = width, height = (600, 400)
    
    screen = pygame.display.set_mode(size)
    screen.fill((0,0,0))

    rock_image = pygame.image.load("rock.png")
    rock_image = pygame.transform.smoothscale(rock_image, (30,30))

    paper_image = pygame.image.load("paper.png")
    paper_image = pygame.transform.smoothscale(paper_image, (30,30))

    scissors_image = pygame.image.load("scissors.png")
    scissors_image = pygame.transform.smoothscale(scissors_image, (30,30))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        screen.fill((120,120,120))
        
        rpsObj = play_obj(rock_image, (300, 200))
        rpsObj.move()
        rpsObj.draw(screen)

        rpsObj2 = play_obj(paper_image, (200,200))
        rpsObj2.move()
        rpsObj2.draw(screen)

        rpsObj3 = play_obj(scissors_image, (400,200))
        rpsObj3.move()
        rpsObj3.draw(screen)
        

        pygame.display.update()

if __name__ == '__main__':
    main()