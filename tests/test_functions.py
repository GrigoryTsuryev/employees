import unittest
import json
from employees import app, get_employee, employee_is_valid
from unittest.mock import patch

class TestEmployeeFunctions(unittest.TestCase):

        def setUp(self):
            self.app = app.test_client()
            self.employees = [
                {'id': 1, 'name': 'Ashley'},
                {'id': 2, 'name': 'Kate'},
                {'id': 3, 'name': 'Joe'}
            ]
        
        def test_get_employees(self):
            response = self.app.get('/employees')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(data, self.employees)
        def test_get_employee_by_id_correct(self):
            response = self.app.get('/employees/1')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(data, self.employees[0])

        def test_get_employee_by_id_not_correct(self):
            response = self.app.get('/employees/5')
            self.assertEqual(response.status_code, 404)
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(data['error'], 'Employee does not exist')


        def test_employee_is_valid(self):
            valid_employee = {'name': 'John'}
            invalid_employee = {'id': 2, 'name': 'Kate'}
            self.assertTrue(employee_is_valid(valid_employee))
            self.assertFalse(employee_is_valid(invalid_employee))


        def test_update_employee(self):
            employee_id = 1
            updated_employee_data = {'name': 'Updated Name'}
            response = self.app.put(f'/employees/{employee_id}', data=json.dumps(updated_employee_data), content_type='application/json')
            self.assertEqual(response.status_code, 200)

            updated_employee = get_employee(employee_id)
            self.assertEqual(updated_employee['name'], updated_employee_data['name'])

            response = self.app.put('/employees/10', data=json.dumps(updated_employee_data), content_type='application/json')
            self.assertEqual(response.status_code, 404)

        def test_delete_employee(self):
            response = self.app.delete('/employees/10')
            self.assertEqual(response.status_code, 404)

        def test_invalid_employee_properties(self):
            invalid_employee = {'id': 5, 'name': 'Invalid', 'age': 30}
            response = self.app.post('/employees', data=json.dumps(invalid_employee), content_type='application/json')
            self.assertEqual(response.status_code, 400)

            response = self.app.put('/employees/1', data=json.dumps(invalid_employee), content_type='application/json')
            self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()