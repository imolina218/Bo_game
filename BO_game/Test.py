import pygame, sys

pygame.init()
clock = pygame.time.Clock()
height, width = 680, 680
screen = pygame.display.set_mode([680, 680])
base_font = pygame.font.Font(None, 22)
user_text = ""
posible = ""
answer = "darkness"

input_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive

run = True
active = False


def img_adapt_f7():

    press_to_continue = base_font.render("Press ENTER to continue", 1, (255, 255, 255))

    screen.blit(press_to_continue, (height - press_to_continue.get_height() - 560, 600))

    pygame.display.update()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                    if event.key == pygame.K_RETURN:
                        print(user_text)
                        img_adapt_f7()



    screen.fill((0, 0, 0))

    if active:
        color = color_active
    else:
        color = color_passive
    pygame.draw.rect(screen, color, input_rect, 2)

    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(100, text_surface.get_width() + 10)
    pygame.display.flip()
    clock.tick(60)








