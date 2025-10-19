from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.


class ProfileTestCase(TestCase):
    # user test
    def setUp(self):
        User.objects.create_user(
            'user_test', 'user_test@utest.com', 'passwordTest1234')

    def test_profile_exist(self):
        exist = Profile.objects.filter(user__username='user_test').exists()

        self.assertEqual(exist, True)
