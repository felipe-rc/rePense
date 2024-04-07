import pygame
from utils.constants import WIDTH, HEIGHT
from utils.Button import Button
from gameClass.gameClass import Game

pygame.init()
res = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("rePense")
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
smallfont = pygame.font.SysFont('Corbel', 35)

game = Game(screen)


new_game_surf = pygame.Surface((150, 64))
new_game_surf.fill(color_dark)
new_game_text_x_pos = (WIDTH / 2) - 100
new_game_button_x_pos = (WIDTH / 2) - 100
new_game_button_y_pos = 250

scores_surf = pygame.Surface((165, 64))
scores_surf.fill(color_dark)
scores_text_x_pos = (WIDTH / 2) - 115
scores_button_x_pos = (WIDTH / 2) - 115
scores_button_y_pos = 250 + 70

credits_surf = pygame.Surface((120, 64))
credits_surf.fill(color_dark)
credits_text_x_pos = (WIDTH / 2) - 70
credits_button_x_pos = (WIDTH / 2) - 70
credits_button_y_pos = 250 + (70 * 2)

info_surf = pygame.Surface((180, 64))
info_surf.fill(color_dark)
info_text_x_pos = (WIDTH / 2) - 130
info_button_x_pos = (WIDTH / 2) - 130
info_button_y_pos = 250 + (70 * 3)

new_game_button = Button(new_game_button_x_pos, new_game_button_y_pos, new_game_surf, 1)
scores_button = Button(scores_button_x_pos, scores_button_y_pos, scores_surf, 1)
credits_button = Button(credits_button_x_pos, credits_button_y_pos, credits_surf, 1)
info_button = Button(info_button_x_pos, info_button_y_pos, info_surf, 1)


def draw_text(text_el, font, text_col, x, y):
    img = font.render(text_el, True, text_col)
    screen.blit(img, (x, y))


def main():
    run = True
    while run:
        screen.fill((60, 25, 60))
        if new_game_button.draw(screen):
            game.start()
        draw_text("Novo Jogo", smallfont, color, new_game_text_x_pos, new_game_button_y_pos)

        if scores_button.draw(screen):
            print("scores")
        draw_text("Pontuações", smallfont, color, scores_text_x_pos, scores_button_y_pos)

        if credits_button.draw(screen):
            print("credits")
        draw_text("Créditos", smallfont, color, credits_text_x_pos, credits_button_y_pos)

        if info_button.draw(screen):
            print("info")

        draw_text("Informações", smallfont, color, info_text_x_pos, info_button_y_pos)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False

        pygame.display.update()


if __name__ == '__main__':
    main()
