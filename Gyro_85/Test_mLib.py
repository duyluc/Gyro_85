import sys
sys.path.insert(1,"/home/tada/L2libraries/")
import Gyro_85
import Gy85
import time
import curses

test_gyro85 = Gy85.Gy85(1,0x53,0x68,0x1e)

def screen_DisplayGyro(screen,col,x,y,z):
    screen.addstr(1,col,"%.1f do"%temp)
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
    pass



if __name__ == "__main__":
    Main()
