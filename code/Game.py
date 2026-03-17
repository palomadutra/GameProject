import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 600))

    def run (self, ):
        print('Setup Start')

        print('Setup End')

        print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



                # Check for all events
                # todos os eventos como fechar janela etc
            #for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      print('Quitting...')
               #     pygame.quit()  # close window
                #    quit()  # end pygame