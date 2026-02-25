import pygame
import sys


def main():
    pygame.init()

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Putanica")

    BLUE = (0, 0, 255)
    WHITE = (135, 206, 235)
    GREEN = (34, 139, 34)
    YELLOW = (255, 255, 0)

    ship_x = 400
    ship_y = 450



    x = 500
    y = 0
    size = 50

    bonus_x = 700
    bonus_y = 300

    game_over = False
    font = pygame.font.Font(None, 74)

    jump = False
    jump_sila = 30
    na_zemle = False


    jump_vyshe = False

    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()


        if keys[pygame.K_a]:
            x -= 5
        if keys[pygame.K_d]:
            x += 5


        if na_zemle == False and jump == False:
            y += 7


        if y > 450:
            y = 450
            na_zemle = True


        if keys[pygame.K_SPACE] and na_zemle == True and jump == False:
            jump = True
            na_zemle = False


            if jump_vyshe == True:
                jump_sila = 30
                jump_vyshe = False
            else:
                jump_sila = 15


        if jump == True:
            y -= jump_sila
            jump_sila -= 1

            if y > 450:
                y = 450
                jump = False
                na_zemle = True


        if x + size > bonus_x and x < bonus_x + size:
            if y + size > bonus_y and y < bonus_y + size:
                bonus_x = -100
                bonus_y = -100
                jump_vyshe = True


        if x < 0:
            x = 0
        if x > 950:
            x = 950

        player_rect = pygame.Rect(x, y, size, size)
        ship_rect = pygame.Rect(ship_x, ship_y, 50, 50)

        if player_rect.colliderect(ship_rect):
            game_over = True

        if game_over:
            screen.fill("black")
            text = font.render("GAME OVER", True, "red")
            screen.blit(text, (339, 270))
        else:
            screen.fill(WHITE)

            pygame.draw.rect(screen, (255, 0, 0), (ship_x, ship_y, 50, 50))
            pygame.draw.rect(screen, GREEN, (0, 500, 1000, 100))
            pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
            pygame.draw.rect(screen, YELLOW, (bonus_x, bonus_y, 50, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()