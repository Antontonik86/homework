import runner_and_tournament as r_and_t
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = r_and_t.Runner("Усэйн", 10)
        self.andrey = r_and_t.Runner("Андрей", 9)
        self.nick = r_and_t.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_usein_nick(self):
        tournament = r_and_t.Tournament(93, self.usein, self.nick)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_andrey_nick(self):
        tournament = r_and_t.Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_usein_andrey_nick(self):
        tournament = r_and_t.Tournament(90, self.usein, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()


