import unittest,main



class QuizTestCase(unittest.TestCase):
    def test_question_1(self):
        """Question 1."""
        msg = """True and False are boolean values.
        Interestingly, they inherit from ints. Read more here:
        https://medium.com/rmotr-com/those-tricky-python-booleans-2100d5df92c#.hiwfwzcrg
        """
        self.assertEqual(main.question_1(), "Boolean", msg)

    def test_question_2(self):
        """Question 2."""
        msg = """The `or` operation will return the *FIRST* truthy value.
        That's the first True in the expression.
        """
        self.assertEqual(main.question_2(), True, msg)

    def test_question_3(self):
        """Question 3."""
        self.assertEqual(main.remove_Es('remoter'), 'rmotr')
        self.assertEqual(main.remove_Es('eaEjd2'), 'ajd2')
        self.assertEqual(main.remove_Es('eE'), '')

    def test_question_4(self):
        """Question 4."""
        msg = "The answer is 22, check the code in this test for more info"
        self.assertEqual(main.question_4(), 22, msg)

        # result = a_list[3**2 - 8] + a_list[-1] + a_tuple[2]
        #          a_list[9  -   8] + a_list[-1] + a_tuple[2]
        #          a_list[    1   ] + a_list[-1] + a_tuple[2]
        #                1          +     9      +    12
        #                            22

    def test_question_5(self):
        """Question 5."""
        self.assertEqual(main.calculate_tax(0), 0)
        self.assertEqual(main.calculate_tax(40000), 6000.0)
        self.assertEqual(main.calculate_tax(63500), 15875.0)
        self.assertEqual(main.calculate_tax(82100), 24630.0)
        self.assertEqual(main.calculate_tax(250000), 87500.0)

    def test_question_6(self):
        """Question 6."""
        m1 = [
            [2, 9, 1],
            [3, 1, 18],
            [22, 8, 16]
        ]
        m2 = [
            [81, 29],
            [31, 57]
        ]
        m3 = [[3]]
        self.assertEqual(main.matrix_sum(m1), 80)
        self.assertEqual(main.matrix_sum(m2), 198)
        self.assertEqual(main.matrix_sum(m3), 3)
