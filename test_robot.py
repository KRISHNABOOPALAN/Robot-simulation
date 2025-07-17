import unittest
from robot import Terrain

class TestRobotMovement(unittest.TestCase):
    def setUp(self):
        self.terrain = Terrain()
        self.terrain.create_robot(1)
        self.terrain.create_robot(2)

    def test_initial_position(self):
        self.assertEqual(self.terrain.get_robot_position(1), (0, 0))

    def test_simple_move(self):
        self.terrain.move_robot(1, "E3")
        self.assertEqual(self.terrain.get_robot_position(1), (0, 3))

    def test_collision(self):
        self.terrain.move_robot(1, "E3")
        self.terrain.move_robot(2, "E4")
        self.assertEqual(self.terrain.get_robot_position(2), (0, 2))

if __name__ == '__main__':
    unittest.main()
