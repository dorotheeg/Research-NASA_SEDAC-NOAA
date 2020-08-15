# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 08:44:49 2019

Mosaic for the mexico data

@author: dgrant
"""

import arcpy
import os
from arcpy import env
from arcpy.sa import *


raster_list = []
count = 219
outputDB = r'\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\mosaic\2018'
outName = "MDMosaic.tif"

# while loop to continue through the number of days, be sure to check if its 365 or 366!

while count < 220: 
    str_count = str(count)
    
# append the 0(s) in front to match the string file name
    
    if count < 10:
        pre = "00"
    elif count < 100:
        pre = "0"
    else:
        pre = ""

# need to update the year each time, to imporve would just add a vairbale year to only have to change it once
# get each input file path, append the day       
        
    input_h08v07 = r'\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Mexico\h08v07\2018' + '\\' + pre + str_count
    input_h08v06 = r'\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Mexico\h08v06\2018' + '\\' + pre + str_count
    input_h07v07 = r'\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Mexico\h07v07\2018' + '\\' + pre + str_count
    input_h07v06 = r'\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Mexico\h07v06\2018' + '\\' + pre + str_count
    input_h06v06 = r'\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Mexico\h06v06\2018' + '\\' + pre + str_count
    
    print(input_h06v06) # to know the day you are at

# get each file from the folder
# make sure that it is not empt, if it is, give file a blank
    
    if not os.listdir(input_h08v07):
        file1 = ""
    else:
        file1 = os.listdir(input_h08v07)[0]

    if not os.listdir(input_h08v06):
        file2 = ""
    else: 
        file2 = os.listdir(input_h08v06)[0]

    if not os.listdir(input_h07v07):
        file3 = ""
    else:
        file3 = os.listdir(input_h07v07)[0]

    if not os.listdir(input_h07v06):
        file4 = ""
    else:
        file4 = os.listdir(input_h07v06)[0]

    if not os.listdir(input_h06v06) :  
        file5 = ""
    else:
        file5 = os.listdir(input_h06v06)[0]
    

# append the output file name
# print is useful to see where you are if ever this is an issue!        
                    
    outFinal = outputDB + "\\" + outName
    print(outFinal)
        

# Create the new mosaic raster
    arcpy.MosaicToNewRaster_management([input_h08v07 + '\\' + file1, 
                             input_h08v06 + '\\' + file2, 
                             input_h07v07  + '\\'+ file3, 
                             input_h07v06 + '\\' + file4,
                             input_h06v06 + '\\' + file5], 
                             r"\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\mosaic\2018", "MDMosaic2018_" + str_count+ ".tif", 
                             "", "8_BIT_UNSIGNED", "", "4", "BLEND","FIRST") 



# print statemnts just helped me visualize where I was in the list when it was running    
    
    print("                 Break")             

# up count for the next day
    count +=1


print("command done")




# code snippet from Python for arcgis

# arcpy.management.Mosaic("DNB_Daily_Level3_h07v06.A2018001.5000.12_99_V25.tif;DNB_Daily_Level3_h07v07.A2018001.5000.12_99_V25.tif;DNB_Daily_Level3_h08v06.A2018001.5000.12_99_V25.tif", r"\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\mosaic\2018\MDMosaic.tif", "BLEND", "FIRST", None, None, "NONE", 0, "NONE")
