from django.test import TestCase
from .models import Customer

class CustomerTests(TestCase):
    def setUp(self):
        # Create a test customer
        self.customer = Customer.objects.create(
            name="Test Customer",
            email="test@example.com",
            phone_number="1234567890",
            address="123 Test Street, Test City"
        )

    def test_customer_str(self):
        # Test string representation of customer
        self.assertEqual(str(self.customer), "Test Customer")

    def test_unique_email(self):
        # Test uniqueness of email field
        with self.assertRaises(Exception):
            customer_duplicate = Customer.objects.create(
                name="Duplicate Customer",
                email="test@example.com",
                phone_number="9876543210",
                address="456 Duplicate Street, Duplicate City"
            )
