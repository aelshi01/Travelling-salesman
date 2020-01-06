import pytest
from cities import *

# compute_total_distance(road_map) - Returns, as a floating point number, the
# sum of the distances of all the connections in the road_map.Remember that it's a
# cycle, so that (for example) in the initial road_map, Wyoming connects to Alabama...

def test_compute_total_distance():
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    assert type(compute_total_distance(road_map)) == float
    assert len(road_map)>=1
    for i in range(len(road_map)):
         assert type(road_map[i][0] and road_map[i][1]) == str
         assert type(road_map[i][2] and road_map[i][3]) == float
         assert road_map[i][3] < 0




# swap_cities(road_map, index1, index2) - Take the city at location index in the road_map,
# and the city at location index2, swap their positions in the road_map, compute the new
# total distance, and return the tuple

def test_swap_cities():
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                 ("Delaware", "Dover", 39.161921, -75.526755),\
                 ("Arizona", "Phoenix'", 33.448457, -112.073844),\
                 ("Arkansas", "Little_Rock", 34.736009, -92.331122),\
                 ("California", "Sacramento", 38.555605, -121.468926),\
                 ("Colorado", "Denver", 39.7391667, -104.984167),\
                 ("Connecticut", "Hartford", 41.767, -72.677)]
     
    assert type(swap_cities(road_map,0,1)) == tuple
    assert swap_cities(road_map, 1, 1)[1] == compute_total_distance(road_map)
    #assert swap_cities(road_map, 0, 1)[1] == compute_total_distance(swap_cities(road_map,0,1)[0])
    new_road_map = swap_cities(road_map, 1, 5)
    #assert new_road_map[0][1] == road_map[5] and new_road_map[0][5] == road_map[1]
    assert len(swap_cities(road_map,0,1)) == 2



# shift_cities(road_map) - For every index i in the road_map, the city at the position i
# moves to the position i+1. The city at the last position moves to the position 0. Return
# the the new road map.

def test_shift_cities():
    road_map = [('Alabama', 'Montgomery', '32.361538', '-86.279118'),\
     ('Alaska', 'Juneau', '58.301935', '-134.41974'),\
     ('Arizona', 'Phoenix', '33.448457', '-112.073844'),\
     ('Arkansas', 'Little_Rock', '34.736009', '-92.331122'),\
     ('California', 'Sacramento', '38.555605', '-121.468926'),\
     ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
     ('Connecticut', 'Hartford', '41.767', '-72.677')]
     
    assert shift_cities(road_map) != shift_cities([('Arizona', 'Phoenix', 33.448457, -112.073844)])
    assert len(shift_cities(road_map)) == len(road_map)
    assert shift_cities(road_map) != road_map
    assert shift_cities(road_map)[1] == road_map[0]
    for i in range(len(road_map)):
        assert len(shift_cities(road_map)[i]) == 4
