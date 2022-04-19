import sys
sys.path.insert(0,"/home/tada/L2libraries/Gyro_85/Gyro_85/i2clibraries/")
from time import *
from i2c_adxl345 import *
from i2c_itg3205 import *
from i2c_hmc5883l import *

class Gy85:
    #Initial Gy85
    def __init__(self,i2cPort,_acclAddress,_gyroAddress,_magAddress):
        self.I2CPort = i2cPort
        self.AcclAddress = _acclAddress
        self.GyroAddress = _gyroAddress
        self.MagAddress = _magAddress
        self.adxl345 = i2c_adxl345(self.I2CPort,self.AcclAddress)
        self.itg3205 = i2c_itg3205(self.I2CPort,self.GyroAddress)
        self.hmc5883l = i2c_hmc5883l(self.I2CPort,self.MagAddress)

    def GetAcclValue(self):
        return self.adxl345.getAxes();

    def GetGyroValue(self):
        (itgready,dataready) = self.itg3205.getInterruptStatus()

        return (self.itg3205.getDegPerSecAxes()[0],self.itg3205.getDegPerSecAxes()[1],self.itg3205.getDegPerSecAxes()[2],dataready);
    

    def GetMagValue(self,degree = 9,min = 54):
        self.hmc5883l.setContinuousMode()
        self.hmc5883l.setDeclination(degree,min)
        return self.hmc5883l.getAxes()





