from random import randrange
from tkinter import Canvas, Tk, messagebox, font
import random

canvas_width = 800
canvas_height = 400
root = Tk() 
c = Canvas(root, width=canvas_width, height=canvas_height,background='light grey')     
c.pack()

player1 = c.create_oval(275, 230, 325, 280, fill='blue', width=0)
player2 = c.create_oval(475, 230, 525, 280, fill='red', width=0)

game_font = font.nametofont('TkFixedFont')
game_font.config(size=18)

player1_score = 0
player1_score_label = c.create_text(10, 10, anchor='nw',font=game_font,
                fill='darkblue', text='Player 1: ' + str(player1_score))

player2_score = 0
player2_score_label = c.create_text(630, 10, anchor='nw', font=game_font,
                fill='darkblue', text='Player 2: ' + str(player2_score))

small_balls = []

running = True

#This function will create the smalls balls that the players should eat
def create_small_balls(color):
    global running
    if running:   
        x = randrange(10, 740)
        y = randrange(10, 340)
        new_ball = c.create_oval(x, y,x+10, y+10, fill=color, width=0)
        small_balls.append(new_ball)
        colors=['blue','red']
        random.shuffle(colors)
    root.after(4000, lambda : create_small_balls(colors[0]))
    
#This function will check which ball did player 1 eat and
#it will increase or decrease the score depending on the
#ball it ate
def check_catch_p1():
    global running
    if running:
        #get the position of player 1
        (player1_x, player1_y, player1_x2, player1_y2) = c.coords(player1)
        for small_ball in small_balls:
            #get the position of current blue ball
            (small_ball_x, small_ball_y, small_ball_x2, small_ball_y2) = c.coords(small_ball)
            if player1_x < small_ball_x and small_ball_x2 < player1_x2 and abs(player1_y2 - small_ball_y2) < 30:
                    #update the score and the size of the player
                    small_ball_color = c.itemcget(small_ball, 'fill')
                    if small_ball_color == 'blue':
                        update_score_p1(10)
                        c.coords(player1, player1_x, player1_y, player1_x2 + 10, player1_y2 + 10)
                    else:
                        update_score_p1(-10)
                        c.coords(player1, player1_x, player1_y, player1_x2 - 10, player1_y2 - 10)
                    small_balls.remove(small_ball)
                    c.delete(small_ball)
    root.after(100, check_catch_p1)

#This function will check which ball did player 2 eat and
#it will increase or decrease the score depending on the
#ball it ate
def check_catch_p2():
    global running
    if running:
        #get the position of player 2
        (player2_x, player2_y, player2_x2, player2_y2) = c.coords(player2)
        for small_ball in small_balls:
            #get the position of current blue ball
            (small_ball_x, small_ball_y, small_ball_x2, small_ball_y2) = c.coords(small_ball)
            if player2_x < small_ball_x and small_ball_x2 < player2_x2 and abs(player2_y2 - small_ball_y2) < 30:
                    #update the score and the size of the player
                    small_ball_color = c.itemcget(small_ball, 'fill')
                    if small_ball_color == 'red':
                        update_score_p2(10)
                        c.coords(player2, player2_x, player2_y, player2_x2 + 10, player2_y2 + 10)
                    else:
                        update_score_p2(-10)
                        c.coords(player2, player2_x, player2_y, player2_x2 - 10, player2_y2 - 10)
                    small_balls.remove(small_ball)
                    c.delete(small_ball)
    root.after(100, check_catch_p2)

#This function will check if player 1 ate player 2
#or if player 2 ate player 1
def check_winner():
    global running
    if running:
        (player1_x, player1_y, player1_x2, player1_y2) = c.coords(player1)
        (player2_x, player2_y, player2_x2, player2_y2) = c.coords(player2)
        if player1_x < player2_x and player2_x2 < player1_x2 and abs(player1_y2 - player2_y2) < 30:
            c.coords(player1, player1_x, player1_y, player1_x2 + 30, player1_y2 + 30)
            c.delete(player2)
            update_score_p1(30)
            running = False
            messagebox.showinfo('Game Over!', ' Player 1 won with score ' \
                        + str(player1_score))
            root.destroy()
        elif player2_x < player1_x and player1_x2 < player2_x2 and abs(player2_y2 - player1_y2) < 30:
            c.coords(player2, player2_x, player2_y, player2_x2 + 30, player2_y2 + 30)
            c.delete(player1)
            update_score_p2(30)
            running = False
            messagebox.showinfo('Game Over!', ' Player 2 won with score ' \
                        + str(player2_score))
            root.destroy()
    root.after(100, check_winner)

#these functions will update the score of the players
def update_score_p1(points):
    global player1_score
    player1_score += points
    c.itemconfigure(player1_score_label, text='Player 1: ' + str(player1_score))

def update_score_p2(points):
    global player2_score
    player2_score += points
    c.itemconfigure(player2_score_label, text='Player 2: ' + str(player2_score))



#these functions will move the player in different directions 
def move_left(event, player):
    (x1, y1, x2, y2) = c.coords(player)
    if x1 > 0:
        c.move(player, -20, 0)
        
def move_right(event, player):
    (x1, y1, x2, y2) = c.coords(player)
    if x2 < canvas_width:
        c.move(player, 20, 0)

def move_up(event, player):
    (x1, y1, x2, y2) = c.coords(player)
    if y1 > 0:
        c.move(player, 0, -20)
        
def move_down(event, player):
    (x1, y1, x2, y2) = c.coords(player)
    if y2 < canvas_height:
        c.move(player, 0, 20)    


c.bind('<a>', lambda player: move_left(player, player1))
c.bind('<d>', lambda player: move_right(player, player1))
c.bind('<w>', lambda player: move_up(player, player1))
c.bind('<s>', lambda player: move_down(player, player1))

c.bind('<Left>', lambda player: move_left(player, player2))
c.bind('<Right>',lambda player: move_right(player, player2))
c.bind('<Up>',lambda player: move_up(player, player2))
c.bind('<Down>',lambda player: move_down(player, player2))


c.focus_set()

#call the functions 
root.after(1000, lambda : create_small_balls('red'))
root.after(1000, check_catch_p1)
root.after(1000, check_catch_p2)
root.after(1000, check_winner)

root.mainloop()



