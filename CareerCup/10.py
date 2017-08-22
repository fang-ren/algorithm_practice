"""
8/19/2017
Author: Fang Ren
"""

"""
A robot in a room. The initial location is unknown. The shape or area of the room is unknown. You have a remote and can 
walk the robot in any directions (up, left, down, right), if the robot hits the wall, it method move() returns false, 
otherwise the robot move to the direction given. 
find the area of the room
"""

def move(position, direction):
    pass

def findNeighbor(position):
    return [(position[0], position[1]+1), (position[0]-1, position[1]),(position[0], position[1]-1),(position[0]+1, position[1])]

def area(origin):
    searched = [(0,0)]
    current_level = [(0,0)]
    while current_level:
        next_level = []
        for position in current_level:
            neighbors = findNeighbor(position)
            direction = 0
            for neighbor in neighbors:
                if neighbor not in searched and move(position, direction):
                    searched.append(neighbor)
                    next_level.append(neighbor)
                direction += 1
        current_level = next_level
    return len(searched)



