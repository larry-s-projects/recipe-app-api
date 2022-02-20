from django.test import TestCase, Client
from django.contrib.auth import get_user, get_user_model
from django.urls import reverse



class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@sdfdsf.com',
            password='password123'
        )
        # this uses the Client helper function that allows a user to login with the Django authentication
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='adsfaf@gmail.com',
            password='password123',
            name="test user full name"
        )


    def test_users_listed(self):
        """test users are listed on user page"""
        #this URLS are located in the Django documentation. This will basically generate the URL for our list user page
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test user edit page works"""
        url  = reverse('admin:core_user_change', args=[self.user.id])
        #/admin/core/user/{id}
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)


    def test_create_user_page(self):
        """Test that the create user page works"""

        url = reverse('admin:core_user_add')
        res =self.client.get(url)
        self.assertEqual(res.status_code, 200)




