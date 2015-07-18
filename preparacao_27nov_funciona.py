import arcpy
from arcpy import env
import os

env.workspace = r"F:\data\zhu\mapeamento_guapiara_2014_pronto_v03\analise\buffer_250m\slip_points"
arcpy.env.extent = "-74.00 -17.75 -44.00 5.25"

fcList = arcpy.ListFeatureClasses ()
i=1
for fc in fcList:
    print fc
    #arcpy.AddField_management(fc,"areas","SHORT",3)
    #arcpy.CalculateField_management(fc, "areas",i)
    print i
    i=i+1
    
    
    
#Process: Add Field
    arcpy.AddField_management(fc, "Prop", "FLOAT", 18, 6, "", "", "", "")
# Process: Calculate Field
    
# Process: Output name
    ofile=unicode(""+os.path.splitext(fc)[0]+".tif")
    print fc + " - " + ofile
    arcpy.PolygonToRaster_conversion(fc, "Prop_def2", ofile, "CELL_CENTER", "NONE", "0.25")
# Process: Convert to ascii
rasterList = arcpy.ListRasters()
for rt in rasterList:
    ofile2=unicode(""+os.path.splitext(rt)[0]+".asc")
    print rt + " - " + ofile2
    arcpy.RasterToASCII_conversion(rt, ofile2)
 
 