import pygame
import os
pygame.font.init()

width, height = 680, 680
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bo game")

# Load images
main_background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),
                                         (width, height))


def main():
    run = True
    fps = 60
    level = 0
    lives = 4
    score = 0
    raghnak = True
    lordk = True
    usarkna = True
    main_font = pygame.font.SysFont("comicsans", 30)
    title_font = pygame.font.SysFont("comicsans", 60)
    clock = pygame.time.Clock()
    text = ''
    user_text = ''
    
    def img_adapt():
        window.blit(main_background, (0, 0))
        # apply text
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))
        press_to_continue = title_font.render("Press ENTER to continue", 1, (255, 255, 255))

        window.blit(lives_label, (20, 15))
        window.blit(level_label, (width - level_label.get_width() - 20, 15))
        window.blit(score_label, (width - score_label.get_width() - 20, 35))

        window.blit(press_to_continue, (width - press_to_continue.get_width() - 20, 100))

        pygame.display.update()
        
    while run:
        clock.tick(fps)
        img_adapt()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False











main()
