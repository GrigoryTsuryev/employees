import requests
import pytest
import unittest
import json
import os

DOCKER_ENV = os.getenv('DOCKER_ENV')

# Define the base URL based on the environment
def get_base_url():
    # if DOCKER_ENV:
    return 'http://flask_app:5000'  # Replace with your service name
    # else:
        # return 'http://127.0.0.1:5000'  # Update with your local Flask app URL

@pytest.fixture
def base_url():
    return get_base_url()

# Test using unittest.TestCase
class TestAPI(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _setup(self, base_url):
        self.base_url = base_url

    # Test GET request for all employees
    def test_get_employees(self):
        response = requests.get(f"{self.base_url}/employees")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)  

    # # Test GET request for a specific employee by ID
    def test_get_employee_by_id(self):
        response = requests.get(f"{self.base_url}/employees/2")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['id'], 2)
        self.assertEqual(data['name'], 'Kate')

    # # # Test POST request to create a new employee
    def test_create_employee(self):
        new_employee = {'name': 'New Employee'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f"{self.base_url}/employees", data=json.dumps(new_employee), headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn('location', response.headers)



    def test_update_employee(self):
        updated_info = {'name': 'Updated Name'}
        headers = {'Content-Type': 'application/json'}
        response = requests.put(f"{self.base_url}/employees/2", data=json.dumps(updated_info), headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Updated Name')


    # # Test DELETE request to delete an employee
    def test_delete_employee(self):
        response = requests.delete(f"{self.base_url}/employees/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['id'], 1)

        # Verify that the employee has been deleted
        response = requests.get(f"{self.base_url}/employees/1")
        self.assertEqual(response.status_code, 404)
    

if __name__ == '__main__':
    unittest.main()