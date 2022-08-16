import pygame
import time
from pygame.locals import *
import random





# colours
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
cyan = (32,180,194)

active_menu = 1 # ! 1 = Main Menu #2 = Game Screen #3 = Leaderboard
username_input = ""

#Variables to identify player
player_img_x = 400-17
player_img_y = 300-12
player_img_w = 34
player_img_h = 24

#Variables to identify base
base_img_x = 0
base_img_y = 600-66
base_img_w = 800
base_img_h = 66

#Variables to identify the top
top_img_x = 0
top_img_y = 0
top_img_w = 1195
top_img_h = -247

# Variables to identify gamover ss
gameover_img_x = 150
gameover_img_y = 150
gameover_img_w = 522
gameover_img_h = 343

# Variables to identify Pipes
#pipe1_x = 700
#pipe1_y = 0
#pipe1_w = 35
#pipe1_h = 220
pipes_x = [700, 800, 900, 1000, 1100]
pipes_y = [0, 0, 600, 0, 600]
pipes_w = [35, 35, 35, 35, 35]
pipes_h = [220, 220, 220, 220, 220]
pipe_gap_x = 35

# Variable for changing the horizontal speed of the pipes
pipe_speed_x = 0.3

gameover = False

lives = 3

score = 0

#Variable for changing the speed of decent
bird_speed_y = 0.65

#Variable for increasing the bird's alittude increment
bird_altitude_increment = 0

scores = []
usernames = []
leaderboard_numbers_text = []
leaderboard_numbers_rect = []

def inithighscores():
    scores.append(100) # Starts to append the scores
    scores.append(99)
    scores.append(98)
    scores.append(97)
    scores.append(96)
    scores.append(95)
    scores.append(94)
    scores.append(93)
    scores.append(92)
    scores.append(91) # End of appending scores

    usernames.append("James")
    usernames.append("Sarah")
    usernames.append("Car")
    usernames.append("Steven")
    usernames.append("Luke")
    usernames.append("Til")
    usernames.append("Eli")
    usernames.append("Scammer")
    usernames.append("Hacker")
    usernames.append("Beluga")

inithighscores()

def randomise_pipe_type():
    pipe = 0 #1 = long (UP) #2 short (UP) #3 long (DOWN)  #4 short (DOWN)

    pipe = random.randint(1, 4)

    return pipe

