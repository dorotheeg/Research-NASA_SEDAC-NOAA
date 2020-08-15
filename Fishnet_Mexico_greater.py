# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:53:12 2019

@author: dgrant
"""


import arcpy
from arcpy.sa import *
from arcpy import env
import os

path = r"\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Mexico\h08v06\2012"
env.workspace = path


count = 20

while count < 366: 
    str_count = str(count)
    
# append the 0(s) in front to match the string file name
    
    if count < 10:
        pre = "00"
    elif count < 100:
        pre = "0"
    else:
        pre = ""

    counter = str(pre) + str_count
    temp = path + "\\" + counter
    env.workspace = temp
    file1 = os.listdir(temp)[0]
    print(file1)
    # arcpy.management.Clip("DNB_Daily_Level3_h08v06.A2015001.5000.45_85_V25.tif", "-95.8304359304738 29.0088340374609 -94.9743937686575 29.9837291538774", r"\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Houston\PleaseWork.tif", "Houston_fishnet_poly", -9.990000e+02, "NONE", "NO_MAINTAIN_EXTENT")
    arcpy.management.Clip(file1, "-95.8304359306272 29.008834038133 -94.9743937682749 29.9837291544849", r"\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Houston\Houston_2012_"+ counter + ".tif", r"\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Houston\Houston_fishnet_poly.shp", 0, "NONE", "NO_MAINTAIN_EXTENT")
    print (counter)
    count+=1
    temp = ""
    
    


print("DONE")

#list_num = [  157, 159, 179, 235, 248, 251, 266, 273, 300, 301, 304, 353]