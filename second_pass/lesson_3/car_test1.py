import unittest

class Car:
    def __init__(self):
        self.wheels = 4

class CarTest(unittest.TestCase):
    @unittest.skip('Skipping the wheel test')
    def test_wheels(self):
        car = Car()
        self.assertEqual(4, car.wheels)

    def test_member(self):
        car = Car()
        self.assertIn(car.wheels, [4, 5, 6])

    def test_bad_wheels(self):
        car = Car()
        self.assertEqual(3, car.wheels)


if __name__ == '__main__':
    unittest.main()