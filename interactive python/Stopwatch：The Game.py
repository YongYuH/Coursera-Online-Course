# template for "Stopwatch: The Game"

# for user interface
import simplegui
# for trunc fuction using in format
import math

# define global variables
time = 0
count_x = 0
count_y = 0
timer_detect = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = math.trunc(t / 600)
    B = math.trunc((t - A * 600) / 100)
    C = math.trunc((t % 100 - t % 10) / 10)
    D = math.trunc(t % 10)
    return str(A) + ":" + str(B) + str(C) + "."+ str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    timer.start()
    global timer_detect
    timer_detect = True
    
def stop_button_handler():
    global timer_detect
    timer.stop()
    global count_x
    global count_y
    if timer_detect:
        count_y += 1
        if (time % 10 == 0):
            count_x += 1   
    timer_detect = False
    
def reset_button_handler():
    timer.stop()
    global time
    global count_x
    global count_y
    global timer_detect
    time = 0
    count_x = 0
    count_y = 0
    timer_detect = False
    
# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time += 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), [100, 165], 50, 'White')
    canvas.draw_text(str(count_x)+ "/" +str(count_y), [212, 50], 50, 'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)
timer = simplegui.create_timer(100, time_handler)

# register event handlers
draw = frame.set_draw_handler(draw_handler)
start_button = frame.add_button('Start', start_button_handler, 100)
stop_button = frame.add_button('Stop', stop_button_handler, 100)
reset_button = frame.add_button('Reset', reset_button_handler, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
