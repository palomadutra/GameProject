import pygame

pygame.init()
window = pygame.display.set_mode(size=(800, 600))

while True:
    # Check for all events
    # todos os eventos como fechar janela etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # close window
            quit() #end pygame