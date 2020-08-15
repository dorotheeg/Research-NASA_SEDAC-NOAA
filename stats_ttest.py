# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:15:10 2019

@author: dgrant
"""
import arcpy
from scipy import stats
import numpy as np


# Get input Raster properties
inRas = arcpy.Raster(r'\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Las_Vegas_update\split\2012\weekday\DNB_Daily_Level3_h06v05.A2012019.5000.129_18_V25.tif.tif')
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

# Convert Raster to numpy array
arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=0)


# '\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Las_Vegas_update\split\2018\weekday\DNB_Daily_Level3_h06v05.A2018001.5000.11_99_V25.tif', 'r'




# data1 = r'\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Las_Vegas_update\split\2018\weekday\DNB_Daily_Level3_h06v05.A2018001.5000.11_99_V25.tif'
# data2 = r'\\DATASERVER1\GADdata$\dgrant\Documents\ArcGIS\Projects\TestingMyProject\Las_Vegas_update\split\2018\weekend\DNB_Daily_Level3_h06v05.A2018006.5000.59_76_V25.tif'

"""
ds = gdal.Open(data1)
myarray = np.array(ds.GetRasterBand(1).ReadAsArray())

ds2 = gdal.Open(data2)
myarray2 = np.array(ds2.GetRasterBand(1).ReadAsArray())

print(stats.ttest_ind(myarray,myarray2, equal_var = False))
"""

print("done")