from typing import Tuple
import math

EARTH_RADIUS = 6371e3 # in meters

MKAD_AREA=((55.503, 37.329), (55.917, 37.895))
MKAD_LOC=(55.7888, 37.6802)

class Geodesic_dist:
    meters:float
    def __init__(self, loc:Tuple):
        self.meters = 0

        # Checking whether it is within the MKAD.
        if self.is_in_area(loc,MKAD_AREA) == False:
            # Measure geodesic distance from given coordinates to MKAD
            self.meters = self.measure(loc,MKAD_LOC)
        else:
            self.meters= 0

    # Geodesic measurement function with two coordinates
    def measure(self,loc1:Tuple,loc2:Tuple) -> float:
        latitude1,longitude1 = loc1[0],loc1[1]
        latitude2,longitude2 = loc2[0],loc2[1]
        
        # latitude,longitude in radians
        lati1 = latitude1 * math.pi/180 
        lati2 = latitude2 * math.pi/180
        dif_latitude = (latitude2 - latitude1) * math.pi/180
        dif_longitude = (longitude2 - longitude1) * math.pi/180

        a = math.sin(dif_latitude/2) * math.sin(dif_latitude/2) + \
            math.cos(lati1) * math.cos(lati2) * \
            math.sin(dif_longitude/2) * math.sin(dif_longitude/2)
        
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        dist = EARTH_RADIUS * c

        return dist
    
    # Function to check whether the given coordinate is in given area.
    def is_in_area(self,loc:Tuple,area) -> bool:
        loc_latitude,loc_longitude = loc[0],loc[1]

        area_low_latitude,area_low_longitude  = area[0][0],area[0][1]
        area_up_latitude,area_up_longitude  = area[1][0],area[1][1]

        return (area_low_latitude<=loc_latitude and loc_latitude<=area_up_latitude and 
                area_low_longitude <=loc_longitude  and loc_longitude <=area_up_longitude )
    
    @property
    def meter(self):
        return self.meters

    @property
    def m(self):
        return self.meter
            
    @property
    def Kilometer(self):
        return self.meters / 1000
        
    @property
    def Km(self):
        return self.Kilometer
