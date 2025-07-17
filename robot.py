DIRECTIONS = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

class Robot:
    def __init__(self, robot_id):
        self.id = robot_id
        self.position = (0, 0)

    def move(self, direction, steps, occupied_positions):
        dx, dy = DIRECTIONS[direction]
        x, y = self.position

        for _ in range(steps):
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in occupied_positions:
                break
            x, y = new_x, new_y

        self.position = (x, y)
        return self.position

class Terrain:
    def __init__(self):
        self.robots = {}
    
    def create_robot(self, robot_id):
        if robot_id in self.robots:
            raise ValueError("Robot with this ID already exists.")
        self.robots[robot_id] = Robot(robot_id)

    def move_robot(self, robot_id, command):
        robot = self.robots.get(robot_id)
        if not robot:
            raise ValueError("Robot ID not found")

        direction = command[0].upper()
        steps = int(command[1:])
        occupied = {r.position for rid, r in self.robots.items() if rid != robot_id}

        return robot.move(direction, steps, occupied)

    def get_robot_position(self, robot_id):
        robot = self.robots.get(robot_id)
        if not robot:
            raise ValueError("Robot ID not found")
        return robot.position
