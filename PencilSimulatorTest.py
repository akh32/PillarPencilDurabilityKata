import unittest
from PencilSimulator import PencilSimulator

class PencilSimulatorTest(unittest.TestCase):
    def setUp(self):
        self.pencil = PencilSimulator()

    def test_pencil_simulator_writes_text(self):
        self.assertEqual("written", self.pencil.write("written"))

    def test_pencil_simulator_appends_text(self):
        self.assertEqual("written", self.pencil.write("written"))
        self.assertEqual("written and added", self.pencil.write(" and added"))

    def test_pencil_durability_created_at_zero(self):
        self.pencil = PencilSimulator(0)
        self.assertEqual("  ", self.pencil.write("hi"))

    def test_pencil_durability_created_at_three(self):
        self.pencil = PencilSimulator(3)
        self.assertEqual("hel  ", self.pencil.write("hello"))

if __name__ == '__main__':
    unittest.main()
