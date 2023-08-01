from enum import Enum
from heapq import heappush, heappop
from time import sleep
move_opposites = {"R" : "L", "L" : "R", "U" : "D", "D" : "U"}

class Pose(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    STANDING = 3


    def coords(self, x, y):
        if self == Pose.HORIZONTAL:
            return [(x, y), (x, y-1)]
        elif self == Pose.VERTICAL:
            return [(x, y), (x+1, y)]
        else:
            return [(x, y)]


    def next_pose(self, direction):
        # direction is one of set(["R", "L", "U", "D"])
        def hor_(direction):
            if direction == "R":
                return Pose.STANDING
            elif direction == "L":
                return Pose.STANDING
            elif direction == "U":
                return Pose.HORIZONTAL
            else:
                return Pose.HORIZONTAL
        def ver_(direction):
            if direction == "R":
                return Pose.VERTICAL
            elif direction == "L":
                return Pose.VERTICAL
            elif direction == "U":
                return Pose.STANDING
            else:
                return Pose.STANDING
        def stand_(direction):
            if direction == "R":
                return Pose.HORIZONTAL
            elif direction == "L":
                return Pose.HORIZONTAL
            elif direction == "U":
                return Pose.VERTICAL
            else:
                return Pose.VERTICAL
        if self == Pose.HORIZONTAL:
            return hor_(direction)
        elif self == Pose.VERTICAL:
            return ver_(direction)
        else:
            return stand_(direction)


    def next_coords(self, x, y, direction):
        def hor_(direction):
            if direction == "R":
                return (x+2, y)
            elif direction == "L":
                return (x-1, y)
            elif direction == "U":
                return (x, y-1)
            else:
                return (x, y+1)
        def ver_(direction):
            if direction == "R":
                return (x+1, y)
            elif direction == "L":
                return (x-1, y)
            elif direction == "U":
                return (x, y-2)
            else:
                return (x, y+1)
        def stand_(direction):
            if direction == "R":
                return (x+1, y)
            elif direction == "L":
                return (x-2, y)
            elif direction == "U":
                return (x, y-1)
            else:
                return (x, y+2)
        if self == Pose.HORIZONTAL:
            return hor_( direction)
        elif self == Pose.VERTICAL:
            return ver_(  direction)
        else:
            return stand_(  direction)


class Prism:
    def __init__(self, x, y, pose, parent, cost, last_move, the_goal_x, the_goal_y):
        self.x = x
        self.y = y
        self.pose = pose
        self.parent = parent
        self.cost = cost
        self.last_move = last_move
        self.the_goal_x = the_goal_x
        self.the_goal_y = the_goal_y
        self.heuristic = self._heuristic_function()


    def __lt__(self, other):    
        return self.cost + self.heuristic < other.cost + other.heuristic
    
    
    def isGoal(self):
        return (self.pose == Pose.STANDING ) and (self.x == self.the_goal_x) and (self.y == self.the_goal_y)

    
    def isValid(self, terrain):
        coords = self.pose.coords(self.x, self.y)
        for coord in coords:
            if coord[0] < 0 or coord[0] >= len(terrain[0]) or coord[1] < 0 or coord[1] >= len(terrain):
                return False
            if terrain[coord[1]][coord[0]] == "0":
                return False
        return True
    
    
    def _heuristic_function(self):
        return (min([abs(x-self.the_goal_x)+abs(y-self.the_goal_y) for (x,y) in self.pose.coords(self.x, self.y)]) // 3 + 1) * 2
    
    def extent_move(self):
        result = []
        directions = ["R","L","U","D"]
        if self.last_move:
            directions.remove(move_opposites[self.last_move])
        for direction in directions:
            new_x, new_y = self.pose.next_coords(self.x, self.y, direction)
            new_pose = self.pose.next_pose(direction)
            new_prism = Prism(new_x, new_y, new_pose, self, self.cost+1, direction, self.the_goal_x, self.the_goal_y)
            result.append( new_prism )
        return result
    

def blox_solver(ar):
    terrain = {
        Pose.HORIZONTAL : {},
        Pose.VERTICAL : {},
        Pose.STANDING : {}
    }
    def find_path(heap):
        while heap:
            current_prism = heappop(heap)
            for prism in current_prism.extent_move():
                if prism.isGoal():
                    return prism
                elif prism.isValid(ar):
                    if terrain[prism.pose].get((prism.x, prism.y), 1000000) > prism.cost:
                        terrain[prism.pose][(prism.x, prism.y)] = prism.cost
                        heappush(heap, prism)

    start_x, start_y = None, None
    goal_x, goal_y = None, None
    for j in range(len(ar)):
        for i in range(len(ar[0])):
            if ar[j][i] == "B":
                start_x, start_y = i, j
            elif ar[j][i] == "X":
                goal_x, goal_y = i, j
                
    start_prism = Prism(start_x, start_y, Pose.STANDING, None, 0, None, goal_x, goal_y)
    print(ar[start_y][start_x], ar[goal_y][goal_x])
    heap = [start_prism]
    
    current_prism = find_path(heap)
    if not current_prism:
        return "impossible"
    result = []
    coords = [(current_prism.x, current_prism.y)]
    while current_prism.parent:
        result.append(current_prism.last_move)
        current_prism = current_prism.parent
        coords.append((current_prism.x, current_prism.y))
    print(coords)
    print("result", result)
    
    return "".join(reversed(result))



example_tests = [
	['1110000000',
	'1B11110000',
	'1111111110',
	'0111111111',
	'0000011X11',
	'0000001110'],
	['000000111111100',
	'111100111001100',
	'111111111001111',
	'1B11000000011X1',
	'111100000001111',
	'000000000000111'],
	['00011111110000',
	'00011111110000',
	'11110000011100',
	'11100000001100',
	'11100000001100',
	'1B100111111111',
	'11100111111111',
	'000001X1001111',
	'00000111001111'],
	['11111100000',
	'1B111100000',
	'11110111100',
	'11100111110',
	'10000001111',
	'11110000111',
	'11110000111',
	'00110111111',
	'01111111111',
	'0110011X100',
	'01100011100'],
	['000001111110000',
	'000001001110000',
	'000001001111100',
	'B11111000001111',
	'0000111000011X1',
	'000011100000111',
	'000000100110000',
	'000000111110000',
	'000000111110000',
	'000000011100000']
]



example_sols = [['RRDRRRD','RDDRRDR','RDRRDDR'],['ULDRURRRRUURRRDDDRU','RURRRULDRUURRRDDDRU'],['ULURRURRRRRRDRDDDDDRULLLLLLD'],['DRURURDDRRDDDLD'],['RRRDRDDRDDRULLLUULUUURRRDDLURRDRDDR','RRRDDRDDRDRULLLUULUUURRDRRULDDRRDDR','RRRDRDDRDDRULLLUULUUURRDRRULDDRRDDR','RRRDDRDDRDRULLLUULUUURRRDDLURRDRDDR']]
for i,x in enumerate(example_tests):
    solution = blox_solver(x)
    print(solution, solution in example_sols[i])