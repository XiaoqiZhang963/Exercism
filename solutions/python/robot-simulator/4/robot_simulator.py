# Globals for the directions
# Change the values as you see fit
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

MOVES = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0),
}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        if direction not in DIRECTIONS:
            raise ValueError('Invalid direction')
 
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    def update_direction(self,turn):
        index = DIRECTIONS.index(self.direction)
        index_updated = (index + 1)%4 if turn == 'R' else (index - 1)%4
        self.direction = DIRECTIONS[index_updated]
        
    def update_xy(self):
        x_move, y_move = MOVES[self.direction]
        self.x_pos += x_move
        self.y_pos += y_move

    def move(self, instructions):
        for instruction in instructions:
            if instruction not in 'LRA':
                raise ValueError('Invalid instructions')
            if instruction == 'A':
                self.update_xy()
            else:
                self.update_direction(instruction)
        
