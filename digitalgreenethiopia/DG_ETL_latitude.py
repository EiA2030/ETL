import pandas as pd
import json
import geopandas as gpd
from pyproj import Proj, Transformer
from shapely.geometry import Point

# Reproject lat lon
def reproj(x, y, srcprj):
    if srcprj == "WGS 84 GCS":
        srcprj = "epsg:4326"
        transformer = Transformer.from_crs(srcprj,prj)
    # else: NEED TO ADD THE OTHER POSSIBLE SRIDs
    x,y = transformer.transform(x, y)
    return x,y

# Check if point is in Ethiopia
def lonlat(lon, lat):
  longitude, latitude = reproj(lon, lat, srcprj)
  pnt = Point(longitude, latitude)
  if eth.contains(pnt):
    longitude = longitude
    latitude = latitude
  else:
    longitude = 'na'
    latitude = 'na'
  return longitude, latitude    