def gameLoop():  # ! Game Life Cycle

    running = True

    global player_img_y, player_img_x, player_img_w, player_img_h
    global base_img_y, base_img_x, base_img_w, base_img_h
    global pipes_y, pipes_x, pipes_w, pipes_h
    global gameover_img_y, gameover_img_x, gameover_img_w, gameover_img_h
    global top_img_y, top_img_x, top_img_w, top_img_h

    global active_menu
    global bird_altitude_increment
    global gameover
    global lives
    global score
    global username_input
    global scores, usernames
    global leaderboard_numbers_text, leaderboard_numbers_rect


    while running: # 1 frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif running == False:
                pygame.quit()


            elif event.type == pygame.MOUSEBUTTONUP:  # * Creating a new event (Detecting the Mouse Button Release)
                if active_menu == 1:
                    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()  # * Gets the current mouse position (Only needed once per each: if active_menu ==)
                    print("x=", mouse_pos_x, "y=", mouse_pos_y)

                    if start_text_rect.collidepoint(mouse_pos_x,mouse_pos_y) == True:  # Detecting Mouse Input (x,y) on user release #! (Play)
                        print("Play has been clicked")
                        player_img_x = 400 - 17 # Resets the Player's x value
                        player_img_y = 300 - 5 # Resets the Player's y value
                        pipes_x = [700, 800, 900, 1000, 1100] # Resets the array's x value
                        pipes_y = [0, 0, 534-220, 0, 534-220] # REsets the array's y value
                        score = 0


                        pipes = [] # Reseting the pipes
                        pipes.append(pygame.image.load('pipe_up.png'))
                        pipes.append(pygame.image.load('pipe_up.png'))
                        pipes.append(pygame.image.load('pipe_down.png'))
                        pipes.append(pygame.image.load('pipe_up.png'))
                        pipes.append(pygame.image.load('pipe_down.png'))


                        lives = 3 # Resetting the lives
                        active_menu = 2 # Moving to active_menu 2


                    elif leaderboard_button_rect.collidepoint(mouse_pos_x,
                                                              mouse_pos_y) == True:  # Detecting Mouse Input (x,y) on user release #! (Leaderboard)
                        print("Leaderboard has been clicked")
                        active_menu = 3


                elif active_menu == 3:
                    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()  # Gets the current mouse position
                    print("x=", mouse_pos_x, "y=", mouse_pos_y)

                    if back_button_rect.collidepoint(mouse_pos_x,
                                                     mouse_pos_y) == True:  # Detecting Mouse Input (x,y) on user release #! (Back Button)
                        print("Back has been clicked")
                        active_menu = 1

                elif active_menu == 4:
                    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()  # Gets the current mouse position
                    print("x=", mouse_pos_x, "y=", mouse_pos_y)

                    if restart_button_rect.collidepoint(mouse_pos_x,
                                                 mouse_pos_y) == True:  # Detecting Mouse Input (x,y) on user release #! (Back Button)
                        print("Restart has been clicked")
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('bg_music.mp3'))
                        active_menu = 1

            elif event.type == pygame.KEYDOWN:
                if active_menu == 1:
                    keys = pygame.key.get_pressed()
                    if keys[K_LSHIFT] and keys[K_a]:
                        username_input = username_input + "A"

                    elif keys[K_a]:
                        username_input = username_input + "a"

                    elif keys[K_BACKSPACE]:
                       username_input = username_input[0:len(username_input) - 1]



                elif active_menu == 2:
                    keys = pygame.key.get_pressed()
                    if keys [K_SPACE]:
                        bird_altitude_increment = 60
                        print('Space has been pressed')
                        pygame.mixer.music.load('wing.wav')
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('wing.wav'))





        #Draws on each interface

        if active_menu == 1:  # ! First Interface
            screen.fill(black)

            # * Drawing the Background
            screen.blit(bg_menu, (0, 0))

            # * Displays the Play Button
            screen.blit(start_text, start_text_rect)

            # * Displays the High Score Text
            screen.blit(highscore_text, highscore_text_rect)

            # Displays the 'Enter Username:' Text
            username_user = font2.render(username_input, True,
                                         (255, 255, 255))  # Creating a button for Username #!
            screen.blit(username_text, username_text_rect)
            screen.blit(username_user, username_user_rect)


            # * Displays the button to take the user to the leaderboard interface
            screen.blit(leaderboard_button, leaderboard_button_rect)

            pygame.display.update()  # * Updates the screen

        elif active_menu == 2:  # ! Second Inteface
            screen.fill(blue)

            screen.blit(bg_game, (0, 0))  # * Displays the background

            screen.blit(top_img,(0, 0))


            for i in range(len(pipes)):
                pipes_x[i] = pipes_x[i] - pipe_speed_x

            for i in range(len(pipes)): # Looks for number of pipes in the array
                screen.blit(pipes[i], (pipes_x[i], pipes_y[i])) # Displays the pipe

            for i in range(len(pipes)):
                distance = player_img_x - pipes_x[i]
                if distance >=-0.15 and distance <= 0.15:
                    score = score + 1
                    pygame.mixer.music.load("smw_coin.wav")
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound('smw_coin.wav'))
                    print('Score is ' + str(score))


            for i in range(len(pipes)): # Checks if the pipes are outside of the window
                if pipes_x[i] <= -35:
                    pipes_x[i] = 800 - pipe_gap_x # Moves the pipes to the right side of the window

                    print(randomise_pipe_type())  # 1 U LONG 2 U SHORT 3 D LONG 4 D SHORT
                    new_pipe_type = randomise_pipe_type()
                    if new_pipe_type == 1:
                        pipes[i] = pygame.image.load('pipe_up.png')
                        pipes_y[i] = 0
                    elif new_pipe_type == 2:
                        pipes[i] = pygame.image.load('pipe_up.png')
                        pipes_y[i] = -(pipes_h[i] / 2)

                    elif new_pipe_type == 3:
                        pipes[i] = pygame.image.load('pipe_down.png')
                        pipes_y[i] = 534-220

                    elif new_pipe_type == 4:
                        pipes[i] = pygame.image.load('pipe_down.png')
                        pipes_y[i] = (534-220) + (pipes_h[i] / 2)

            screen.blit(base_img, (0, 534))

            score_text = font2.render("Score: " + str(score), True, (255, 255, 255))  # Creating a Score Text

            screen.blit(score_text, score_text_rect)

            screen.blit(timer_text, timer_text_rect)

            if lives == 3:
                for i in range(0, 3):
                    screen.blit(lives_img, (700 - (i * 50), 30))
            elif lives == 2:
                for i in range(0, 2):
                    screen.blit(lives_img, (700 - (i * 50), 30))
            elif lives == 1:
                for i in range(0, 1):
                    screen.blit(lives_img, (700 - (i * 50), 30))

            #if lives == 3:
                #screen.blit(lives_img, (600,30))
                #screen.blit(lives_img, (650,30))
                #screen.blit(lives_img, (700,30))
            #elif lives == 2:
                #screen.blit(lives_img, (650, 30))
                #screen.blit(lives_img, (700, 30))
            #elif lives == 1:
                #screen.blit(lives_img, (700, 30))


            if bird_altitude_increment > 0: #Begins to move up
                bird_altitude_increment = bird_altitude_increment - bird_speed_y
                player_img_y = player_img_y - bird_speed_y #Changes the y value
                #bird_altitude_increment = 0
            else: #Begins to move down
                player_img_y = player_img_y + (bird_speed_y) # Decreases the y value

            #checking Collision
            bird_rect = Rect(player_img_x, player_img_y, player_img_w, player_img_h)
            base_rect = Rect(base_img_x, base_img_y, base_img_w, base_img_h)
            pipes_rect = []
            for i in range(len(pipes_x)):
                pipes_rect.append(Rect(pipes_x[i], pipes_y[i], pipes_w[i], pipes_h[i]))

            top_rect = Rect(top_img_x, top_img_y, top_img_w, top_img_h)
            if bird_rect.colliderect(base_rect) == True:
                lives = lives - 1
                pygame.mixer.music.load('die.wav')  # Loads in die.wav
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('die.wav'))  # Plays die.wav
                player_img_x = 400 - 17
                player_img_y = 300 - 12

            for i in range(len(pipes_x)):
                if bird_rect.colliderect(pipes_rect[i]) == True:
                    lives = lives - 1
                    pygame.mixer.music.load('die.wav')  # Loads in die.wav
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound('die.wav'))  # Plays die.wav

                    pipes = [] # Resets the pipes array
                    pipes.append(pygame.image.load('pipe_up.png'))
                    pipes.append(pygame.image.load('pipe_up.png'))
                    pipes.append(pygame.image.load('pipe_down.png'))
                    pipes.append(pygame.image.load('pipe_up.png'))
                    pipes.append(pygame.image.load('pipe_down.png'))

                    pipes_x = [700, 800, 900, 1000, 1100]  # Resets the array's x value
                    pipes_y = [0, 0, 534 - 220, 0, 534 - 220]  # REsets the array's y value
                    player_img_x = 400 - 17
                    player_img_y = 300 - 12
                    print('You have hit a wall')

            if bird_rect.colliderect(top_rect) == True:
                player_img_y = 0

                #active_menu = 1
            if lives == 0:
                    gameover = True
                    pygame.mixer.Channel(1).stop()
                    pygame.mixer.music.load("smw_game_over.wav")
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound('smw_game_over.wav'))
                    active_menu = 4


            screen.blit(player_img, (player_img_x,player_img_y)) #Displays the Bird-Character

            pygame.display.update()  # * Updates the screen

        ##### Create another Interface
        elif active_menu == 3:  # ! Third Inteface
            screen.fill(red)

            screen.blit(bg_leaderboard, (0, 0))

            screen.blit(leaderboard_text, leaderboard_text_rect)

            screen.blit(back_button, back_button_rect)  # * Displays the Back Button

            screen.blit(leaderboard1hour,
                        leaderboard1hour_rect)  # * Displays the button to take the user to the 1-hour leaderboard
            for i in range(len(leaderboard_numbers_text)):
                screen.blit(leaderboard_numbers_text[i], leaderboard_numbers_rect[i])



            screen.blit(leaderboard24hour,
                        leaderboard24hour_rect)  # * Displays the button to take the user to the 24-hour leaderboard


            pygame.display.update()  # * Updates the screen


        elif active_menu == 4:  # Fourth Interface
           pygame.mixer.music.stop

           screen.fill(cyan)

           screen.blit(bg_gameover, (gameover_img_x, gameover_img_y))

           screen.blit(restart_button, restart_button_rect)

          # screen.blit(restartgame_text, restartgame_text_rect)


           pygame.display.update()  # * Updates the screen


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("The Flappy Banana")

    # * Loading in Images (Buttons and Lives)
    start_img = pygame.image.load('start_button.png').convert_alpha()
    lives_img = pygame.image.load('lives.png').convert_alpha()


    # *  Loading the Background for Main Menu
    bg_menu = pygame.image.load('bg_menu.jpg')

    # *  Loading the Background for Leaderboard
    bg_leaderboard = pygame.image.load('bg_game.jpg')
    bg_gameover = pygame.image.load('gameover.png')

    # *  Loading the Background for Gameplay
    bg_game = pygame.image.load('bg_game.jpg')

    # Loading in the Bird
    player_img = pygame.image.load('bird.png')

    #Loading the base
    base_img = pygame.image.load('base.png')

    # Loading the top
    top_img = pygame.image.load('tbarrier.png')

    #Loading the Pipes
    #pipe_up_img = pygame.image.load('pipe_up.png')
    #pipe_down_img = pygame.image.load('pipe_down.png')

    # Removing the background of pipe_up.png and pipe_down.png
    #colorkey = pipe_up_img.get_at((1, 1))
    #pipe_up_img.set_colorkey(colorkey)

    pipes = []
    pipes.append(pygame.image.load('pipe_up.png'))
    pipes.append(pygame.image.load('pipe_up.png'))
    pipes.append(pygame.image.load('pipe_down.png'))
    pipes.append(pygame.image.load('pipe_up.png'))
    pipes.append(pygame.image.load('pipe_down.png'))

    # Removing the Background of Bird.png
    colorkey = player_img.get_at((1, 1))
    player_img.set_colorkey(colorkey)  # Removes the white background

    # * Creating Start, High Score and Leaderboard Text
    font1 = pygame.font.SysFont("Comic Sans MS", 40)  # Creating a new font for play button

    font2 = pygame.font.SysFont("Comic Sans MS", 30)  # Creating a new font for highscore text

    flappyfont = pygame.font.Font("FlappyBirdy.ttf", 55)  # ? Creating a new Flappy Bird Themed Font

    start_text = flappyfont.render("Play", True, (255, 255, 255))  # Creating a Text Button

    highscore_text = flappyfont.render("High Score ", True, (255, 255, 255))  # Creating a High Score Text

    leaderboard_text = flappyfont.render("Highest Scores ", True, (255, 255, 255))  # Creating a Leaderboard Text

    leaderboard_button = flappyfont.render("Leaderboard", True, (255, 255, 255))  # Creating a Leaderboard Button

    back_button = flappyfont.render("Back", True, (255, 255, 255))  # Creating a Back Button

    restart_button = flappyfont.render("Restart", True, (255, 255, 255))  # Creating a Back Button

    leaderboard1hour = font2.render("Last Hour", True,
                                    (255, 255, 255))  # Creating a button for last hour #! (Leaderboard)

    leaderboard24hour = font2.render("Last 24 Hours", True,
                                     (255, 255, 255))  # Creating a button for last hour #! (Leaderboard)

    username_text = font2.render("Enter Username: ", True,
                                     (255, 255, 255))  # Creating a button for Username #!

    username_user = font2.render(username_input, True,
                                 (255, 255, 255))  # Creating a button for Username #!


    for i in range(len(scores)):
        leaderboard_numbers_text.append(font2.render( str(i + 1) + ". " + usernames[i] + ', ' + str(scores[i]), True,
                                 (255, 255, 255)))


    timer_text = font2.render("Timer: ", True , (255, 255, 255))  # Creating a Timer Text

    score_text = font2.render("Score: " + str(score), True, (255, 255, 255))  # Creating a Score Text

    lives_text = font2.render("Lives: ", True, (255, 255, 255))  # Creating a lives Text

    # Creates the rectangle for Text Button
    start_text_rect = start_text.get_rect()
    start_text_rect.move_ip(350, 510)

    # Creates the Rectangle for the Highscore Text
    highscore_text_rect = start_text.get_rect()
    highscore_text_rect.move_ip(35, 510)

    # Creates the Leaderboard text rectangle
    leaderboard_text_rect = leaderboard_text.get_rect()
    leaderboard_text_rect.move_ip(285, 50)

    # Creates the rectancle of the button to take the user to Inferface #3
    leaderboard_button_rect = leaderboard_button.get_rect()
    leaderboard_button_rect.move_ip(600, 510)

    # Creates the rectangle of the Back Button
    back_button_rect = back_button.get_rect()
    back_button_rect.move_ip(45, 565)

    # Creates the rectangle of the restart button
    restart_button_rect = restart_button.get_rect()
    restart_button_rect.move_ip(165, 565)

    # Creates the rectangle of the Last Hour on Leaderboard
    leaderboard1hour_rect = leaderboard1hour.get_rect()
    leaderboard1hour_rect.move_ip(45, 65)

    # Creates the rectangle of the Last 24 Hours on Leaderboard
    leaderboard24hour_rect = leaderboard24hour.get_rect()
    leaderboard24hour_rect.move_ip(550, 65)

    # Creates a the rectangle of the username box
    username_text_rect = username_text.get_rect()
    username_text_rect.move_ip(45, 350)

    username_user_rect = username_user.get_rect()
    username_user_rect.move_ip(295, 350)

    for i in range(len(scores)):
        leaderboard_numbers_rect.append(leaderboard_numbers_text[i].get_rect())
        leaderboard_numbers_rect[i].move_ip(45, 115 + (i * 45))



    # Creates rectangles for timer, scoire and lives

    timer_text_rect = timer_text.get_rect()
    timer_text_rect.move_ip(125, 50)

    score_text_rect = score_text.get_rect()
    score_text_rect.move_ip(340, 50)

    lives_text_rect = lives_text.get_rect()
    lives_text_rect.move_ip(550, 50)



    # ! Load Music
    pygame.mixer.music.load('bg_music.wav')


    # ! Play Music
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('bg_music.wav'), loops = -1)
    pygame.mixer.Channel(1).set_volume(0.5)

    # Stop Music
    if active_menu == 4:
        pygame.mixer.Channel(1).stop

    gameLoop()
    #pygame.quit()


