import sys
sys.path.insert(1,"/home/tada/L2libraries/")
import Gyro_85
import Gy85
import time
import curses

test_gyro85 = Gy85.Gy85(1,0x53,0x68,0x1e)

def screen_DisplayGyro(screen,col,x,y,z):
    #screen.addstr(1,col,"%.1f do"%temp)
    screen.addstr(2,col,"%.1f do"%x)
    screen.addstr(3,col,"%.1f do"%y)
    screen.addstr(4,col,"%.1f do"%z)

def screen_DisplayAccl(screen,col,x,y,z):
    screen.addstr(1,col,"%.2f do"%x)
    screen.addstr(2,col,"%.2f do"%y)
    screen.addstr(3,col,"%.2f do"%z)
    
def screen_DisplayMag(screen, col, heading, declination,x,y,z):
    screen.addstr(1,col,heading+" ")
    screen.addstr(2,col,decliantion+" ")
    screen.addstr(3,col,"%.2f  " %x)
    screen.addstr(4,col,"%.2f  " %y)
    screen.addstr(5,col,"%.2f  " %z)

def Main():
    myscreen = curses.initscr() # Initialize the curses
    myscreen.border(0)
    (screen_h, screen_w) = myscreen.getmaxyx() # Get screen height and width 
    curses.start_color() # Set the color 
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN) # The bottom of the green black 
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # White with blue words 
    curses.init_pair(3, curses.COLOR_MAGENTA,curses.COLOR_BLACK) # What's in black 
    myscreen.clear() # Remove the canvas 
    #  Calculate the coordinates of each block ,  The screen 3 column ,  Each column displays one sensor 
    col1 = screen_w / 3 * 0
    col2 = screen_w / 3 * 1
    col3 = screen_w / 3 * 2
    #  The screen is divided into three horizontal sections , Write a title in the middle of each block 
    myscreen.addstr(0, int(col1 + screen_w / 3 / 2 - 3), "GYRO", curses.color_pair(1))
    myscreen.addstr(0, int(col2 + screen_w / 3 / 2 - 4), "ACCL", curses.color_pair(1))
    myscreen.addstr(0, int(col3 + screen_w / 3 / 2 - 4), "MAG", curses.color_pair(1))
    
    # Painting line , Divide the screen into 3 column 
    for col in range(1, screen_h):
        myscreen.addstr(col, int(col2), " │ ")
        myscreen.addstr(col, int(col3), " │ ")
    #  Print in advance IGT3205 The names of the values of 
    myscreen.addstr(1, int(col1), "Temp:", curses.color_pair(2))
    myscreen.addstr(2, int(col1), "X   :", curses.color_pair(2))
    myscreen.addstr(3, int(col1), "Y   :", curses.color_pair(2))
    myscreen.addstr(4, int(col1), "z   :", curses.color_pair(2))
    #  Print in advance ADXL345 The names of the values of 
    myscreen.addstr(1, int(col2) + 1, "X:", curses.color_pair(2))
    myscreen.addstr(2, int(col2) + 1, "Y:", curses.color_pair(2))
    myscreen.addstr(3, int(col2) + 1, "z:", curses.color_pair(2))
    #  Print in advance HMC5883L The names of the values of 
    myscreen.addstr(1, int(col3) + 1, "Heading:    ", curses.color_pair(2))
    myscreen.addstr(2, int(col3) + 1, "Declination:", curses.color_pair(2))
    myscreen.addstr(3, int(col3) + 1, "X:          ", curses.color_pair(2))
    myscreen.addstr(4, int(col3) + 1, "Y:          ", curses.color_pair(2))
    myscreen.addstr(5, int(col3) + 1, "z:          ", curses.color_pair(2))
    #  Initialization 
    while True:
        GyroValue = test_gyro85.GetGyroValue()
        if GyroValue[3]:
             #temp = GyroValue[0]
             (x, y, z) = (GyroValue[0],GyroValue[1],GyroValue[2]) 
             screen_DisplayGyro(myscreen, 6, x, y, z) # Refresh the canvas 
        # read adxl345 data 
        (x, y, z) = adxtest_gyro85.GetAcclValue()
        screen_DisplayAccl(myscreen, int(col2) + 4, x, y, z) # Refresh the canvas 
        # read hmc5883l data 
        (x, y, z) = adxtest_gyro85.GetMAgValue()
        heading = adxtest_gyro85.hmc5883l.getHeadingString() # Get the pointing Angle 
        declination = adxtest_gyro85.hmc5883l.getDeclinationString() # Obtain the compensation information of magnetic declination Angle 
        screen_DisplayMag(myscreen, int(col3) + 13, heading, declination, x, y, z) # Refresh the canvas 
        myscreen.refresh() # Application of the canvas 
        sleep(0.1) # suspended 0.1 seconds 

if __name__ == "__main__":
    try:
        Main()
    except Exception as e:
        print(str(e))
