from django.test import TestCase
from .models import ServiceRequest
from customer_accounts.models import Customer

class ServiceRequestTests(TestCase):
    def setUp(self):
        # Create a test customer
        self.customer = Customer.objects.create(
            name="Test Customer",
            email="test@example.com",
            phone_number="1234567890",
            address="123 Test Street, Test City"
        )

        # Create a test service request
        self.service_request = ServiceRequest.objects.create(
            customer=self.customer,
            request_type="Test Request",
            details="This is a test request details",
            attachment=None,  # You can upload a file for testing if needed
            status="Pending"
        )

    def test_service_request_str(self):
        # Test string representation of service request
        self.assertEqual(str(self.service_request), "Service Request #1")

    def test_service_request_customer(self):
        # Test the customer associated with the service request
        self.assertEqual(self.service_request.customer, self.customer)

    def test_service_request_status(self):
        # Test the default status of the service request
        self.assertEqual(self.service_request.status, "Pending")

