# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# extract_by_mask.py
# Created on: 2013-08-16 10:45:03.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

arcpy.env.extent = "-74.00 -17.75 -44.00 5.25"

for j in range(1998, 2013):
		year = str(j)	
		for i in range(1, 13):
		    
		    if i>9:
		        month = str(i)
		    else:
		        month = "0" + str(i)
		
		    # Local variables:
		    inputMask = "C:\\Users\\Bruno\\Desktop\\Maxent\\Data\\WATER_DEFICIT_DATA_UNMASKED_TIFF\\Monthly_WATER_DEFICIT\\CWD_TRMM_" + year + month + "01.tiff"
		    mask = "C:\\Users\\Bruno\\Desktop\\Maxent\\Data\\MASK_DATA_2\\mascara_oficial_trmm_deter.tif"
		    output_Mask = "D:\\AndreLima\\CWD\\CWD_TRMM_" + year + month + "01.tif"
		
		    # Process: Extract by Mask
		    arcpy.gp.ExtractByMask_sa(inputMask, mask, output_Mask)
