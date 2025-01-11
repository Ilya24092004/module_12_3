from unittest import TestCase
import unittest



class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(TestCase):
    def test_walk(self):
        peshehod = Runner('Пешеход')
        for i in range(10):
            peshehod.walk()
        self.assertEqual(peshehod.distance, 50)

    def test_run(self):
        begun = Runner('Бегун')
        for i in range(10):
            begun.run()
        self.assertEqual(begun.distance, 100)

    def test_challenge(self):
        peshehod = Runner('Пешеход')
        begun = Runner('Бегун')
        for i in range(10):
            peshehod.walk()
            begun.run()
        self.assertNotEqual(peshehod.distance, begun.distance)


if __name__ == "__main__":
    unittest.main()