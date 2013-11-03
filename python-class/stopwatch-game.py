# template for "Stopwatch: The Game"
import simplegui
# define global variables
stime=0
time=0
win_cnt=0
stp_cnt=0
stopped=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    c = t % 10
    seconds = t // 10    
    bc = seconds % 60
    a = seconds // 60
    
    if bc < 10:
        time_str = str(a)+':0'+str(bc)+'.'+str(c)
    else:
        time_str = str(a)+':'+str(bc)+'.'+str(c)
    return time_str
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_hdl():
    global stopped
    stopped = 0
    print 'start'
    timer.start()
   

def stop_hdl():
    global stime,win_cnt, stp_cnt, stopped
    if stopped == 0:
        stp_cnt = stp_cnt + 1
    c = stime % 10    
    if c == 0 and stopped == 0:
        win_cnt = win_cnt + 1
    stopped = 1
    print 'stop'
    timer.stop()
    

def rst_hdl():
    global stime, win_cnt, stp_cnt, stopped
    print stime
    stopped = 1
    timer.stop()
    stime = 0
    win_cnt = 0
    stp_cnt = 0
    print 'reset'
    pass

# define event handler for timer with 0.1 sec interval
def time_hdl():
    global stime
    stime = stime + 1

# define draw handler
def draw(canvas):
    global stime, win_cnt, stp_cnt
    str_time = format(stime)
    counter = str(win_cnt)+'/'+str(stp_cnt)    
    canvas.draw_text(counter,(250,30), 30, 'Green')
    canvas.draw_text(str_time,(50, 150), 70, 'Red')
    
# create frame
frame = simplegui.create_frame("StopWatch: The Game!!", 320, 300)

# register event handlers
frame.set_draw_handler(draw)
str_but = frame.add_button('Start', start_hdl,100)
stp_but = frame.add_button('Stop', stop_hdl,100)
rst_bt = frame.add_button('Reset', rst_hdl,100)
timer=simplegui.create_timer(100, time_hdl)

# start frame
frame.start()

# Please remember to review the grading rubric
