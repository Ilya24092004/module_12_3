import module_12_1
import module_12_2
import unittest

proverka = unittest.TestSuite()
proverka.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
proverka.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))

proverka_2 = unittest.TextTestRunner(verbosity=2)
proverka_2.run(proverka)