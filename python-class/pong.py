# Implementation of classic arcade game Pong

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
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,0] 
paddle1_vel = 0
paddle2_vel = 0
right_win = 0
left_win = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    if direction == 'LEFT':
        ball_vel=[-2,-2]
    else:
        ball_vel=[2,-2]

def restart_game():
    new_game()
    
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global left_win, right_win  # these are ints
    left_win = 0
    right_win = 0
    spawn_ball('LEFT')
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global right_win, left_win
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
          
    # draw ball
    c.draw_circle(ball_pos,BALL_RADIUS, 1,'White','White')
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    
    if paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
        
    if paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    
    if paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    
    
    # paddle positions list
    paddle1_list = [(0,paddle1_pos - HALF_PAD_HEIGHT),(PAD_WIDTH,paddle1_pos - HALF_PAD_HEIGHT),(PAD_WIDTH,paddle1_pos + HALF_PAD_HEIGHT),(0,paddle1_pos + HALF_PAD_HEIGHT)]
    paddle2_list = [(WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH,paddle2_pos + HALF_PAD_HEIGHT), (WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT)]
    
    # draw paddles    
    c.draw_polygon(paddle1_list, 1, 'White', 'White')
    c.draw_polygon(paddle2_list, 1, 'White', 'White')    
    
    
    if (ball_pos[0]  <= PAD_WIDTH + BALL_RADIUS):
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT - 10 and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT + 10:
            ball_vel[0] = -(ball_vel[0] + (ball_vel[0]*0.1))
            ball_vel[1] = (ball_vel[1] + (ball_vel[1]*0.1))
        else:
            right_win += 1
            spawn_ball('RIGHT')
    
    if ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT - 10 and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT + 10:
            ball_vel[0] = -(ball_vel[0]+ (ball_vel[0]*0.1))
            ball_vel[1] = (ball_vel[1] + (ball_vel[1]*0.1))
        else:
            left_win +=1
            spawn_ball('LEFT')
            
    #verify the wall collision    
    if (ball_pos[1] <= BALL_RADIUS) or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    
    
    # draw scores
    c.draw_text(str(left_win) , [(WIDTH /2) - 55, 50], 42,'Blue')
    c.draw_text(str(right_win) , [(WIDTH /2) + 55, 50], 42,'Red')
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP['w']:        
            paddle1_vel -= 10        
    elif key == simplegui.KEY_MAP['s']:        
            paddle1_vel += 10        
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 10
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 10
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('Restart',restart_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
