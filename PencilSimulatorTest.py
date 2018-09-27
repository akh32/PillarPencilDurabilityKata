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

    def test_pencil_durability_for_capital_letters(self):
        self.pencil = PencilSimulator(3)
        self.assertEqual("He   ", self.pencil.write("Hello"))

    def test_pencil_durability_for_spaces(self):
        self.pencil = PencilSimulator(3)
        self.assertEqual("hi y  ", self.pencil.write("hi you"))

    def test_pencil_durability_for_newlines(self):
        self.pencil = PencilSimulator(3)
        self.assertEqual("hi\ny  ", self.pencil.write("hi\nyou"))

    def test_NOT_IN_REQUIREMENTS_pencil_durability_halfway_through_capitals(self):
        self.pencil = PencilSimulator(3)
        self.assertEqual("HE   ", self.pencil.write("HELLO"))

    def test_pencil_sharpened_regains_initial_durability(self):
        self.pencil = PencilSimulator(3)
        self.pencil.write("Hello")
        self.pencil.sharpen()
        self.assertEqual("He   Ev      ", self.pencil.write("Everyone"))

    def test_pencil_sharpened_regains_initial_durability_of_four(self):
        self.pencil = PencilSimulator(4)
        self.pencil.write("Hello")
        self.pencil.sharpen()
        self.assertEqual("Hel  Eve     ", self.pencil.write("Everyone"))

    def test_pencil_sharpened_too_many_times_cannot_be_restored(self):
        self.pencil = PencilSimulator(3)
        self.pencil.sharpen()
        self.pencil.sharpen()
        self.assertEqual("hel  ", self.pencil.write("hello"))
        self.pencil.sharpen()
        self.assertEqual("hel   ", self.pencil.write("a"))

    def test_pencil_length_determines_number_of_sharpens_allowed(self):
        self.pencil = PencilSimulator(3,6)
        self.pencil.sharpen()
        self.pencil.sharpen()
        self.assertEqual("hel  ", self.pencil.write("hello"))
        self.pencil.sharpen()
        self.assertEqual("hel  a", self.pencil.write("a"))
        self.pencil.sharpen()
        self.pencil.sharpen()
        self.pencil.sharpen()
        self.assertEqual("hel  abcd", self.pencil.write("bcd"))
        self.pencil.sharpen()
        self.assertEqual("hel  abcd  ", self.pencil.write("ef"))

    def test_pencil_will_erase_text(self):
        self.pencil.write("The quick brown fox jumps over the lazy dog")
        self.assertEqual("The quick brown     jumps over the lazy dog", self.pencil.erase("fox"))

    def test_pencil_will_erase_last_instance(self):
        self.pencil.write("The quick brown dog jumps over the lazy dog")
        self.assertEqual("The quick brown dog jumps over the lazy    ", self.pencil.erase("dog"))

    def test_eraser_degradation(self):
        self.pencil = PencilSimulator(4000, 2, 3)
        self.pencil.write("The quick brown fox jumps over the lazy dog")
        self.assertEqual("The quick br    fox jumps over the lazy dog", self.pencil.erase("brown"))




if __name__ == '__main__':
    unittest.main()
