from django.test import TestCase, Client
from django.contrib.auth.models import User
# Create your tests here.




class RegistrationTest(TestCase):
    def setUp(self):
        self.email = "test@example.com"
        self.username = "testuser"
        self.password = "testpass"

    def test_registration_with_existing_email(self):
        # Create a user with the email address we want to test
        User.objects.create_user(username="existinguser", email=self.email)

        # Submit the registration form with the same email address
        response = self.client.post("cvgen/register", {
            "username": self.username,
            "email": self.email,
            "password1": self.password,
            "password2": self.password,
        })

        # Check that the form didn't validate and that the error message is displayed
        self.assertFormError(response, "RegistrationForm", "email", "This email address is already in use.")
