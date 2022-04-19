import sys
sys.path.insert(1,"./i2clibraries")
from time import *
from i2c_adxl345 import *

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
        return self.itg3205.getAxes();

    def GetMagValue(self,degree = 9,min = 54):
        self.hmc5883l.setContinuousMode()
        self.setDeclination(degree,min)
        return self.hmc5883l.getAxes()


    



