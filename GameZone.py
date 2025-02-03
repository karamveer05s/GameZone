from cgitb import text
import numbers
from pprint import pp
import sys
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pyautogui
from pygame import mixer
import mysql.connector as sqlcon
import re
from pygame.locals import *
import smtplib
import math, random
import ctypes

#----------------------------------------------------Database-------------------------------------------------------------
def connect_with_database():
    global dbcon
    global cursor
    dbcon = sqlcon.connect(
        host = "localhost",
        user = 'root',
        password = 'admin',
    )
    cursor = dbcon.cursor()

try:
    connect_with_database()
except:
    #ask_MySQL_username_password()
    connect_with_database()

def create_database_and_table():
    operation = """CREATE DATABASE IF NOT EXISTS gamezone"""
    cursor.execute(operation)

    operation = """USE gamezone"""
    cursor.execute(operation)

    operation = """CREATE TABLE IF NOT EXISTS player_details(
					username            VARCHAR(30)          NOT NULL    PRIMARY KEY,
					password            VARCHAR(15)          NOT NULL,
					email               VARCHAR(50)          NOT NULL,
                    number              VARCHAR(15)          NOT NULL,
                    age                 VARCHAR(100)         NOT NULL,
                    snake_easy          BIGINT(50)          ,
                    snake_medium        BIGINT(50)          ,
                    snake_hard          BIGINT(50)          ,
                    car                 BIGINT(50)          ,
                    dodge_ball          BIGINT(50)          )"""
    cursor.execute(operation)
    
create_database_and_table()

#--------------------------------------------------------------------------------------------------------------------
gamezone = Tk()

