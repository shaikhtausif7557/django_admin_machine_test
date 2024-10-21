
# Create your tests here.
from django.test import TestCase
from .models import client, User, projects

class ClientModelTest(TestCase):
    def setUp(self):
        self.client_instance = client.objects.create(name="Test Client", contact_info="test@example.com")

    def test_client_creation(self):
        self.assertIsInstance(self.client_instance, client)
        self.assertEqual(self.client_instance.name, "Test Client")
        self.assertEqual(str(self.client_instance), "Test Client")

class UserModelTest(TestCase):
    def setUp(self):
        self.user_instance = User.objects.create(userName="TestUser", email="testuser@example.com")

    def test_user_creation(self):
        self.assertIsInstance(self.user_instance, User)
        self.assertEqual(self.user_instance.userName, "TestUser")
        self.assertEqual(str(self.user_instance), "TestUser")

class ProjectsModelTest(TestCase):
    def setUp(self):
        # Create a client and user for testing
        self.test_client = client.objects.create(name="Test Client", contact_info="test@example.com")
        self.test_user = User.objects.create(userName="TestUser", email="testuser@example.com")
        self.project_instance = projects.objects.create(pname="Test Project", client=self.test_client)
        self.project_instance.users.add(self.test_user)  # Add user to the project

    def test_project_creation(self):
        self.assertIsInstance(self.project_instance, projects)
        self.assertEqual(self.project_instance.pname, "Test Project")
        self.assertEqual(self.project_instance.client, self.test_client)
        self.assertIn(self.test_user, self.project_instance.users.all())

    def test_project_users_relationship(self):
        self.assertEqual(self.project_instance.users.count(), 1)  # Ensure one user is assigned
        self.assertEqual(self.project_instance.users.first(), self.test_user)  # Check that the user assigned is correct
