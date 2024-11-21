import unittest
import main

"""В методе start класса Tournament теперь возвращается имя участника (finishers[place] = participant.name), 
а не сам объект."""

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = main.Runner("Усэйн", 10)
        self.andrey = main.Runner("Андрей", 9)
        self.nick = main.Runner("Ник", 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_usain_and_nick(self):
        tournament = main.Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results.update({1: results})
        self.assertTrue(results[max(results)] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_andrey_and_nick(self):
        tournament = main.Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results.update({2: results})
        self.assertTrue(results[max(results)] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_all_three(self):
        tournament = main.Tournament(120, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.all_results.update({3: results})
        self.assertTrue(results[max(results)] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    unittest.main()