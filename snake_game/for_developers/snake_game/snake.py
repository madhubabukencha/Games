"""
Author : Madhu Babu Kencha
Created on : 29-19-2019

Inspiration:
https://www.edureka.co/blog/snake-game-with-pygame/
"""
import pygame
import time
import random

# Initializing all pygame modules
pygame.init()

# Creating game screen
screen_width = 800  # column
screen_height = 580  # rows
my_screen = pygame.display.set_mode(size=[screen_width, screen_height])

# Setting icon (Changing pygame default icon)
screen_icon = pygame.image.load('nature.jpg')
pygame.display.set_icon(screen_icon)

# Defining snake speed
snake_speed = 5
snake_block = 10  # Not dynamic so don't touch it

# RGB colors: https://python-forum.io/Thread-PyGame-PyGame-Colors
red = (255, 0, 0, 255)
white = (255, 255, 255, 255)
blue = (0, 0, 179)
green = (0, 255, 0)
purple = (240, 0, 255)
yellow = (255, 255, 0)
moon_glow = (235, 245, 255)
dark_red = (24.7, 0, 0)
cyan = (51, 255, 255)
gold = (255, 215, 0)


# To set background image
# Make sure screen size and image size is same to get good results
all_background_images = ['nature.jpg']
image = random.choice(all_background_images)
background_image = pygame.image.load(image)

# To update any changes made to the screen
pygame.display.set_caption("Snake Game")

# To track the frame speed
# In general how speed snake has to move
# http://pygametutorials.wikidot.com/book-time
clock = pygame.time.Clock()

# Adding continuous background music
# Source : http://www.orangefreesounds.com/
all_background_songs = ["emotional_piano.mp3", "ambient_music.mp3"]
music = random.choice(all_background_songs)
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1, 0.0)

# Adding sound effects
food_eating = pygame.mixer.Sound("eating.wav")
# wall_hitting = pygame.mixer.Sound("wall_hitting.wav")
ending_effect = pygame.mixer.Sound("ending.wav")


def message(msg, font_color, size, default_position=[screen_width/3, screen_height/2]):
    """It will display the message at center of screen"""
    # window fonts : http://www.ampsoft.net/webdesign-l/WindowsMacFonts.html
    font_style_size = pygame.font.SysFont("Times New Roman", size)
    my_message = font_style_size.render(msg, True, font_color)
    my_screen.blit(my_message, default_position)


def snake_food_position():
    """This function returns the snake food position"""
    x_food = round(random.randint(0, screen_width-snake_block) / 10) * 10.0
    y_food = round(random.randint(0, screen_height-snake_block) / 10) * 10.0
    return x_food, y_food


def my_snake(snake_block, snake_list):
    for snake in snake_list:
        snake_x = snake[0]
        snake_y = snake[1]
        pygame.draw.rect(my_screen, blue, [snake_x, snake_y, snake_block, snake_block])


def game_score(score):
    """I will display the game score"""
    score_font_style = pygame.font.SysFont("Times New Roman", 35)
    value = score_font_style.render(f"Your Score: {score}", True, dark_red)
    my_screen.blit(value, [0, 0])


def final_game():
    # To stop immediately closing and to control came flow
    game_over = False
    game_close = False

    # Positions of x, y
    # Helps to create snake starting point
    # Helps to exit, based on boundaries
    current_x = screen_width / 2
    current_y = screen_height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    # To stop going in the opposite direction
    # Which means for example if your going down and if press up
    # It shouldn't go up
    direction = ""
    x_food, y_food = snake_food_position()
    while not game_over:
        while game_close:
            game_close_msg = "You loose the Game !!! Press Q-Quit or C-Play Again"
            msg_position = [screen_width/7, screen_height/2]
            message(game_close_msg, white, 30, msg_position)
            pygame.display.update()
            pygame.mixer.music.pause()
            if event.type == pygame.QUIT:
                ending_effect.play()
                game_close = False
                game_over = True
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        ending_effect.play()
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        pygame.mixer.music.unpause()
                        final_game()

        for event in pygame.event.get():
            # This helps to close the screen whenever you click on cancel button
            if event.type == pygame.QUIT:
                pygame.mixer.music.pause()
                ending_effect.play()
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "right":
                    x_change = -snake_block
                    y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    x_change = snake_block
                    y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP and direction != "down":
                    y_change = -snake_block
                    x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    y_change = snake_block
                    x_change = 0
                    direction = "down"
                elif event.key == pygame.K_p:
                    msg_position = [screen_width / 8, screen_height / 2]
                    message("Pause and press \'R\' to resume", white, 45, msg_position )
                    pygame.display.update()
                    pause = False
                    while not pause:
                        for my_event in pygame.event.get():
                            if my_event.type == pygame.QUIT:
                                ending_effect.play()
                                game_over = True
                                pause = True
                            if my_event.type == pygame.KEYDOWN:
                                if my_event.key == pygame.K_r:
                                    pause = True
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    ending_effect.play()
                    game_over = True

        if current_x >= screen_width or current_x < 0 or current_y >= screen_height or current_y < 0:
            ending_effect.play()
            game_close = True
            # It will print the event occurring on the screen
            # print(event)

        # https://stackoverflow.com/questions/47878264/background-image-not-appearing-in-pygame
        my_screen.blit(background_image, [0, 0])

        current_x += x_change
        current_y += y_change
        # pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
        # left = 1 means, screen left side(you can say first column)
        # top = 1 means, screen top side(you can say first row)

        # Rectangle for food
        pygame.draw.rect(my_screen, red, [x_food, y_food, snake_block, snake_block])

        # Rectangle for snake
        snake_head = [current_x, current_y]
        # print(f"snake_head : {snake_head}")
        snake_list.append(snake_head)
        # print(f"snake_list : {snake_list}")
        # print(f"length fo the snake : {length_of_snake}")
        if len(snake_list) > length_of_snake:
            # print(f"deleting : {snake_list[0]}")
            del snake_list[0]
        for x in snake_list[:-1]:
            # print(f"x: {x}")
            if x == snake_head:
                # print(f"x : {x}, snake_head : {snake_head}")
                game_close = True
        # print(f"snake_list : {snake_list}")
        # print(" ")
        # time.sleep(1) # useful for debugging

        my_snake(snake_block, snake_list)
        game_score(length_of_snake-1)
        pygame.display.update()

        # print(f"current_x : {current_x}")
        # print(f"current_y : {current_y}")
        # print(f"x_food : {x_food}")
        # print(f"y_food : {y_food}")
        # print(" ")
        # time.sleep(1) # useful for debugging
        if current_x == x_food and current_y == y_food:
            x_food, y_food = snake_food_position()
            length_of_snake += 1
            food_eating.play()
        clock.tick(snake_speed)


final_game()
message("Game Over", red, 70)
pygame.display.update()

# To stay after end
time.sleep(2)

# un-initializing all pygame modules
pygame.quit()
quit()