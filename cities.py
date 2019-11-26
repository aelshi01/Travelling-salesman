def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    f = open(file_name,"r")
    lst =[]
    j=0
    for x in f:
        lst.append(x)
    for i in lst:
        lst[j]=i.rstrip('\n')
        j+=1
    for i in range(len(lst)):
        lst[i]= tuple(lst[i].split())
    return lst
    

  
def print_cities(road_map):
    """
        Prints a list of cities, along with their locations.
        Print only one or two digits after the decimal point.
        """
    lst1 = []
    l = read_cities(road_map)
    for i in range(len(l)):
        lst1.append(l[i][1:4])

    for i in range(len(lst1)):
        lst1[i]=tuple([lst1[i][0],round(float(lst1[i][1]),2),round(float(lst1[i][2]),2)])

    print(lst1)

import math

def compute_total_distance(road_map):
    """
        Returns, as a floating point number, the sum of the distances of all
        the connections in the `road_map`. Remember that it's a cycle, so that
        (for example) in the initial `road_map`, Wyoming connects to Alabama...
        """
    d = 0
    for i in range(len(road_map)-1):
        d += math.sqrt((float(road_map[i][2]) - float(road_map[i+1][2]))**2 + (float(road_map[i][3]) - float(road_map[i+1][3]))**2)
    d+= math.sqrt((float(road_map[0][2]) - float(road_map[len(road_map)-1][2]))**2 + (float(road_map[0][3]) - float(road_map[len(road_map)-1][3]))**2)
    return d




def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple
        
    (new_road_map, new_total_distance)
        
    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    city1 = road_map[index1]
    city2 = road_map[index2]
    road_map[index1] = city2
    road_map[index2] = city1
    
    new_road_map = road_map
    
    
    
    return (new_road_map, compute_total_distance(new_road_map))

def shift_cities(road_map):
    """
        For every index i in the `road_map`, the city at the position i moves
        to the position i+1. The city at the last position moves to the position
        0. Return the new road map.
        """
    lst = []
    lst.append(road_map[len(road_map)-1])
    for i in range(0,len(road_map)-1):
        lst.append(road_map[i])
    
    
    return lst

def find_best_cycle(road_map):
    """
        Using a combination of `swap_cities` and `shift_cities`,
        try `10000` swaps/shifts, and each time keep the best cycle found so far.
        After `10000` swaps/shifts, return the best cycle found so far.
        Use randomly generated indices for swapping.
        """
    best_cycle = compute_total_distance(road_map)
    for i in range(1000):
        num1 = rd.randint(1,49)
        num2 = rd.randint(1,49)
        swap_cities(road_map,num1,num2)
        shift_cities(road_map)
        new_best_cycle = compute_total_distance(road_map)
        if new_best_cycle < best_cycle:
            best_cycle = new_best_cycle
    
    return  best_cycle 

def print_map(road_map):
    """
        Prints, in an easily understandable format, the cities and
        their connections, along with the cost for each connection
        and the total cost.
        """
    dic = {}
    for i in range(len(road_map)-2):
        dic[road_map[i][1]] = (road_map[i+1][1], compute_total_distance(road_map[i:i+2]))
    
    return dic

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__": #keep this in
    main()
