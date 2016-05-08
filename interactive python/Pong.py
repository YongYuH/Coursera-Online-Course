# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user40_A9cdfARaCyoPzhG.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1 = 0
score2 = 0

paddle1_vel= [0, 0]
paddle2_vel= [0, 0]

paddle1_pos = [0 + HALF_PAD_WIDTH, HEIGHT / 2] 
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]

# initialize ball_pos and ball_vel for new bal in middle of table
ball_vel = [0, 0]
ball_pos = [WIDTH / 2, HEIGHT / 2] 

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if(direction == LEFT):
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        ball_vel = [-random.randrange(120, 240), -random.randrange(60, 180)]
    elif(direction == RIGHT):
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        ball_vel = [random.randrange(120, 240), -random.randrange(60, 180)]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    # initialize the score
    score1 = 0
    score2 = 0
    # initialize the paddle position
    paddle1_pos = [0 + HALF_PAD_WIDTH, HEIGHT / 2] 
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]
    
    spawn_ball(bool(random.randrange(0, 2)))
       
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
         
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")       
    # update ball
    ball_pos[0] += 0.01 * ball_vel[0]
    ball_pos[1] += 0.01 * ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel[1]
    paddle2_pos[1] += paddle2_vel[1]
    if paddle1_pos[1] < 0 + HALF_PAD_HEIGHT:
        paddle1_pos[1] = 0 + HALF_PAD_HEIGHT
    elif paddle1_pos[1] > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    if paddle2_pos[1] < 0 + HALF_PAD_HEIGHT: 
        paddle2_pos[1] = 0 + HALF_PAD_HEIGHT
    elif paddle2_pos[1] > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    # determine whether paddle and ball collide
    if ball_pos[1] < 0 + BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] *= -1
    # left paddle
    if ball_pos[0] < 0 + PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] < paddle1_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] > paddle1_pos[1] - HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.25
        else:
            score2 += 1
            spawn_ball(RIGHT)
    # right paddle     
    elif ball_pos[0] > WIDTH - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] < paddle2_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] > paddle2_pos[1] - HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.25
        else:
            score1 += 1
            spawn_ball(LEFT)
    # draw paddles
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT],[paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT], 7.5, 'White')
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT],[paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT], 7.5, 'White')
    # draw scores
    canvas.draw_text(str(score1), (150, 60), 50, 'White')
    canvas.draw_text(str(score2), (450, 60), 50, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= 5       
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += 5
    elif key == simplegui.KEY_MAP["up"]:    
        paddle2_vel[1] -= 5       
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += 5
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["up"]:    
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0

def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('New game', button_handler, 100)

# start frame
new_game()
frame.start()
