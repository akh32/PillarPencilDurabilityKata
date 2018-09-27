import unittest
from PencilSimulator import PencilSimulator

class PencilSimulatorTest(unittest.TestCase):
    def test_pencil_simulator_writes_text(self):
        pencil = PencilSimulator()
        self.assertEqual("written", pencil.write("written"))


if __name__ == '__main__':
    unittest.main()