#--------------------Sign-In Detection    
def psignin():
    global p_username
    global pname
    global ppass
    player_username = pname.get()
    player_passsword = ppass.get()
    
    
    data = [player_username, player_passsword]    
    for i in data:
        if (i == player_username):
            if (len(i) == 0):
                messagebox.showerror("GameZone", "Please enter Username.")
                return
        elif (i == player_passsword):
            if (len(i) != 6):
                messagebox.showerror("GameZone", "Please enter 6 digits of password.")
                return
    try:
        operation = "SELECT *FROM player_details where username ='%s'"%(player_username)
        cursor.execute(operation)
        results = cursor.fetchall()

        global p_snake_easy
        global  p_snake_medium
        global p_snake_hard
        global p_car
        global p_daudge_ball
        for rec in results:
            p_username = rec[0]
            p_password = rec[1]
            p_snake_easy = rec[5]
            p_snake_medium = rec[6]
            p_snake_hard = rec[7]
            p_car = rec[8]
            p_daudge_ball = rec[9]
        
        if (player_passsword == p_password):
            messagebox.showinfo("GameZone","You Are Scuccessfully Login.")
            signin.withdraw()
        else:
            messagebox.showerror("GameZone","Please Enter Correct Password!.")
            return
    except:
        messagebox.showerror("GameZone","Please Enter Correct Username and Password")
        return
    
    gamezone.withdraw()
    froot.deiconify()
        

    Label(scroreframe,text="----------------------------------------------------------------------",font=("times new roman",15,"bold"),bg="ghostwhite",fg="black").place(x=0,y=35)
    
    show_details1 = Label(scroreframe,text="Welcome "+str(p_username),font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details1.place(x=10,y=10)
    global show_details2_1
    show_details2 = Label(scroreframe,text="Snake Game Easy Level",font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details2.place(x=10,y=60)
    show_details2_1 = Label(scroreframe,text="High Score : "+str(p_snake_easy),font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details2_1.place(x=10,y=90)
    
    global show_details3_1
    show_details3 = Label(scroreframe,text="Snake Game Medium Level",font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details3.place(x=10,y=140)
    show_details3_1 = Label(scroreframe,text="High Score : "+str(p_snake_medium),font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details3_1.place(x=10,y=170)
    
    global show_details4_1
    show_details4 = Label(scroreframe,text="Snake Game Hard Level",font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details4.place(x=10,y=220)
    show_details4_1 = Label(scroreframe,text="High Score : "+str(p_snake_hard),font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details4_1.place(x=10,y=250)
    
    Label(scroreframe,text="----------------------------------------------------------------------",font=("times new roman",15,"bold"),bg="ghostwhite",fg="black").place(x=0,y=282)
    
    global show_details5_1
    show_details5 = Label(scroreframe,text="Car Game",font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details5.place(x=10,y=310)
    show_details5_1 = Label(scroreframe,text="High Score : "+str(p_car),font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details5_1.place(x=10,y=340)
    
    Label(scroreframe,text="----------------------------------------------------------------------",font=("times new roman",15,"bold"),bg="ghostwhite",fg="black").place(x=0,y=372)
    
    global show_details6_1
    show_details6 = Label(scroreframe,text="Daudge The Ball",font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details6.place(x=10,y=405)
    show_details6_1 = Label(scroreframe,text="High Score : "+str(p_daudge_ball),font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
    show_details6_1.place(x=10,y=440)
    


def player_register():
    try:
        signin.withdraw()
        pregister.deiconify()
    except:
        messagebox.showerror("Gamezone","Please Restart The Game.!")


#-------------------------------------------------Backgroung Image-----------------------------------------------------
screenwidth,screenheight = pyautogui.size()
backgroundimg=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\gamezone.jpg")
resizebackimg = backgroundimg.resize((1925, 1080), Image.LANCZOS)
mainbackimg=ImageTk.PhotoImage(resizebackimg)

# mainbacklabel = Label(gamezone,image=mainbackimg,height=screenheight,width=screenwidth).grid(row=0,column=0)
mainbacklabel = Label(gamezone,image=mainbackimg,height=717,width=1498).place(x=0,y=0)


#-----------------------------------------------------------------------------------------------------------------------------
img5=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\welcome.jpg")
ph5=ImageTk.PhotoImage(img5)
Label(gamezone,image=ph5).place(x=540,y=10)
#-------------------------------------------Snake Game-----------------------------------------------------------------
def defsnakegame():
    import pygame, sys, time, random
    import tkinter
        
    snakewindow = Toplevel()                                   #snakegame level window
    snakewindow.geometry("720x480+285+125")
#------------------------------------------------snake level Background Image---------------------------------------------------------------
    backgroundimg=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\gamewindowbackground.jpg")
    resizebackimg = backgroundimg.resize((720, 480), Image.LANCZOS)
    mainsnakebackimg=ImageTk.PhotoImage(resizebackimg)
    mainsnakebacklabel = Label(snakewindow,image=mainsnakebackimg)
    mainsnakebacklabel.grid(row=0,column=0)
#-------------------------------------------------Easy Level-----------------------------------------------------------
    def snakegameeasylevel():
        try:
        # Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
            difficulty = 10


# Checks for errors encountered
            check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
            if check_errors[1] > 0:
                print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
                sys.exit(-1)
            else:
                print('[+] Game successfully initialised')


# Initialise game window
            info = pygame.display.Info()
            frame_size_x = info.current_w  # Screen Width
            frame_size_y = info.current_h  # Screen Height
            game_window = pygame.display.set_mode((frame_size_x-50, frame_size_y-50), pygame.RESIZABLE)
            pygame.display.set_caption('Snake Eater')
            pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, {"w": frame_size_x, "h": frame_size_y}))
            ctypes.windll.user32.ShowWindow(pygame.display.get_wm_info()["window"], 3)



# Colors (R, G, B)
            black = pygame.Color(0, 0, 0)
            white = pygame.Color(255, 255, 255)
            red = pygame.Color(255, 0, 0)
            green = pygame.Color(0, 255, 0)
            blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
            fps_controller = pygame.time.Clock()


# Game variables
            snake_pos = [100, 50]
            snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

            food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
            food_spawn = True

            direction = 'RIGHT'
            change_to = direction

            score = 0

# Game Over
            def game_over():
                mixer.init()
                mixer.music.load(r"C:\Users\rajpu\Desktop\GameZone\Music File\Snake Game\out.mp3")
                mixer.music.play()
                my_font = pygame.font.SysFont('times new roman', 60)
                game_over_surface = my_font.render('YOU DIED.....Play Again.!', True, red)
                game_over_rect = game_over_surface.get_rect()
                game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
                game_window.fill(black)
                game_window.blit(game_over_surface, game_over_rect)
                show_score(0, red, 'times', 20)
                pygame.display.flip()
                time.sleep(1.3)
                pygame.quit()
# Score
            def show_score(choice, color, font, size):
                global p_username
                score_font = pygame.font.SysFont(font, size)
                score_surface = score_font.render('Score : ' + str(score), True, color)
                score_rect = score_surface.get_rect()

#----------------------------------------Store Score In DataBase----------------------------------------------------------
                try:
                    global p_snake_easy
                    if score>p_snake_easy:
                        show_details2_1.configure(text="High Score : "+str(score))
                        gamezone.update()
                        operation = "UPDATE player_details SET snake_easy=%s where username =%s"
                        data = (score,p_username)
                        cursor.execute(operation,data)
                        dbcon.commit()
                except:
                    messagebox.showerror("GameZone","Play This Game After Sign-In.")
                    pygame.quit()
            
                if choice == 1:
                    score_rect.midtop = (frame_size_x/10, 15)
                else:
                    score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
                game_window.blit(score_surface, score_rect)
    # pygame.display.flip()
# Main logic
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    #sys.exit()
        # Whenever a key is pressed down
                    elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
                        if event.key == pygame.K_UP or event.key == ord('w'):
                            change_to = 'UP'
                        if event.key == pygame.K_DOWN or event.key == ord('s'):
                            change_to = 'DOWN'
                        if event.key == pygame.K_LEFT or event.key == ord('a'):
                            change_to = 'LEFT'
                        if event.key == pygame.K_RIGHT or event.key == ord('d'):
                            change_to = 'RIGHT'
            # Esc -> Create event to quit the game
                        if event.key == pygame.K_ESCAPE:
                            pygame.event.post(pygame.event.Event(pygame.QUIT))
    # Making sure the snake cannot move in the opposite direction instantaneously
                if change_to == 'UP' and direction != 'DOWN':
                    direction = 'UP'
                if change_to == 'DOWN' and direction != 'UP':
                    direction = 'DOWN'
                if change_to == 'LEFT' and direction != 'RIGHT':
                    direction = 'LEFT'
                if change_to == 'RIGHT' and direction != 'LEFT':
                    direction = 'RIGHT'
    # Moving the snake
                if direction == 'UP':
                    snake_pos[1] -= 10
                if direction == 'DOWN':
                    snake_pos[1] += 10
                if direction == 'LEFT':
                    snake_pos[0] -= 10
                if direction == 'RIGHT':
                    snake_pos[0] += 10
    # Snake body growing mechanism                Snake Bit
                snake_body.insert(0, list(snake_pos))
                if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
                    mixer.init()
                    mixer.music.load(r"C:\Users\rajpu\Desktop\GameZone\Music File\Snake Game\bite.mp3")
                    mixer.music.play()
                    score += 1
                    food_spawn = False
                else:
                    snake_body.pop()
    # Spawning food on the screen
                if not food_spawn:
                    food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
                food_spawn = True
    # GFX
                game_window.fill(black)
                for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
                    pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    # Snake food
                pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    # Game Over conditions
    # Getting out of bounds
                if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
                    game_over()
                if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
                    game_over()
    # Touching the snake body
                for block in snake_body[1:]:
                    if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                        game_over()
                show_score(1, white, 'consolas', 20)
    # Refresh game screen
                pygame.display.update()
    # Refresh rate
                fps_controller.tick(difficulty)
        except:
            pass
            
#------------------------------------------------- Medium Level------------------------------------------------------------
    def snakegamemediumlevel():
        try:
        # Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
            difficulty1 = 25


# Checks for errors encountered
            check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
            if check_errors[1] > 0:
                print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
                sys.exit(-1)
            else:
                print('[+] Game successfully initialised')


# Initialise game window
            info = pygame.display.Info()
            frame_size_x = info.current_w  # Screen Width
            frame_size_y = info.current_h  # Screen Height
            game_window = pygame.display.set_mode((frame_size_x-50, frame_size_y-50), pygame.RESIZABLE)
            pygame.display.set_caption('Snake Eater')
            pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, {"w": frame_size_x, "h": frame_size_y}))
            ctypes.windll.user32.ShowWindow(pygame.display.get_wm_info()["window"], 3)


# Colors (R, G, B)
            black = pygame.Color(0, 0, 0)
            white = pygame.Color(255, 255, 255)
            red = pygame.Color(255, 0, 0)
            green = pygame.Color(0, 255, 0)
            blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
            fps_controller = pygame.time.Clock()


# Game variables
            snake_pos = [100, 50]
            snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

            food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
            food_spawn = True

            direction = 'RIGHT'
            change_to = direction

            score = 0


# Game Over
            def game_over():
                mixer.init()
                mixer.music.load(r"C:\Users\rajpu\Desktop\GameZone\Music File\Snake Game\out.mp3")
                mixer.music.play()
                my_font = pygame.font.SysFont('times new roman', 60)
                game_over_surface = my_font.render('YOU DIED.....Play Again.!', True, red)
                game_over_rect = game_over_surface.get_rect()
                game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
                game_window.fill(black)
                game_window.blit(game_over_surface, game_over_rect)
                show_score(0, red, 'times', 20)
                pygame.display.flip()
                time.sleep(1.3)
                pygame.quit()
# Score
            def show_score(choice, color, font, size):
                score_font = pygame.font.SysFont(font, size)
                score_surface = score_font.render('Score : ' + str(score), True, color)
                score_rect = score_surface.get_rect()
                if choice == 1:
                    score_rect.midtop = (frame_size_x/10, 15)
                else:
                    score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
                game_window.blit(score_surface, score_rect)

#---------------------------------------Strore Score In DataBase---------------------------------------------------------------
                try:
                    global p_snake_medium
                    if score>p_snake_medium:
                        show_details3_1.configure(text="High Score : "+str(score))
                        gamezone.update()
                        operation = "UPDATE player_details SET snake_medium=%s where username =%s"
                        data = (score,p_username)
                        cursor.execute(operation,data)
                        dbcon.commit()
                except:
                    messagebox.showerror("GameZone","Play This Game After Sign-In.")
                    pygame.quit()
    # pygame.display.flip()
# Main logic
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    #sys.exit()
        # Whenever a key is pressed down
                    elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
                        if event.key == pygame.K_UP or event.key == ord('w'):
                            change_to = 'UP'
                        if event.key == pygame.K_DOWN or event.key == ord('s'):
                            change_to = 'DOWN'
                        if event.key == pygame.K_LEFT or event.key == ord('a'):
                            change_to = 'LEFT'
                        if event.key == pygame.K_RIGHT or event.key == ord('d'):
                            change_to = 'RIGHT'
            # Esc -> Create event to quit the game
                        if event.key == pygame.K_ESCAPE:
                            pygame.event.post(pygame.event.Event(pygame.QUIT))
    # Making sure the snake cannot move in the opposite direction instantaneously
                if change_to == 'UP' and direction != 'DOWN':
                    direction = 'UP'
                if change_to == 'DOWN' and direction != 'UP':
                    direction = 'DOWN'
                if change_to == 'LEFT' and direction != 'RIGHT':
                    direction = 'LEFT'
                if change_to == 'RIGHT' and direction != 'LEFT':
                    direction = 'RIGHT'
    # Moving the snake
                if direction == 'UP':
                    snake_pos[1] -= 10
                if direction == 'DOWN':
                    snake_pos[1] += 10
                if direction == 'LEFT':
                    snake_pos[0] -= 10
                if direction == 'RIGHT':
                    snake_pos[0] += 10
    # Snake body growing mechanism                        Snake Bit
                snake_body.insert(0, list(snake_pos))
                if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
                    mixer.init()
                    mixer.music.load(r"C:\Users\rajpu\Desktop\GameZone\Music File\Snake Game\bite.mp3")
                    mixer.music.play()
                    score += 1
                    food_spawn = False
                else:
                    snake_body.pop()
    # Spawning food on the screen
                if not food_spawn:
                    food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
                food_spawn = True
    # GFX
                game_window.fill(black)
                for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
                    pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    # Snake food
                pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    # Game Over conditions
    # Getting out of bounds
                if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
                    game_over()
                if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
                    game_over()
    # Touching the snake body
                for block in snake_body[1:]:
                    if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                        game_over()
                show_score(1, white, 'consolas', 20)
    # Refresh game screen
                pygame.display.update()
    # Refresh rate
                fps_controller.tick(difficulty1)
        except:
            pass


#--------------------------------------------------Hard Level----------------------------------------------------------------
    def snakegamehardlevel():
        try:
        # Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
            difficulty2 = 40


# Checks for errors encountered
            check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
            if check_errors[1] > 0:
                print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
                sys.exit(-1)
            else:
                print('[+] Game successfully initialised')


# Initialise game window
            info = pygame.display.Info()
            frame_size_x = info.current_w  # Screen Width
            frame_size_y = info.current_h  # Screen Height
            game_window = pygame.display.set_mode((frame_size_x-50, frame_size_y-50), pygame.RESIZABLE)
            pygame.display.set_caption('Snake Eater')
            pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE, {"w": frame_size_x, "h": frame_size_y}))
            ctypes.windll.user32.ShowWindow(pygame.display.get_wm_info()["window"], 3)
            

# Colors (R, G, B)
            black = pygame.Color(0, 0, 0)
            white = pygame.Color(255, 255, 255)
            red = pygame.Color(255, 0, 0)
            green = pygame.Color(0, 255, 0)
            blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
            fps_controller = pygame.time.Clock()


# Game variables
            snake_pos = [100, 50]
            snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

            food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
            food_spawn = True

            direction = 'RIGHT'
            change_to = direction

            score = 0


# Game Over
            def game_over():
                mixer.init()
                mixer.music.load(r"C:\Users\rajpu\Desktop\GameZone\Music File\Snake Game\out.mp3")
                mixer.music.play()
                my_font = pygame.font.SysFont('times new roman', 60)
                game_over_surface = my_font.render('YOU DIED.....Play Again.!', True, red)
                game_over_rect = game_over_surface.get_rect()
                game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
                game_window.fill(black)
                game_window.blit(game_over_surface, game_over_rect)
                show_score(0, red, 'times', 20)
                pygame.display.flip()
                time.sleep(1.3)
                pygame.quit()
# Score
            def show_score(choice, color, font, size):
                score_font = pygame.font.SysFont(font, size)
                score_surface = score_font.render('Score : ' + str(score), True, color)
                score_rect = score_surface.get_rect()
                if choice == 1:
                    score_rect.midtop = (frame_size_x/10, 15)
                else:
                    score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
                game_window.blit(score_surface, score_rect)
            
#--------------------------------Store Score In DataBase------------------------------------------------------------
                try:
                    global p_snake_hard
                    if score>p_snake_hard:
                        show_details4_1.configure(text="High Score : "+str(score))
                        gamezone.update()
                        operation = "UPDATE player_details SET snake_hard=%s where username =%s"
                        data = (score,p_username)
                        cursor.execute(operation,data)
                        dbcon.commit()
                except:
                    messagebox.showerror("GameZone","Play This Game After Sigh-in.")
                    pygame.quit()
    # pygame.display.flip()
# Main logic
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    #sys.exit()
        # Whenever a key is pressed down
                    elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
                        if event.key == pygame.K_UP or event.key == ord('w'):
                            change_to = 'UP'
                        if event.key == pygame.K_DOWN or event.key == ord('s'):
                            change_to = 'DOWN'
                        if event.key == pygame.K_LEFT or event.key == ord('a'):
                            change_to = 'LEFT'
                        if event.key == pygame.K_RIGHT or event.key == ord('d'):
                            change_to = 'RIGHT'
            # Esc -> Create event to quit the game
                        if event.key == pygame.K_ESCAPE:
                            pygame.event.post(pygame.event.Event(pygame.QUIT))
    # Making sure the snake cannot move in the opposite direction instantaneously
                if change_to == 'UP' and direction != 'DOWN':
                    direction = 'UP'
                if change_to == 'DOWN' and direction != 'UP':
                    direction = 'DOWN'
                if change_to == 'LEFT' and direction != 'RIGHT':
                    direction = 'LEFT'
                if change_to == 'RIGHT' and direction != 'LEFT':
                    direction = 'RIGHT'
    # Moving the snake
                if direction == 'UP':
                    snake_pos[1] -= 10
                if direction == 'DOWN':
                    snake_pos[1] += 10
                if direction == 'LEFT':
                    snake_pos[0] -= 10
                if direction == 'RIGHT':
                    snake_pos[0] += 10
    # Snake body growing mechanism
                snake_body.insert(0, list(snake_pos))
                if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
                    mixer.init()
                    mixer.music.load(r"C:\Users\rajpu\Desktop\GameZone\Music File\Snake Game\bite.mp3")
                    mixer.music.play()
                    score += 1
                    food_spawn = False
                else:
                    snake_body.pop()
    # Spawning food on the screen
                if not food_spawn:
                    food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
                food_spawn = True
    # GFX
                game_window.fill(black)
                for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
                    pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    # Snake food
                pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    # Game Over conditions
    # Getting out of bounds
                if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
                    game_over()
                if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
                    game_over()
    # Touching the snake body
                for block in snake_body[1:]:
                    if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                        game_over()
                show_score(1, white, 'consolas', 20)
    # Refresh game screen
                pygame.display.update()
    # Refresh rate
                fps_controller.tick(difficulty2)
        except:
            pass
#-----------------------------------------------------------------------------------------------------------------    
    displaylabel = Label(snakewindow,text="Welcome To Snake Game",font=("times new roman",18,"bold")).place(x=250,y=20)
    snakelabel1 = Label(snakewindow,text="Choose The Level:-",font=("times new roman",18,"bold")).place(x=50,y=80)
    snakelabel2 = Label(snakewindow,text="Easy",font=("times new roman",18,"bold")).place(x=180,y=145)
    snakebutton1 = Button(snakewindow,text="Start",font=("times new roman",18,"bold"),bg="yellow",fg="red",height=1,width=15,command=snakegameeasylevel).place(x=300,y=138)
    snakelabel3 = Label(snakewindow,text="Medium",font=("times new roman",18,"bold")).place(x=180,y=224)
    snakebutton2 = Button(snakewindow,text="Start",font=("times new roman",18,"bold"),bg="yellow",fg="red",height=1,width=15,command=snakegamemediumlevel).place(x=300,y=218)
    snakelabel4 = Label(snakewindow,text="Hard",font=("times new roman",18,"bold")).place(x=180,y=300)
    snakebutton3 = Button(snakewindow,text="Start",font=("times new roman",18,"bold"),bg="yellow",fg="red",height=1,width=15,command=snakegamehardlevel).place(x=300,y=298)

      
    snakewindow.mainloop()

#--------------------------------------------------
snakegame = Frame(gamezone)
img=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\snake-game.jpeg")
resizeimg = img.resize((606, 200), Image.LANCZOS)
ph=ImageTk.PhotoImage(resizeimg)

snakegameimg = Label(snakegame,image=ph,height=198,width=606, bg="red").grid(row=0,column=0)
btn = Button(snakegame,text="Start",height=1,width=40,font=("times new roman",15,"bold"),bg="yellow",fg="red",activebackground="skyblue",command=defsnakegame).grid(row=1,column=0)

snakegame.place(x=100,y=70)

#----------------------------------------------------   Pong  -------------------------------------------------------------------
def startponggame():
    import pygame
    import random
    from math import cos
    from math import radians
    from math import sin
    try:

        pygame.init()

        width = 600
        height = 400
        display = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pong!")
        clock = pygame.time.Clock()

        background = (27, 38, 49)
        white = (236, 240, 241)
        red = (203, 67, 53)
        blue = (52, 152, 219)
        yellow = (244, 208, 63)

        top = white
        bottom = white
        left = white
        right = white

        margin = 4

        global scoreLeft
        scoreLeft = 0
        global scoreRight
        scoreRight = 0
        maxScore = 10

        font = pygame.font.SysFont("Small Fonts", 30)
        largeFont = pygame.font.SysFont("Small Fonts", 60)

    # Draw the Boundary of Board
        def boundary():
            pygame.draw.rect(display, left, (0, 0, margin, height))
            pygame.draw.rect(display, top, (0, 0, width, margin))
            pygame.draw.rect(display, right, (width-margin, 0, margin, height))
            pygame.draw.rect(display, bottom, (0, height - margin, width, margin))

            l = 25
    
            pygame.draw.rect(display, white, (width/2-margin/2, 10, margin, l))
            pygame.draw.rect(display, white, (width/2-margin/2, 60, margin, l))
            pygame.draw.rect(display, white, (width/2-margin/2, 110, margin, l))
            pygame.draw.rect(display, white, (width/2-margin/2, 160, margin, l))
            pygame.draw.rect(display, white, (width/2-margin/2, 210, margin, l))
            pygame.draw.rect(display, white, (width/2-margin/2, 260, margin, l))
            pygame.draw.rect(display, white, (width/2-margin/2, 310, margin, l))
            pygame.draw.rect(display, white, (width/2-margin/2, 360, margin, l))
    
    # Paddle Class 
        class Paddle:
            def __init__(self, position):
                self.w = 10
                self.h = self.w*8
                self.paddleSpeed = 6
            
                if position == -1:
                    self.x = 1.5*margin
                else:
                    self.x = width - 1.5*margin - self.w
            
                self.y = height/2 - self.h/2

        # Show the Paddle
            def show(self):
                pygame.draw.rect(display, white, (self.x, self.y, self.w, self.h))

        # Move the Paddle
            def move(self, ydir):
                self.y += self.paddleSpeed*ydir
                if self.y < 0:
                    self.y -= self.paddleSpeed*ydir
                elif self.y + self.h> height:
                    self.y -= self.paddleSpeed*ydir


        leftPaddle = Paddle(-1)
        rightPaddle = Paddle(1)

    # Ball Class
        class Ball:
            def __init__(self, color):
                self.r = 20
                self.x = width/2 - self.r/2
                self.y = height/2 -self.r/2
                self.color = color
                self.angle = random.randint(-75, 75)
                if random.randint(0, 1):
                    self.angle += 180
        
                self.speed = 8

        # Show the Ball
            def show(self):
                pygame.draw.ellipse(display, self.color, (self.x, self.y, self.r, self.r))

        # Move the Ball
            def move(self):
                global scoreLeft
                global scoreRight
                self.x += self.speed*cos(radians(self.angle))
                self.y += self.speed*sin(radians(self.angle))
                if self.x + self.r > width - margin:
                    scoreLeft += 1
                    self.angle = 180 - self.angle
                if self.x < margin:
                    scoreRight += 1
                    self.angle = 180 - self.angle
                if self.y < margin:
                    self.angle = - self.angle
                if self.y + self.r  >=height - margin:
                    self.angle = - self.angle

        # Check and Reflect the Ball when it hits the padddle
            def checkForPaddle(self):
                if self.x < width/2:
                    if leftPaddle.x < self.x < leftPaddle.x + leftPaddle.w:
                        if leftPaddle.y < self.y < leftPaddle.y + 10 or leftPaddle.y < self.y + self.r< leftPaddle.y + 10:
                            self.angle = -45
                        if leftPaddle.y + 10 < self.y < leftPaddle.y + 20 or leftPaddle.y + 10 < self.y + self.r< leftPaddle.y + 20:
                            self.angle = -30
                        if leftPaddle.y + 20 < self.y < leftPaddle.y + 30 or leftPaddle.y + 20 < self.y + self.r< leftPaddle.y + 30:
                            self.angle = -15
                        if leftPaddle.y + 30 < self.y < leftPaddle.y + 40 or leftPaddle.y + 30 < self.y + self.r< leftPaddle.y + 40:
                            self.angle = -10
                        if leftPaddle.y + 40 < self.y < leftPaddle.y + 50 or leftPaddle.y + 40 < self.y + self.r< leftPaddle.y + 50:
                            self.angle = 10
                        if leftPaddle.y + 50 < self.y < leftPaddle.y + 60 or leftPaddle.y + 50 < self.y + self.r< leftPaddle.y + 60:
                            self.angle = 15
                        if leftPaddle.y + 60 < self.y < leftPaddle.y + 70 or leftPaddle.y + 60 < self.y + self.r< leftPaddle.y + 70:
                            self.angle = 30
                        if leftPaddle.y + 70 < self.y < leftPaddle.y + 80 or leftPaddle.y + 70 < self.y + self.r< leftPaddle.y + 80:
                            self.angle = 45
                else:
                    if rightPaddle.x + rightPaddle.w > self.x  + self.r > rightPaddle.x:
                        if rightPaddle.y < self.y < leftPaddle.y + 10 or leftPaddle.y < self.y + self.r< leftPaddle.y + 10:
                            self.angle = -135
                        if rightPaddle.y + 10 < self.y < rightPaddle.y + 20 or rightPaddle.y + 10 < self.y + self.r< rightPaddle.y + 20:
                            self.angle = -150
                        if rightPaddle.y + 20 < self.y < rightPaddle.y + 30 or rightPaddle.y + 20 < self.y + self.r< rightPaddle.y + 30:
                            self.angle = -165
                        if rightPaddle.y + 30 < self.y < rightPaddle.y + 40 or rightPaddle.y + 30 < self.y + self.r< rightPaddle.y + 40:
                            self.angle = 170
                        if rightPaddle.y + 40 < self.y < rightPaddle.y + 50 or rightPaddle.y + 40 < self.y + self.r< rightPaddle.y + 50:
                            self.angle = 190
                        if rightPaddle.y + 50 < self.y < rightPaddle.y + 60 or rightPaddle.y + 50 < self.y + self.r< rightPaddle.y + 60:
                            self.angle = 165
                        if rightPaddle.y + 60 < self.y < rightPaddle.y + 70 or rightPaddle.y + 60 < self.y + self.r< rightPaddle.y + 70:
                            self.angle = 150
                        if rightPaddle.y + 70 < self.y < rightPaddle.y + 80 or rightPaddle.y + 70 < self.y + self.r< rightPaddle.y + 80:
                            self.angle = 135

    # Show the Score
        def showScore():
            leftScoreText = font.render("Score : " + str(scoreLeft), True, red)
            rightScoreText = font.render("Score : " + str(scoreRight), True, blue)

            display.blit(leftScoreText, (3*margin, 3*margin))
            display.blit(rightScoreText, (width/2 + 3*margin, 3*margin))

    # Game Over
        def gameOver():
            if scoreLeft == maxScore or scoreRight == maxScore:
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                pygame.quit()
                            if event.key == pygame.K_r:
                                reset()
                    if scoreLeft == maxScore:
                        playerWins = largeFont.render("Left Player Wins!", True, red)
                    elif scoreRight == maxScore:
                        playerWins = largeFont.render("Right Player Wins!", True, blue)

                    display.blit(playerWins, (width/2 - 100, height/2))
                    pygame.display.update()

        def reset():
            global scoreLeft, scoreRight
            scoreLeft = 0
            scoreRight = 0
            board()


        def close():
            pygame.quit()
        #sys.exit()

        def board():
            loop = True
            leftChange = 0
            rightChange = 0
            ball = Ball(yellow)
    
            while loop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        close()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            close()
                        if event.key == pygame.K_r:
                            reset()
                        if event.key == pygame.K_w:
                            leftChange = -1
                        if event.key == pygame.K_s:
                            leftChange = 1
                        if event.key == pygame.K_UP:
                            rightChange = -1
                        if event.key == pygame.K_DOWN:
                            rightChange = 1
                    if event.type == pygame.KEYUP:
                        leftChange = 0
                        rightChange = 0

                leftPaddle.move(leftChange)
                rightPaddle.move(rightChange)
                ball.move()
                ball.checkForPaddle() 
        
                display.fill(background)
                showScore()

                ball.show()
                leftPaddle.show()
                rightPaddle.show()

                boundary()

                gameOver()
        
                pygame.display.update()
                clock.tick(60)

        board()
    except:
        pass
    
#--------------------------------------------------
ponggame = Frame(gamezone)
img1=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\pong.jpg")
resizeimg1 = img1.resize((606, 200), Image.LANCZOS)
ph1=ImageTk.PhotoImage(resizeimg1)

ponggameimg = Label(ponggame,image=ph1,height=198,width=606, bg="red").grid(row=0,column=0)
btn1 = Button(ponggame,text="Start",height=1,width=40,font=("times new roman",15,"bold"),bg="yellow",fg="red",activebackground="skyblue",command=startponggame).grid(row=1,column=0)

ponggame.place(x=800,y=70)

#---------------------------------------------------  Car Racing ---------------------------------------------------------------
def startcarracinggame():
    import pygame, random, sys, os, time

    try:
        WINDOWWIDTH = 800
        WINDOWHEIGHT = 600
        TEXTCOLOR = (255, 255, 255)
        BACKGROUNDCOLOR = (0, 0, 0)
        FPS = 40
        BADDIEMINSIZE = 10
        BADDIEMAXSIZE = 40
        BADDIEMINSPEED = 8
        BADDIEMAXSPEED = 8
        ADDNEWBADDIERATE = 6
        PLAYERMOVERATE = 5
        count = 3
        topScore=0

        def terminate():
            pygame.quit()
        #sys.exit()

        def waitForPlayerToPressKey():
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        terminate()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:  # escape quits
                            terminate()
                        return

        def playerHasHitBaddie(playerRect, baddies):
            for b in baddies:
                if playerRect.colliderect(b['rect']):
                    return True
            return False

        def drawText(text, font, surface, x, y):
            textobj = font.render(text, 1, TEXTCOLOR)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)


        pygame.init()
        mainClock = pygame.time.Clock()
        windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('Car Race')
        pygame.mouse.set_visible(False)

        playerImage = pygame.image.load(r"C:\Users\rajpu\Desktop\GameZone\Image\Car_game_2\car1.png")
        car3 = pygame.image.load(r"C:\Users\rajpu\Desktop\GameZone\Image\Car_game_2\car3.png")
        car4 = pygame.image.load(r"C:\Users\rajpu\Desktop\GameZone\Image\Car_game_2\car4.png")
        playerRect = playerImage.get_rect()
        baddieImage = pygame.image.load(r"C:\Users\rajpu\Desktop\GameZone\Image\Car_game_2\car2.png")
        sample = [car3, car4, baddieImage]
        wallLeft = pygame.image.load(r"C:\Users\rajpu\Desktop\GameZone\Image\Car_game_2\left.png")
        wallRight = pygame.image.load(r"C:\Users\rajpu\Desktop\GameZone\Image\Car_game_2\right.png")

        font = pygame.font.SysFont(None, 42)
        drawText('PRESS ANY KEY TO START THE GAME!', font, windowSurface, (WINDOWWIDTH / 3) - 137, (WINDOWHEIGHT / 3)+80)
        pygame.display.update()
        waitForPlayerToPressKey()
        zero = 0

        while (count > 0):
            baddies = []
            score = 0
            playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
            moveLeft = moveRight = moveUp = moveDown = False
            reverseCheat = slowCheat = False
            baddieAddCounter = 0

            while True:
                score += 1

                for event in pygame.event.get():

                    if event.type == QUIT:
                        terminate()

                    if event.type == KEYDOWN:
                        if event.key == ord('z'):
                            reverseCheat = True
                        if event.key == ord('x'):
                            slowCheat = True
                        if event.key == K_LEFT or event.key == ord('a'):
                            moveRight = False
                            moveLeft = True
                        if event.key == K_RIGHT or event.key == ord('d'):
                            moveLeft = False
                            moveRight = True
                        if event.key == K_UP or event.key == ord('w'):
                            moveDown = False
                            moveUp = True
                        if event.key == K_DOWN or event.key == ord('s'):
                            moveUp = False
                            moveDown = True

                    if event.type == KEYUP:
                        if event.key == ord('z'):
                            reverseCheat = False
                            score = 0
                        if event.key == ord('x'):
                            slowCheat = False
                            score = 0
                        if event.key == K_ESCAPE:
                            terminate()

                        if event.key == K_LEFT or event.key == ord('a'):
                            moveLeft = False
                        if event.key == K_RIGHT or event.key == ord('d'):
                            moveRight = False
                        if event.key == K_UP or event.key == ord('w'):
                            moveUp = False
                        if event.key == K_DOWN or event.key == ord('s'):
                            moveDown = False

                if not reverseCheat and not slowCheat:
                    baddieAddCounter += 1
                if baddieAddCounter == ADDNEWBADDIERATE:
                    baddieAddCounter = 0
                    baddieSize = 30
                    newBaddie = {'rect': pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                            'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                            'surface': pygame.transform.scale(random.choice(sample), (23, 47)),
                        }
                    baddies.append(newBaddie)
                    sideLeft = {'rect': pygame.Rect(0, 0, 126, 600),
                            'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                            'surface': pygame.transform.scale(wallLeft, (126, 599)),
                        }
                    baddies.append(sideLeft)
                    sideRight = {'rect': pygame.Rect(497, 0, 303, 600),
                            'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                            'surface': pygame.transform.scale(wallRight, (303, 599)),
                        }
                    baddies.append(sideRight)

                if moveLeft and playerRect.left > 0:
                    playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
                if moveRight and playerRect.right < WINDOWWIDTH:
                    playerRect.move_ip(PLAYERMOVERATE, 0)
                if moveUp and playerRect.top > 0:
                    playerRect.move_ip(0, -1 * PLAYERMOVERATE)
                if moveDown and playerRect.bottom < WINDOWHEIGHT:
                    playerRect.move_ip(0, PLAYERMOVERATE)

                for b in baddies:
                    if not reverseCheat and not slowCheat:
                        b['rect'].move_ip(0, b['speed'])
                    elif reverseCheat:
                        b['rect'].move_ip(0, -5)
                    elif slowCheat:
                        b['rect'].move_ip(0, 1)

                for b in baddies[:]:
                    if b['rect'].top > WINDOWHEIGHT:
                        baddies.remove(b)

                font = pygame.font.SysFont(None, 38)
                windowSurface.fill(BACKGROUNDCOLOR)
                drawText('Score: %s' % (score), font, windowSurface, 128, 0)
                drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 21)
                drawText('Rest Life: %s' % (count), font, windowSurface, 128, 41)

                windowSurface.blit(playerImage, playerRect)

                for b in baddies:
                    windowSurface.blit(b['surface'], b['rect'])

                pygame.display.update()

                if playerHasHitBaddie(playerRect, baddies):
                    if score > topScore:
                        topScore = score
                    break
            
#--------------------------------Store Score In DataBase------------------------------------------------------------
                try:
                    global p_car
                    if topScore>p_car:
                        show_details5_1.configure(text="High Score : "+str(topScore))
                        gamezone.update()
                        operation = "UPDATE player_details SET car=%s where username =%s"
                        data = (topScore,p_username)
                        cursor.execute(operation,data)
                        dbcon.commit()
                except:
                    messagebox.showerror("GameZone","Play This Game After Sihn-In.")
                    pygame.quit()

                mainClock.tick(FPS)

            count = count - 1
            time.sleep(1)
            font = pygame.font.SysFont(None, 52)
            if (count == 0):

                drawText('Game Over', font, windowSurface, (WINDOWWIDTH / 3)+40, (WINDOWHEIGHT / 3)+70)
                drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH /3) - 110, (WINDOWHEIGHT / 3) + 95)
                pygame.display.update()
                time.sleep(2)
                waitForPlayerToPressKey()
                count = 3
    except:
        pass

#-----------------------------------------------
thirdrdgame = Frame(gamezone)
img2=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\car_racing.jpg")
resizeimg2 = img2.resize((606, 200), Image.LANCZOS)
ph2=ImageTk.PhotoImage(resizeimg2)

thirdrdgameimg = Label(thirdrdgame,image=ph2,height=198,width=606, bg="red").grid(row=0,column=0)
btn2 = Button(thirdrdgame,text="Start",height=1,width=40,font=("times new roman",15,"bold"),bg="yellow",fg="red",activebackground="skyblue",command=startcarracinggame).grid(row=1,column=0)

thirdrdgame.place(x=100,y=350)

#-----------------------------------------------------Dodge The Ball---------------------------------------------------------
def startdadgethaball():
    import pygame
    import random
    from math import cos
    from math import sin
    from math import radians
    
    try:
        pygame.init()

        width = 800
        height = 600
        display = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Dodge The Ball!")
        clock = pygame.time.Clock()

        background = (51, 51, 51)
        playerColor = (249, 231, 159)

        red = (203, 67, 53)
        yellow = (241, 196, 15)
        blue = (46, 134, 193)
        green = (34, 153, 84)
        purple = (136, 78, 160)
        orange = (214, 137, 16)

        colors = [red, yellow, blue, green, purple, orange]
    
        global score
        score = 0


        class Ball:
            def __init__(self, radius, speed):
                self.x = 0
                self.y = 0
                self.r = radius
                self.color = 0
                self.speed = speed
                self.angle = 0
    
            def createBall(self):
                self.x = width/2 - self.r
                self.y = height/2 - self.r
                self.color = random.choice(colors)
                self.angle = random.randint(-180, 180)
    
            def move(self):
                self.x += self.speed*cos(radians(self.angle))
                self.y += self.speed*sin(radians(self.angle))

                if self.x < self.r or self.x + self.r > width:
                    self.angle = 180 - self.angle
                if self.y < self.r or self.y + self.r > height:
                    self.angle *= -1

            def draw(self):
                pygame.draw.ellipse(display, self.color, (self.x - self.r, self.y - self.r, self.r*2, self.r*2))

            def collision(self, radius):
                pos = pygame.mouse.get_pos()

                dist = ((pos[0] - self.x)**2 + (pos[1] - self.y)**2)**0.5

                if dist <= self.r + radius:
                    gameOver()

        class Target:
            def __init__(self):
                self.x = 0
                self.y = 0
                self.w = 20
                self.h = self.w

            def generateNewCoord(self):
                self.x = random.randint(self.w, width - self.w)
                self.y = random.randint(self.h, height - self.h)

            def draw(self):
                color = random.choice(colors)

                pygame.draw.rect(display, color, (self.x, self.y, self.w, self.h))

    
        def gameOver():
            loop = True

            font = pygame.font.SysFont("Agency FB", 55)
            text = font.render("Game Over....."+"Press R To Restart The Game.!", True, (230, 230, 230))
    
    
            while loop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                        if event.key == pygame.K_r:
                            gameLoop()

                display.fill(background)

                display.blit(text, (20, height/2 - 100))
                displayScore()
        
                pygame.display.update()
                clock.tick()


        def checkCollision(target, d, objTarget):
            pos = pygame.mouse.get_pos()
            dist = ((pos[0] - target[0] - objTarget.w)**2 + (pos[1] - target[1]  - objTarget.h)**2)**0.5

            if dist <= d + objTarget.w:
                return True
            return False


        def drawPlayerPointer(pos, r):
            pygame.draw.ellipse(display, playerColor, (pos[0] - r, pos[1] - r, 2*r, 2*r))


        def close():
            pygame.quit()

        def displayScore():
            font = pygame.font.SysFont("Forte", 30)
            scoreText = font.render("Score: " + str(score), True, (230, 230, 230))
            display.blit(scoreText, (10, 10))
        
#--------------------------------Store Score In DataBase------------------------------------------------------------
            try:    
                global p_daudge_ball
                if score>p_daudge_ball:
                    show_details6_1.configure(text="High Score : "+str(score))
                    gamezone.update()
                    operation = "UPDATE player_details SET dodge_ball=%s where username =%s"
                    data = (score,p_username)
                    cursor.execute(operation,data)
                    dbcon.commit()
            except:
                messagebox.showerror("GameZone","Play This After Sign-In.")
                pygame.quit()

        def gameLoop():
            global score
            score = 0
    
            loop = True

            pRadius = 10

            balls = []

            for i in range(1):
                newBall = Ball(pRadius + 2, 5)
                newBall.createBall()
                balls.append(newBall)

            target = Target()
            target.generateNewCoord()
    
            while loop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                        if event.key == pygame.K_r:
                            gameLoop()

                display.fill(background)

                for i in range(len(balls)):
                    balls[i].move()
            
                for i in range(len(balls)):
                    balls[i].draw()
            
                for i in range(len(balls)):
                    balls[i].collision(pRadius)

                playerPos = pygame.mouse.get_pos()
                drawPlayerPointer((playerPos[0], playerPos[1]), pRadius)

                collide = checkCollision((target.x, target.y), pRadius, target)
        
                if collide:
                    score += 1
                    target.generateNewCoord()
                elif score == 2 and len(balls) == 1:
                    newBall = Ball(pRadius + 2, 5)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 5 and len(balls) == 2:
                    newBall = Ball(pRadius + 2, 6)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 10 and len(balls) == 3: 
                    clock.tick(30)
                    newBall = Ball(pRadius + 2, 7)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 15 and len(balls) == 4:
                    newBall = Ball(pRadius + 2, 8)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 20 and len(balls) == 5:
                    newBall = Ball(pRadius + 2, 9)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 25 and len(balls) == 6:
                    newBall = Ball(pRadius + 2, 10)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 30 and len(balls) == 7:
                    newBall = Ball(pRadius + 2, 11)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 35 and len(balls) == 8:
                    newBall = Ball(pRadius + 2, 12)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 40 and len(balls) == 9:
                    newBall = Ball(pRadius + 2, 13)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 45 and len(balls) == 10:
                    newBall = Ball(pRadius + 2, 14)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 50 and len(balls) == 11:
                    newBall = Ball(pRadius + 2, 15)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 55 and len(balls) == 12:
                    newBall = Ball(pRadius + 2, 16)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 60 and len(balls) == 13:
                    newBall = Ball(pRadius + 2, 17)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 65 and len(balls) == 14:
                    newBall = Ball(pRadius + 2, 18)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 70 and len(balls) == 15:
                    newBall = Ball(pRadius + 2, 19)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 75 and len(balls) == 16:
                    newBall = Ball(pRadius + 2, 20)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 80 and len(balls) == 17:
                    newBall = Ball(pRadius + 2, 21)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 85 and len(balls) == 18:
                    newBall = Ball(pRadius + 2, 22)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 90 and len(balls) == 19:
                    newBall = Ball(pRadius + 2, 23)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 95 and len(balls) == 20:
                    newBall = Ball(pRadius + 2, 24)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()
                elif score == 100 and len(balls) == 21:
                    newBall = Ball(pRadius + 2, 25)
                    newBall.createBall()
                    balls.append(newBall)
                    target.generateNewCoord()

                target.draw()
                displayScore()
        
                pygame.display.update()
                clock.tick(20)

        gameLoop()
    
    except:
        pass

#----------------------------------------------------------
fourthgame = Frame(gamezone)
img3=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\dodge_the_ball.jpg")
resizeimg3 = img3.resize((606, 200), Image.LANCZOS)
ph3=ImageTk.PhotoImage(resizeimg3)
fourthgameimg = Label(fourthgame,image=ph3,height=198,width=606, bg="red").grid(row=0,column=0)
btn1 = Button(fourthgame,text="Start",height=1,width=40,font=("times new roman",15,"bold"),bg="yellow",fg="red",activebackground="skyblue",command=startdadgethaball)
btn1.grid(row=1,column=0)

fourthgame.place(x=800,y=350)

#---------------------------------------------------Closing Function-----------------------------------------------------
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #exit()
        sys.exit()
    else:
        sign_in.withdraw()
        pregister.withdraw()
        gamezone.deiconify()
gamezone.protocol("WM_DELETE_WINDOW", on_closing)
#-------------------------------------------------Sign-In/PRegister Function------------------------------------------------------
def sign_in():
    signin.deiconify()

def forger_password():
    signin.withdraw()
    def emial_verify():
        checkemail2 = str(e1.get())
        
        try:
            operation = "SELECT *FROM player_details where username ='%s'"%(checkemail2)
            cursor.execute(operation)
            results = cursor.fetchall()
            for rec in results:
                p_username = rec[0]
                p_email = rec[2]
            if p_username == checkemail2: 
                global generate_OTP
                corpus= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                generate_OTP = "" 
                size=6
                length = len(corpus) 
                for i in range(size) : 
                    generate_OTP+= corpus[math.floor(random.random() * length)] 
                print(generate_OTP)
                
            gmail_user = ''
            gmail_password = ''
            to_test = p_email
            sent_from = gmail_user
            to = [to_test]
            subject = 'GameZone'
            a = p_username
            body = 'your OTP has: '+generate_OTP
            email_text = """
            From : %s
            To : %s
            Subject : %s


            your username : %s
        
        
        
            %s
            """ % (sent_from, ", ".join(to), subject,a, body)
        
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
            messagebox.showinfo("GameZone","check your gmail for OTP.")   
            forget_win.deiconify()   
            fbtn_forget_win.place_forget()
            bbtn_forget_win.place_forget()  
            verify_otp_entry = StringVar()
            e1.config(state=DISABLED)
            lbl2 = Label(forget_win,text="Enter Your OTP :",font=("times new roman",15,"bold"),bg="lightblue",fg="red").place(x=10,y=110)
            e2 = Entry(forget_win,font=("times new roman",15,"bold"),textvariable=verify_otp_entry,bd=6, insertwidth=4, bg='ghostwhite', justify='right')
            e2.place(x=260,y=110)
                    
            def forget_password():
                def back2():
                    forget_win2.withdraw()
                    forget_win.deiconify()
                forget_win.withdraw()
                forget_win2 = Toplevel()
                forget_win2.config(bg="lightblue")
                forget_win2.iconbitmap(r"C:\Users\rajpu\Desktop\GameZone\Image\gameicon.ico")
                forget_win2.geometry("615x260+580+270")
                forget_win2.resizable(False, False)
                lbl = Label(forget_win2,text="Forger Password",font=("times new roman",15,"bold"),bg="lightblue",fg="red").place(x=200,y=30)
                password1 = StringVar()
                password2 = StringVar()
                lbl2 = Label(forget_win2,text="Enter New Password :",font=("times new roman",15,"bold"),bg="lightblue",fg="red").place(x=75,y=90)
                e2 = Entry(forget_win2,font=("times new roman",15,"bold"),textvariable=password1,bd=6, insertwidth=4, bg='ghostwhite', justify='right')
                e2.place(x=325,y=90)
                lbl3 = Label(forget_win2,text="Enter Confirmed Password :",font=("times new roman",15,"bold"),bg="lightblue",fg="red").place(x=10,y=140)
                e3 = Entry(forget_win2,font=("times new roman",15,"bold"),textvariable=password2,bd=6, insertwidth=4, bg='ghostwhite', justify='right')
                e3.place(x=325,y=140)
                def forget():
                    passw1 = str(password1.get())
                    passw2 = str(password2.get())
                    data = [passw1]    
                    for i in data:
                        if (i != passw2):
                            messagebox.showerror("GameZone","please enter new password same as well as confirmed password.")
                            forget_win2.deiconify()
                            return
                        elif (i == passw1):
                            if (len(i) != 6):
                                messagebox.showerror("GameZone", "Please enter 6 digits of password.")
                                forget_win2.deiconify()
                                return
                        
                    operation = "UPDATE player_details SET password=%s where email=%s"
                    data = (passw2,p_email)
                    cursor.execute(operation,data)
                    dbcon.commit()
                    messagebox.showinfo("GameZone","Your Password Has Successfully Updated.")
                    forget_win2.destroy()
                    gmail_user = ''
                    gmail_password = ''
                    to_test = p_email
                    sent_from = gmail_user
                    to = [to_test]
                    subject = 'GameZone'
                    a = p_username
                    body = "your password has been successfully changed."+"\n"+"your new password :"+str(passw1)
                    email_text = """
                    From : %s
                    To : %s
                    Subject : %s


                    your username : %s
        
        
        
                    %s
                    """ % (sent_from, ", ".join(to), subject,a,body)
        
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(gmail_user, gmail_password)
                    server.sendmail(sent_from, to, email_text)
                    server.close()
                    
                    
                    
                fbtn = Button(forget_win2,text="Forget Password",font=("times new roman",15,"bold"),bd=4,bg="yellow",fg="red",command=forget).place(x=390,y=195)
             
            def verify_otp():       
                if str(verify_otp_entry.get()) == str(generate_OTP):
                    forget_password()
                else:
                    messagebox.showerror("GameZone","please enter correct OTP.")
                    forget_win.deiconify()
                    print(generate_OTP)
            
                    
            checkotp = Button(forget_win,text="Submit",font=("times new roman",15,"bold"),bd=4,bg="yellow",fg="red",command=verify_otp).place(x=428,y=160)
                
        except:
            messagebox.showerror("GameZone","Please enter correct username.")
            forget_win.deiconify()
            return
        
    def back():
        forget_win.withdraw()
        signin.deiconify()
    
    checkemail = StringVar()

    forget_win = Toplevel()
    forget_win.config(bg="lightblue")
    forget_win.iconbitmap(r"C:\Users\rajpu\Desktop\GameZone\Image\gameicon.ico")
    forget_win.title("GameZone")
    forget_win.geometry("550x220+650+300")
    forget_win.resizable(False, False)

    lbl = Label(forget_win,text="Forger Password",font=("times new roman",15,"bold"),bg="lightblue",fg="red").place(x=150,y=10)
    lbl1 = Label(forget_win,text="Enter your username :",font=("times new roman",15,"bold"),bg="lightblue",fg="red").place(x=10,y=60)
    e1 = Entry(forget_win,font=("times new roman",15,"bold"),textvariable=checkemail,bd=6, insertwidth=4, bg='ghostwhite', justify='right')
    e1.place(x=260,y=60)
    fbtn_forget_win = Button(forget_win,text="Send",font=("times new roman",15,"bold"),bd=4,bg="yellow",fg="red",command=emial_verify)
    fbtn_forget_win.place(x=370,y=130)
    bbtn_forget_win = Button(forget_win,text="Back",font=("times new roman",15,"bold"),bd=4,bg="yellow",fg="red",command=back)
    bbtn_forget_win.place(x=455,y=130)

      
#-----------------------------------------------------Sign-In Screen--------------------------------------------------
signin = Toplevel()
signin.iconbitmap(r"C:\Users\rajpu\Desktop\GameZone\Image\gameicon.ico")
signin.title("GameZone")
signin.geometry("470x240+700+290")
signin.resizable(False, False)

pname = StringVar()
ppass = StringVar()

lbl = Label(signin,text="SIGN-IN",font=("times new roman",15,"bold"),bg="lightblue",fg="red").place(x=150,y=10)
lbl1 = Label(signin,text="USERNAME :",font=("times new roman",15,"bold"),bg="lightblue",fg="red").place(x=10,y=60)
e1 = Entry(signin,font=("times new roman",15,"bold"),textvariable=pname,bd=6, insertwidth=4, bg='ghostwhite', justify='right').place(x=180,y=60)
lbl2 = Label(signin,text="PASSWORD :",font=("times new roman",15,"bold"),bg="lightblue",fg="red").place(x=10,y=105)
e2 = Entry(signin,font=("times new roman",15,"bold"),textvariable=ppass,bd=6, insertwidth=4, bg='ghostwhite', justify='right').place(x=180,y=105)
sbtn = Button(signin,text="Sign-In",font=("times new roman",15,"bold"),bd=4,bg="yellow",fg="red",command=psignin).place(x=8,y=160)
rbtn = Button(signin,text="Register",font=("times new roman",15,"bold"),bd=4,bg="yellow",fg="red",command=player_register).place(x=345,y=160)
forget = Button(signin,text="Forget Password",font=("times new roman",12,"bold"), width=17,bd=4,bg="yellow",fg="red",command=forger_password).place(x=120,y=167)
signin.config(bg="lightblue")
# signin.geometry("380x250+480+170")
signin.withdraw()
#----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Player Register Screen--------------------------------------------------------
pregister = Toplevel()
pregister.iconbitmap(r"C:\Users\rajpu\Desktop\GameZone\Image\gameicon.ico")
pregister.title("GameZone")
pregister.geometry("480x380+700+220")
pregister.resizable(False, False)

e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
plbl = Label(pregister,text="REGISTRATION",font=("times new roman",15,"bold"),bg="ghostwhite",fg="red").place(x=130,y=10)
plbl1 = Label(pregister,text="USERNAME :",font=("times new roman",15,"bold"),bg="ghostwhite",fg="red").place(x=10,y=60)
pe1 = Entry(pregister,textvariable=e1,font=("times new roman",15,"bold"),bd=6, insertwidth=4, bg='skyblue', justify='right').place(x=180,y=60)
plbl2 = Label(pregister,text="PASSWORD :",font=("times new roman",15,"bold"),bg="ghostwhite",fg="red").place(x=10,y=110)
pe2 = Entry(pregister,textvariable=e2,font=("times new roman",15,"bold"),bd=6, insertwidth=4, bg='skyblue', justify='right').place(x=180,y=110)
plbl3 = Label(pregister,text="Email :",font=("times new roman",15,"bold"),bg="ghostwhite",fg="red").place(x=10,y=160)
pe3 = Entry(pregister,textvariable=e3,font=("times new roman",15,"bold"),bd=6, insertwidth=4, bg='skyblue', justify='right').place(x=180,y=160)
plbl4 = Label(pregister,text="Phone Num. :",font=("times new roman",15,"bold"),bg="ghostwhite",fg="red").place(x=10,y=210)
pe4 = Entry(pregister,textvariable=e4,font=("times new roman",15,"bold"),bd=6, insertwidth=4, bg='skyblue', justify='right').place(x=180,y=210)
plbl5 = Label(pregister,text="Age :",font=("times new roman",15,"bold"),bg="ghostwhite",fg="red").place(x=10,y=260)
pe5 = Entry(pregister,textvariable=e5,font=("times new roman",15,"bold"),bd=6, insertwidth=4, bg='skyblue', justify='right').place(x=180,y=260)

def register_data():
    username = str(e1.get())
    password = str(e2.get())
    email = str(e3.get())
    number = str(e4.get())
    age = str(e5.get())
    
    operation = "SELECT *FROM player_details where username ='%s'"%(username)
    cursor.execute(operation)
    results = cursor.fetchall()
    for rec in results:
        p_email_verify = rec[2]
    
    data = [username, password, email,number,age]    
    for i in data:
        if (i == username):
            if (len(i) == 0):
                messagebox.showerror("GameZone", "Please enter Username.")
                return
        elif (i == password):
            if (len(i) != 6):
                messagebox.showerror("GameZone", "Please enter 6 digits of password.")
                return
        elif ( i == email):
            if (len(i) == 0):
                messagebox.showerror("GameZone","Please enter Email Address.")
                return
        elif(i == email):
            for p_email_verify in i:
                if p_email_verify in i:
                    messagebox.showerror("GameZone","this email has been already exist.")
                    return
        if(i == email):
            pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            if not re.match(pat,i):
                messagebox.showerror("GameZone","Please enter valid email address.")
                return
        elif (i == number):
                if (len(i) != 10):
                    messagebox.showerror("GameZone", "Please enter valid 10 digits of Contact Number.")
                    return
                try:
                    con = int(number)
                except:
                    messagebox.showerror("GameZone", "Number should not contain any character.")
                    return
        elif (i == age):
            if (len(i)==0):
                messagebox.showerror("GameZone", "Please enter your age.")
                return
            
        
    gmail_user = ''
    gmail_password = ''
    to_test = email
    sent_from = gmail_user
    to = [to_test]
    subject = 'GameZone'
    a = username
    b = password
    body = 'you have been successfully registered.'

    email_text = """
    From : %s
    To : %s
    Subject : %s


    your username : %s
    your password : %s
        
        
        
    %s
    """ % (sent_from, ", ".join(to), subject,a,b, body)
    
    try:
        operation = """INSERT INTO player_details(username, password, email,number,age,snake_easy,snake_medium,snake_hard,car,dodge_ball) VALUES
		    			("{}", "{}", "{}","{}","{}",{}, {}, {},{},{})""".format(username,password,email,number,age,0,0,0,0,0)
        cursor.execute(operation)
        dbcon.commit()
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        
        messagebox.showinfo("GameZone","Successflly Register.")
        e1.set(" ")
        e2.set(" ")
    except:
        messagebox.showerror("GameZone","this username has already exist.")
def Back2():
    signin.withdraw()
    
def Back3():
    pregister.withdraw()

def Back():
    pregister.withdraw()
    signin.deiconify()
prbtn = Button(pregister,text="Back",font=("times new roman",15,"bold"),bd=4,bg="yellow",fg="red",command=Back).place(x=264,y=315)
prbtn = Button(pregister,text="Register",font=("times new roman",15,"bold"),bd=4,bg="yellow",fg="red",command=register_data).place(x=350,y=315)
signin.protocol("WM_DELETE_WINDOW",Back2)
pregister.protocol("WM_DELETE_WINDOW",Back3)

pregister.config(bg="ghostwhite")
pregister.withdraw()

#-------------------------------------------------------  Frame  ------------------------------------------------------------------
froot = Toplevel()
froot.iconbitmap(r"C:\Users\rajpu\Desktop\GameZone\Image\gameicon.ico")
froot.title("GameZone")
frame = Frame(froot)
screenwidth,screenheight = pyautogui.size()
frootbackgroundimg=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\gamezone.jpg")
frootresizebackimg = frootbackgroundimg.resize((1950, 1080), Image.LANCZOS)
frootmainbackimg=ImageTk.PhotoImage(frootresizebackimg)
# frootmainbacklabel = Label(froot,image=frootmainbackimg,height=screenheight,width=screenwidth).grid(row=0,column=0)
frootmainbacklabel = Label(froot,image=frootmainbackimg,height=717,width=1600, bg="red").place(x=0,y=0)

frootimg5=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\welcome.jpg")
frootph5=ImageTk.PhotoImage(frootimg5)
Label(froot,image=frootph5).place(x=750,y=25)

frootsnakegame = Frame(froot)
frootimg=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\snake-game.jpeg")
frootresizeimg = frootimg.resize((606, 200), Image.LANCZOS)
frootph=ImageTk.PhotoImage(frootresizeimg)
frootsnakegameimg = Label(frootsnakegame,image=frootph,height=198,width=606, bg="red").grid(row=0,column=0)
frootbtn = Button(frootsnakegame,text="Start",height=1,width=40,font=("times new roman",15,"bold"),bg="yellow",fg="red",activebackground="skyblue",command=defsnakegame).grid(row=1,column=0)
frootsnakegame.place(x=350,y=110)

frootponggame = Frame(froot)
frootimg1=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\pong.jpg")
frootresizeimg1 = frootimg1.resize((606, 200), Image.LANCZOS)
frootph1=ImageTk.PhotoImage(frootresizeimg1)
frootponggameimg = Label(frootponggame,image=frootph1,height=198,width=606, bg="red").grid(row=0,column=0)
frootbtn1 = Button(frootponggame,text="Start",height=1,width=40,font=("times new roman",15,"bold"),bg="yellow",fg="red",activebackground="skyblue",command=startponggame).grid(row=1,column=0)
frootponggame.place(x=980,y=110)

frootthirdrdgame = Frame(froot)
frootimg2=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\car_racing.jpg")
frootresizeimg2 = frootimg2.resize((606, 200), Image.LANCZOS)
frootph2=ImageTk.PhotoImage(frootresizeimg2)
frootthirdrdgameimg = Label(frootthirdrdgame,image=frootph2,height=198,width=606, bg="red").grid(row=0,column=0)
frootbtn2 = Button(frootthirdrdgame,text="Start",height=1,width=40,font=("times new roman",15,"bold"),bg="yellow",fg="red",activebackground="skyblue",command=startcarracinggame).grid(row=1,column=0)
frootthirdrdgame.place(x=350,y=390)

frootfourthgame = Frame(froot)
frootimg3=Image.open(r"C:\Users\rajpu\Desktop\GameZone\Image\dodge_the_ball.jpg")
frootresizeimg3 = frootimg3.resize((606, 200), Image.LANCZOS)
frootph3=ImageTk.PhotoImage(frootresizeimg3)
frootfourthgameimg = Label(frootfourthgame,image=ph3,height=198,width=606, bg="red").grid(row=0,column=0)
frootbtn1 = Button(frootfourthgame,text="Start",height=1,width=40,font=("times new roman",15,"bold"),bg="yellow",fg="red",activebackground="skyblue",command=startdadgethaball).grid(row=1,column=0)
frootfourthgame.place(x=980,y=390)

scroreframe = Frame(froot,width=330,height=500,bg="ghostwhite")
#Label(scroreframe,text="Welcome "+str(p_username),font=("times new roman",15,"bold"),bg="ghostwhite",fg="black")
# .place(x=10,y=10)
scroreframe.place(x=10,y=60)

def sign_out():
    froot.withdraw()
    gamezone.deiconify()
    ppass.set("")
    pname.set("")

Button(froot,text="Sign-Out",font=("times new roman",15,"bold"),bg="yellow",fg="red",activebackground="skyblue",width=8,command=sign_out).place(x=210,y=590)

# froot.state("zoomed")
froot.geometry("1600x680+210+100")
froot.resizable(False,False)
froot.withdraw()
froot.protocol("WM_DELETE_WINDOW", on_closing)
#---------------------------------------------------------------------------------------------------------------------

loginbutton = Button(gamezone,text="Sign-In",font=("times new roman",15,"bold"),bg="yellow",fg="red",activebackground="skyblue",width=8,command=sign_in).place(x=1350,y=640)

gamezone.config(background="red")
gamezone.geometry("1500x720+210+100")
gamezone.resizable(False, False)
# gamezone.state("zoomed")
gamezone.title("GameZone")
gamezone.iconbitmap(r"C:\Users\rajpu\Desktop\GameZone\Image\gameicon.ico")
gamezone.mainloop()