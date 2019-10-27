import pytest
from cities import *

# compute_total_distance(road_map) - Returns, as a floating point number, the
# sum of the distances of all the connections in the road_map.Remember that it's a
# cycle, so that (for example) in the initial road_map, Wyoming connects to Alabama...

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    assert type(compute_total_distance(road_map)) == float
    assert 0 < test_compute_total_distance(0) < 0.1

# swap_cities(road_map, index1, index2) - Take the city at location index in the road_map,
# and the city at location index2, swap their positions in the road_map, compute the new
# total distance, and return the tuple

def test_swap_cities():
    assert type(road_map) == tuple
    assert 0 <=swap_cities(road_map, index1, index2 = index1) < 0.1


# shift_cities(road_map) - For every index i in the road_map, the city at the position i
# moves to the position i+1. The city at the last position moves to the position 0. Return
# the the new road map.

def test_shift_cities():
    assert shift_cities(road_map) != shift_cities([(Arizona, Phoenix, 33.448457, -112.073844)])

