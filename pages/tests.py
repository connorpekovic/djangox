from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from .views import HomePageView, DetailView, CreateCBView, UpdateCBView, DeleteCBView, HasVoted
from .models import Response

# Create your tests here.

# We are going to test ALL the pages a user can try to access before logging in.
class AnonymousUserTest(TestCase):

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
        self.assertTemplateUsed(self.home_response, 'pages/home.html') #Only 2 templates in play before signin because
        self.assertTemplateUsed(self.read_response, 'pages/read.html') #Create, Update, Delete pages lead to redirects

    # Assert the setUp responce(parm1) contains a str(parm2) and a coded http responce code(parm3).
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.home_response, '<h3 style="text-align: center;">Participate')
        self.assertContains(self.read_response, '<h3 style="text-align: center;">View Results</h3>')

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

#Test that the sign up page works
class SignupPageTests(TestCase):
    
    def setUp(self):
        # url = reverse('signup') Used only if we overwrite Django AllAuth
        self.response = self.client.get('/accounts/signup/')

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign up')

# Testing that our customer user model works.
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

# Test the create form's page.
class CreatePageTest(TestCase):
    
    def setUp(self):
        User = get_user_model() #Create test user for subsequent test.
        user = User.objects.create_user( 
            username='rachel',
            email='rachel@email.com',
            password='testpass123'
        )

    # Test what happens when a loggin in user accesses the Create page.
    def test_create_page_logged_in_user(self):
        self.client.login(username='rachel', password='testpass123') # Log in / credentials
        url = reverse('create') 
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200) # Assure url success
        self.assertTemplateUsed(response, 'pages/create.html') #Assure correct template used
        view = resolve('/create/')
        self.assertEqual(           # Check that the URL Path resolves from CreateEBView view.py function
            view.func.__name__,
            CreateCBView.as_view().__name__
        )

    # Test what happens when a logged out user accesses the Create page.
    def test_create_page_logged_out_user(self):
        self.client.logout() # Logout
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 302) # Assure url redirects 
        self.assertRedirects(response,(reverse('account_signup')))  # Redirects to 'account_signup' url name.


# Test the update form's page.
class UpdatePageTest(TestCase):
    
    def setUp(self):
        User = get_user_model() #Create test user for subsequent test.
        user = User.objects.create_user( 
            username='rachel',
            email='rachel@email.com',
            password='testpass123'
        )

    # Test what happens when a loggin in user accesses the Update page.
    def test_update_page_logged_in_user(self):
        self.client.login(username='rachel', password='testpass123') # Log in / credentials
        url = reverse('update') 
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200) # Assure url success
        self.assertTemplateUsed(response, 'pages/update.html') #Assure correct template used
        view = resolve('/update/')
        self.assertEqual(           # Check that the URL Path resolves from UpdateEBView view.py function
            view.func.__name__,
            UpdateCBView.as_view().__name__
        )

    # Test what happens when a logged out user accesses the Update page.
    def test_update_page_logged_out_user(self):
        self.client.logout() # Logout
        response = self.client.get(reverse('update'))
        self.assertEqual(response.status_code, 302) # Assure url redirects 
        self.assertRedirects(response,(reverse('account_signup')))  # Redirects to 'account_signup' url name.


# Test the delete form's page.
class DeletePageTest(TestCase):
    
    def setUp(self):
        User = get_user_model() #Create test user for subsequent test.
        user = User.objects.create_user( 
            username='rachel',
            email='rachel@email.com',
            password='testpass123'
        )
        # login = self.client.login(username='rachel', password='testpass123')
        # url = reverse('delete')
        # self.response = self.client.get(url)

    # Test what happens when a loggin in user accesses the Delete page.
    def test_delete_page_logged_in_user(self):
        self.client.login(username='rachel', password='testpass123') # Log in / credentials
        url = reverse('delete') 
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200) # Assure url success
        self.assertTemplateUsed(response, 'pages/delete.html') #Assure correct template used
        view = resolve('/delete/')
        self.assertEqual(           # Check that the URL Path resolves from DeleteEBView view.py function
            view.func.__name__,
            DeleteCBView.as_view().__name__
        )

    # Test what happens when a logged out user accesses the Delete page.
    def test_delete_page_logged_out_user(self):
        self.client.logout() # Logout
        response = self.client.get(reverse('delete'))
        self.assertEqual(response.status_code, 302) # Assure url redirects 
        self.assertRedirects(response,(reverse('account_signup')))  # Redirects to 'account_signup' url name.


#Testing the Response objects create-read-update-delete abilities
class ResponseObjectTest(TestCase):
    def setUp(self):
        User = get_user_model() #Create test user for subsequent test.
        testuser = User.objects.create_user( 
            username='rachel',
            email='rachel@email.com',
            password='testpass123'
        )
        self.client.login(username='rachel', password='testpass123')
        # self.special_permission = Permission.objects.get(  # How to add permissions for our test.
        #     codename='special_status'
        # )

        # setUp 1 test object
        self.Response = Response.objects.create(
            Question1 = 'Yes',
            Question2 = 'Yes',
            Question3 = 'Strong',
            Question4 = 'Yes',
            Question5 = 'Yes',
            created_by = testuser
        )
    
    # Assert responces are correct
    def test_responses(self):
        self.assertEqual(f'{self.Response.Question1}','Yes')
        self.assertEqual(f'{self.Response.Question2}','Yes')
        self.assertEqual(f'{self.Response.Question3}','Strong')
        self.assertEqual(f'{self.Response.Question4}','Yes')
        self.assertEqual(f'{self.Response.Question5}','Yes')