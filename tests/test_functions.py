import unittest
from employees import get_employee, employee_is_valid, create_employee, update_employee, delete_employee

class TestEmployeeFunctions(unittest.TestCase):

    def setUp(self)
        self.employees = [
            {'id': 1, 'name': 'Ashley'},
            {'id': 2, 'name': 'Kate'},
            {'id': 3, 'name': 'Joe'}
        ]

    def test_get_employee_by_id_existing(self):
        employee = get_employee(1, self.employees)
        self.assertIsNotNone(employee)
        self.assertEqual(employee['id'], 1)
        self.assertEqual(employee['name'], 'Ashley')

    def test_get_employee_by_id_non_existing(self):
        employee = get_employee(4, self.employees)
        self.assertIsNone(employee)

    def test_employee_is_valid_valid_employee(self):
        valid_employee = {'name': 'John'}
        self.assertTrue(employee_is_valid(valid_employee))

    def test_employee_is_valid_invalid_employee(self):
        invalid_employee = {'name': 'Alex', 'age': 25}
        self.assertFalse(employee_is_valid(invalid_employee))

    def test_create_employee(self):
        next_id = len(self.employees) + 1
        new_employee = {'name': 'Michael', 'id': next_id}
        create_employee(self.employees, new_employee)
        self.assertEqual(len(self.employees), 4)
        self.assertIn(new_employee, self.employees)

    def test_update_employee(self):
        updated_info = {'name': 'Updated Name'}
        update_employee(1, updated_info, self.employees)
        updated_employee = get_employee(1, self.employees)
        self.assertEqual(updated_employee['name'], 'Updated Name')

    def test_delete_employee(self):
        delete_employee(1, self.employees)
        deleted_employee = get_employee(1, self.employees)
        self.assertIsNone(deleted_employee)
        self.assertEqual(len(self.employees), 2)

if __name__ == '__main__':
    unittest.main()