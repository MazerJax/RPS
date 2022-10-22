from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from re import S
import pygame, random, sys

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
    speed = 1
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
    
    #debugging
    path = 'D:\Programming\Github\RPS\RPS.py'
    print(os.path.isfile(path))

    print(os.getcwd()) 
    
    #main program
    #
    #

    pygame.init()
    size = width, height = (600, 400)
    
    screen = pygame.display.set_mode(size)   #flags=pygame.FULLSCREEN
    pygame.display.set_caption('Rock, Paper and Scissors Battle')
    icon = pygame.image.load("scissors.png")
    icon = pygame.transform.smoothscale(icon, (50,50))
    pygame.display.set_icon(icon)
    screen.fill((120,20,90))

    rock_image = pygame.image.load("rock.png")
    rock_image = pygame.transform.smoothscale(rock_image, (30,30))

    paper_image = pygame.image.load("paper.png")
    paper_image = pygame.transform.smoothscale(paper_image, (30,30))

    scissor_image = pygame.image.load("scissors.png")
    scissor_image = pygame.transform.smoothscale(scissor_image, (30,30))


    print(random.randint(0,width))

    rocklist = []
    for count in range(20):
        rock_obj = play_obj(rock_image, ((random.randint(0,width)), random.randint(0,height)))
        rocklist.append(rock_obj)
       
    paperlist = []
    for count in range(20):
        paper_obj = play_obj(paper_image, (random.randint(0,width), random.randint(0,height)))
        paperlist.append(paper_obj)

    scissorlist = []
    for count in range(20):
        scissor_obj = play_obj(scissor_image, (random.randint(0,width), random.randint(0,height)))
        scissorlist.append(scissor_obj)

    print(rocklist)
 
 
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        for rock in rocklist:
            for scissor in scissorlist:
                if rock.rectangle.collidepoint(scissor.rectangle.center):
                    replace_obj = play_obj(rock_image, (scissor.rectangle.center))
                    rocklist.append(replace_obj)
                    scissorlist.remove(scissor)

        for paper in paperlist:
            for rock in rocklist:
                if paper.rectangle.collidepoint(rock.rectangle.center):
                    replace_obj = play_obj(paper_image, (rock.rectangle.center))
                    paperlist.append(replace_obj)
                    rocklist.remove(rock)

        for scissor in scissorlist:
            for paper in paperlist:
                if scissor.rectangle.collidepoint(paper.rectangle.center):
                    replace_obj = play_obj(scissor_image, (paper.rectangle.center))
                    scissorlist.append(replace_obj)
                    paperlist.remove(paper) 

       
       
        screen.fill((204,255,255))
        
        for rock in rocklist:
            rock.move()
            rock.draw(screen)
        
        for paper in paperlist:
            paper.move()
            paper.draw(screen)
        
        for scissor in scissorlist:
            scissor.move()
            scissor.draw(screen)
        
        pygame.display.update()

if __name__ == '__main__':
    main()