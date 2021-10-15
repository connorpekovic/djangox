from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .views import HomePageView, DetailView, NewPostView, UpdateView, DeleteView, UserAlreadyVotedView

# Create your tests here.

class HomepageTests(SimpleTestCase):

    # Assign variables used in other test.
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    # Assert availability of URL pattern name in get('#').
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    # Asserts that the template with the given name was used in rendering the setUp response.
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'pages/home.html')

    # Assert the setUp responce(parm1) contains a str(parm2) and a coded http responce code(parm3).
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Home', status_code=200)

    # Assert the setUp responce(parm1) DOES NOT contains a string(parm2).
    def test_homepage_does_not_contain_incorrect_html(self):
         self.assertNotContains(
             self.response, 'Hi there! I should not be on the page.')

    # Check that a view.py function resolves to a given URL Path
    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class CustomUserTests(TestCase):

    #Assert user account creation works
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='rachel',
            email='rachel@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'rachel')
        self.assertEqual(user.email, 'rachel@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    #Assert superuser account creation works
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)