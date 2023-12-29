import unittest
import json
from your_flask_app import app

class TestEmployeeFunctions(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

        # Initialize some test data
        self.test_employees = [
            {'id': 1, 'name': 'Ashley'},
            {'id': 2, 'name': 'Kate'},
            {'id': 3, 'name': 'Joe'}
        ]
        self.next_id = 4

    def test_get_employee_by_id(self):
        employee_id = 2
        # Test the function that gets an employee by ID from the data
        employee = self.get_employee(employee_id)
        self.assertIsNotNone(employee)
        self.assertEqual(employee['id'], employee_id)

    def test_get_employee_not_found(self):
        # Test for a case where the employee is not found
        employee_id = 10
        employee = self.get_employee(employee_id)
        self.assertIsNone(employee)

    def get_employee(self, employee_id):
        # Simulate the function to get an employee from the data
        return next((e for e in self.test_employees if e['id'] == employee_id), None)

