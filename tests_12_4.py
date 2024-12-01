import rt_with_exceptions as rt
import logging as log
import unittest




log.basicConfig(

    level=log.INFO,

    filemode='w',

    filename='runner_tests.log',

    encoding='UTF-8',

    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):


    def test_walk(self):

        try:

            runner = rt.Runner("Runner1", speed=-12)
            runner.walk()


            log.info('"test_walk" выполнен успешно')


        except ValueError as err:


            log.warning("Неверная скорость для Runner")


    def test_run(self):


        try:

            runner = rt.Runner(1, 12)
            runner.run()


            log.info('"test_run" выполнен успешно')


        except TypeError as err:
            log.warning("Неверный тип данных для объекта Runner")


if __name__ == '__main__':
    unittest.main()

