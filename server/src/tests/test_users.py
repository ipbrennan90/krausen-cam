import json
import unittest

from src.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users(self):
        """Ensure the /users route behaves correctly."""
        response = self.client.get('/users')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()