import math
import random

def dist(p1, p2):
    """
    Find the euclidean distance between two 2-D points

    Args:
        p1: (p1_x, p1_y)
        p2: (p2_x, p2_y)
    
    Returns:
        Euclidean distance between p1 and p2
    """
    return (((p1[0]) - (p2[0]))**2 + ((p1[1]) -(p2[1]))**2)**0.5

def sort_points_by_x(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by X coordinate
    """
    s = []
    m = []
    for num in points:
        s.append(num[0])
    s.sort()
    for num in s:
        for dum in points:
            if num == dum[0]:
                m.append(dum)
    unique_d = []
    for num in m:
        if num not in unique_d:
            unique_d.append(num)
    return unique_d        
#print(sort_points_by_x([(3, 4), (1, 1), (7, 5),(3, 5)]))

def sort_points_by_y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by Y coordinate 
    """
    s = []
    m = []
    for num in points:
        s.append(num[1])
    s.sort()    
    for num in s:
        for dum in points:
            if num == dum[1]:
                m.append(dum)
    unique_d = []
    for num in m:
        if num not in unique_d:
            unique_d.append(num)
    return unique_d      

#print(sort_points_by_y([(3, 4), (1, 8), (7, 6), (3, 5)]))

def naive_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    s = []
    for num in plane:
        for dum in plane:
            h = (num, dum , dist(num, dum))
            s.append(h)
    unique = []
    for num in s:
        if num[0] != num[1]:
            unique.append(num)
    values = []        
    for num in unique:
        values.append(num[2])
    values.sort()
    for num in unique:
        if values[0] in num:
            return num
#print(naive_closest_pair([(5, 4), (3, 2), (9, 10)]))        
#print(naive_closest_pair([(5, 4), (6, 3), (3, 2)])) 

def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a 
    given upper bound. This function is called by 
    efficient_closest_pair_routine

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by 
            efficient_closest_pair_routine

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)] if
        distance between p1 and p2 is less than d. Otherwise
        return -1.
    """
    s = []
    l = []
    for num in points:
        for dum in points:
            h = (num, dum , dist(num, dum))
            s.append(h)
            
    unique = []
    for num in s:
        if num[0] != num[1] and num[2] < d:
            unique.append((num[0]))
            unique.append(num[1])
            
    for num in unique:
        if num not in l:
            l.append(num)            
            
    values = []
    t = sort_points_by_y(l)
    if len(l) != 0:
        
        return naive_closest_pair(l)
    else:
        return -1

#print(closest_pair_in_strip([(5, 4), (6, 6), (3, 2), (1, 1), (6, 7), (11, 13), (15, 16), (16, 18)], 16))

def efficient_closest_pair_routine(points):
    s = []
    l = []
    for num in points:
        for dum in points:
            h = (num, dum , dist(num, dum))
            s.append(h)
    for num in s:
        if num[0] != num[1]:
            
            l.append(num[2])
    t = min(l)
    for num in s:
        if num[2] == t:
            return num
print(efficient_closest_pair_routine([(5, 4), (6, 6), (3, 2), (1, 1), (6, 7), (11, 13), (15, 16), (16, 18)]))        

def efficient_closest_pair(points): 
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    
    q = len(points)
    if q == 3:
        distance = (10**9)**3
        s = efficient_closest_pair_routine(points)
        if s[2] <= distance:
                return s[2]
        else:
            return distance
    elif q == 2:
        distance = (10**9)**3
        s = efficient_closest_pair_routine(points)
        if s[2] <= distance:
            return distance
        else:
            return distance
    else:
        distance = (10**9)**3
        middlevalue = points[q//2]
        m = efficient_closest_pair(points[:q//2])
        n = efficient_closest_pair(points[q//2:])
        d = distance
        if closest_pair_in_strip(points, d) == -1:
            return distance
        else:
            return closest_pair_in_strip(points, distance)
        
print(efficient_closest_pair([(4.10, 4),(4.15, 4),(4.25, 4),(4.5, 4),(5, 4), (8, 2), (9, 10)]))
    
def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points: [(p1_x, p1_y), (p2_x, p2_y), ...]
    """
    
    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]

    return random_points



if __name__ == "__main__":  
    #number of points to generate
    num_pts = 10
    #size of plane for generation of points
    plane_size = (10, 10) 
    plane = generate_plane(plane_size, num_pts)
    print(plane)
    #naive_closest_pair(plane)
    #efficient_closest_pair(plane)
print(generate_plane((100, 100), 10))        

             