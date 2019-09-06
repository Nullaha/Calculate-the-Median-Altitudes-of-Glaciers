import arcpy
import os
from arcpy import env
import time

# -1 tif and tif>shp.
# 0 shp and it includes name field.
env.workspace = "F:/running/auto-zone/labs/hss/alps" # RE

# 1 contours
in_raster = "alps.tif" # RE
contour_interval = 30 # RE
base_contour = 0
out_contours = "xian1.shp"   # xian 1

# Check out the ArcGIS 3D Analyst extensionlicense
arcpy.CheckOutExtension("3D")

t1 = time.time()
#Exe Contours
arcpy.Contour_3d(in_raster,out_contours,contour_interval,base_contour)
elapsed1 = (time.time()-t1)

print("finish part 1------------------")
print("time:",elapsed1)

time.sleep(2)


# 2 cut
clip_features = "alpst.shp"  # mian 1 RE
out_features = "xian2_identity.shp"  # xian 2
xy_tolerance = ""

t2 = time.time()
# Execute Clip
arcpy.Clip_analysis(out_contours, clip_features, out_features, xy_tolerance)
elapsed2 = (time.time()-t2)

print("finish part 2------------------")
print("time:",elapsed2)

time.sleep(2)


# 3 identity
id_features = "xian3.shp"
t3 = time.time()
arcpy.Identity_analysis(out_features, clip_features, id_features)
elapsed3 = (time.time()-t3)

print("finish part 3------------------")
print("time:",elapsed3)

time.sleep(2)


# 4 features to polygon
in_features4 = [id_features, clip_features]
to_polygon = "mian2_polygon.shp"
clus_tol = "0.05 Meters"

t4 = time.time()
arcpy.FeatureToPolygon_management(in_features4, to_polygon, clus_tol, "NO_ATTRIBUTES", "")
elapsed4 = (time.time()-t4)

print("finish part 4------------------")
print("time:",elapsed4)

time.sleep(2)


# 5 spatial join
spatial_join5 = "mian3.shp"

#  Create FieldMappings object to manage merge output fields
fieldmappings = arcpy.FieldMappings()

# Add all fields from both oldStreets and newStreets
fieldmappings.addTable(to_polygon)
fieldmappings.addTable(id_features)

# First get the CONTOUR fieldmap. CONTOUR is a field in the xian3 feature class.
conFieldIndex = fieldmappings.findFieldMapIndex("CONTOUR")
fieldmap = fieldmappings.getFieldMap(conFieldIndex)

# Get the output field's properties as a field object
field = fieldmap.outputField

fieldmap.mergeRule = "mean"
fieldmappings.replaceFieldMap(conFieldIndex, fieldmap)

# delete field

x2 = fieldmappings.findFieldMapIndex("FID_xian2_")
fieldmappings.removeFieldMap(x2)
x3 = fieldmappings.findFieldMapIndex("Id")
fieldmappings.removeFieldMap(x3)

t5 = time.time()
arcpy.SpatialJoin_analysis(to_polygon, id_features, spatial_join5, "#", "#", fieldmappings, "SHARE_A_LINE_SEGMENT_WITH")
elapsed5 = (time.time()-t5)

print("finish part 5------------------")
print("time:",elapsed5)

time.sleep(2)


# 6 calculate
out_calculate = "finally_areas.shp"
t6 = time.time()
try:    
	# Process: Calculate Areas...    
	arcpy.CalculateAreas_stats(spatial_join5, out_calculate)
except:    
	# If an error occurred when running the tool, print out the error message.    
	print arcpy.GetMessages()

elapsed6 = (time.time()-t6)

print("finish part 6------------------")
print("time:",elapsed6)
