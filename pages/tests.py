from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .views import HomePageView, DetailView, CreateCBView, UpdateCBView, DeleteCBView, HasVoted

# Create your tests here.

class OrganicUserTest(TestCase):

    # Assign variables used in other test.
    def setUp(self):
        url_home = reverse('home')
        url_create = reverse('create')
        url_created = reverse('created')
        url_read = reverse('read')
        url_update = reverse('update')
        url_delete = reverse('delete')
        self.home_response = self.client.get(url_home)
        self.create_response = self.client.get(url_create)
        self.created_response = self.client.get(url_created)
        self.read_response = self.client.get(url_read)
        self.update_response = self.client.get(url_update)
        self.delete_response = self.client.get(url_delete)


    # Assert availability of URL pattern name in get('#').
    def test_homepage_status_code(self):
        home_response = self.client.get('/')
        create_response = self.client.get('/create/')
        read_response = self.client.get('/read/')
        update_response = self.client.get('/update/')
        delete_response = self.client.get('/delete/')
        self.assertEqual(home_response.status_code, 200)   # Users are not allowed to create, 
        self.assertEqual(create_response.status_code, 302) # update or delete vote objects until
        self.assertEqual(read_response.status_code, 200)   # they are signed in, so pages/views.py
        self.assertEqual(update_response.status_code, 302) # redirects users to the signup.html page
        self.assertEqual(create_response.status_code, 302) # if they try to CURD before logging in.


    # Asserts that the template with the given name was used in rendering the setUp response.
    def test_homepage_template(self):
        self.assertTemplateUsed(self.home_response, 'pages/home.html') #Only 2 templates in play before signin
        self.assertTemplateUsed(self.read_response, 'pages/read.html')

    # Assert the setUp responce(parm1) contains a str(parm2) and a coded http responce code(parm3).
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.home_response, 'Participate in community decesion making with the Normal Organization')

    # Assert the setUp responce(parm1) DOES NOT contains a string(parm2).
    def test_homepage_does_not_contain_incorrect_html(self):
         self.assertNotContains(
             self.home_response, 'Hi there! I should not be on the page.')


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

class CustomUserTests(TestCase):
    
    def setUp(self):
        # url = reverse('signup') Used only if we overwrite Django AllAuth
        self.response = self.client.get('/accounts/signup/')

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign up')