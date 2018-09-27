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


if __name__ == '__main__':
    unittest.main()
