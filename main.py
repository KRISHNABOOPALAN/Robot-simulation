from robot import Terrain

if __name__ == "__main__":
    terrain = Terrain()
    
    terrain.create_robot(1)
    terrain.create_robot(2)
    
    print("Move Robot 1:", terrain.move_robot(1, "E5"))
    print("Move Robot 2:", terrain.move_robot(2, "E5"))
    print("Robot 1 Position:", terrain.get_robot_position(1))
    print("Robot 2 Position:", terrain.get_robot_position(2))
