# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:35:05 2020

@author: chris
"""

from shapely.geometry import Point, Polygon

poly = Polygon([(0, 0), (2,8), (14, 10), (6,1)])
point = Point(4,4)

poly.exterior.distance(point)