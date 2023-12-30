import unittest
from app import get_employee, employee_is_valid

class TestEmployeeFunctions(unittest.TestCase):

    def setUp(self):
        self.employees = [
            {'id': 1, 'name': 'Ashley'},
            {'id': 2, 'name': 'Kate'},
            {'id': 3, 'name': 'Joe'}
        ]

    def test_get_employee_by_id_existing(self):
        employee = get_employee(1, self.employees)
        self.assertIsNotNone(employee)
        self.assertEqual(employee['id'], 1)

    def test_get_employee_by_id_non_existing(self):
        employee = get_employee(4, self.employees)
        self.assertIsNone(employee)

    def test_employee_is_valid_valid_employee(self):
        valid_employee = {'name': 'John'}
        self.assertTrue(employee_is_valid(valid_employee))

    def test_employee_is_valid_invalid_employee(self):
        invalid_employee = {'name': 'Alex', 'age': 25}
        self.assertFalse(employee_is_valid(invalid_employee))

    def test_employee_is_valid_empty_employee(self):
        empty_employee = {}
        self.assertFalse(employee_is_valid(empty_employee))

    