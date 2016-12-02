# -*- coding: utf-8 -*-
import urllib, os

myloc = r"/Users/progamadores/Documents" #replace with your own location
key = "&key=" + "AIzaSyCyQx3weH5MwxzIIOsKSTHCvtn8929ffKM" #got banned after ~100 requests with no key
fov = "&fov=" + str(30)

directions = [
	["_Front", 0 , -10],
    ["_Back" , 180, -10],
    ["_Left" , 90, -10],
    ["_Right", 270, -10],
]

def GetStreet(Add,SaveLoc):
  base = "https://maps.googleapis.com/maps/api/streetview?size=800x600&location="

  for direction in directions:
    name = direction[0]
    heading  = "&heading=" + str((direction[1] + 50)%360.0)
    pitch = "&pitch=" + str(direction[2] % 360.0)

    MyUrl = base + Add + heading + pitch + fov + key
    fi = Add + name + fov + ".jpg"
    print(fi)
    urllib.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))

Tests = ["R. São Martinho, 1 - Cidade Nova, Rio de Janeiro - RJ, 20211-220"]

for i in Tests:
  GetStreet(Add=i,SaveLoc=myloc)