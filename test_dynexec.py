import unittest
import json
import os
import inspect
from dynexec.operator import Operator


class TestOperator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        with open(f'{dir_path}/scripts.json', 'r') as f:
            cls.scripts = json.load(f)

    def setUp(self):
        self.operator = Operator()

    def tearDown(self):
        self.operator = None

    def test_disallowed_input(self):
        self.operator._script = self.scripts[inspect.currentframe().f_code.co_name]
        with self.assertRaises(ValueError):
            self.operator._execute()
            self.assertIsNone(self.operator._result.body)

    def test_disallowed_import(self):
        self.operator._script = self.scripts[inspect.currentframe().f_code.co_name]
        with self.assertRaises(ValueError):
            self.operator._execute()
            self.assertIsNone(self.operator._result.body)

    def test_disallowed_exec(self):
        self.operator._script = self.scripts[inspect.currentframe().f_code.co_name]
        with self.assertRaises(ValueError):
            self.operator._execute()
            self.assertIsNone(self.operator._result.body)

    def test_allowed_numpy_basic(self):
        self.operator._script = self.scripts[inspect.currentframe().f_code.co_name]
        try:
            self.operator._execute()
        except Exception as e:
            self.fail(f'Unexpected exception: {e}')
        self.assertIsNotNone(self.operator._result.body)

    def test_allowed_numpy_pandas_basic(self):
        self.operator._script = self.scripts[inspect.currentframe().f_code.co_name]
        try:
            self.operator._execute()
        except Exception as e:
            self.fail(f'Unexpected exception: {e}')
        self.assertIsNotNone(self.operator._result.body)

    def test_disallowed_in_callbacks(self):
        pass


if __name__ == '__main__':
    unittest.main()
