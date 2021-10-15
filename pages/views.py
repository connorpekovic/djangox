# views.py
from django.views.generic import View, TemplateView,  CreateView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from .forms import ResponseForm
from .models import Response
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.utils import timezone

# Table of Contents
#   Static Pages
#   Create views
#   Read views
#   Update views
#   Delete views

################
# Static views #
################
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class UserAlreadyVotedView(TemplateView):
    template_name = 'pages/iscreated.html'


##########
# Create #
##########

# Class-Based View(CVB) example
# A Class-Based View extends the View class. Requests are handled inside class methods named after
# the HTTP methods (GET, POST, PUT, HEAD ect.) offering SUPERIOR flexability.
class NewPostView(View):

    # Renders the base HTML.
    def render(self, request):
        return render(request, 'pages/create.html',  {'form': ResponseForm})

    # Renders the Create form, if user is 1) logged in and 2) has not already voted.
    def get(self, request):

        # Redirect non-user to the all-auth sign up page. You must have account to Vote.
        if self.request.user.is_authenticated:
            pass
        else:
            return redirect('account_signup')

        PrevResponse = Response.objects.filter(created_by=self.request.user) # Query with a WHERE clause.
        if PrevResponse.exists():      # Redirect users who have already voted away from the Create page.
            return redirect('votecasted')

        self.form = ResponseForm()  # Render requested Create form.
        return self.render(request)


    def post(self, request):

        self.form = ResponseForm(request.POST)

        if self.form.is_valid():
            self.form = self.form.save(commit=False) #This is the trick to saving editing input b4 commit.
            self.form.created_by = self.request.user
            self.form.save()
            return redirect('read')
            
        return self.render(request)


# Generic Class-Based View (GCBV) example of a CreateView.
class VoteView(CreateView):
    model = Response
    form_class = ResponseForm
    template_name = 'pages/create.html'
    success_url = 'pages/read.html'
   
    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Saveing user UUID to the Responce.

        if self.request.user.is_authenticated:  # Assert user is logged in.
            pass
        else:
            return redirect('account_signup')

        # Assert user vote will be unique
        PrevResponse = Response.objects.filter(created_by=self.request.user) # Query with a WHERE clause.
        if PrevResponse.exists():
            return redirect('votecasted')

        return super(VoteView, self).form_valid(form)


########
# Read #
########
class DetailView(ListView):
    model = Response
    context_object_name = 'response_list' #Name of object in HTML template.
    template_name = 'pages/read.html'


##########
# Update #
##########

# Class-Based View(CVB)
#  A Class-Based View extends the View class. Requests are handled inside class methods named after
#  the HTTP methods (GET, POST, PUT, HEAD ect.) offering SUPERIOR flexability.
class UpdateView(View):

    def render(self, request):
        return render(request, 'pages/update.html',  {'form': ResponseForm})

    def post(self, request):

        #Delete the existing users previous entry.
        Response.objects.filter(created_by=self.request.user).delete()

        #Post the form data to the Django server.
        self.form = ResponseForm(request.POST)

        #If the form is valid, let's manipulate the data before saving.
        if self.form.is_valid():
            self.form = self.form.save(commit=False) #This is the trick to saving the current user data.
            self.form.created_by = self.request.user #Data manipulation.
            self.form.save()                         #Save(commit) the data.
            return redirect('read')                  #Send the users to the DetailView upon submission.
            
        return self.render(request)

    #This function retrieves the initial form itself and brings it to the page.
    def get(self, request):
        self.form = ResponseForm()

        return self.render(request)


# Generic Class Based View (GCVB) UpdateView is NOT yet functional. 
# The Class Based View (CVB) implementation of a UpdateView above is functional.
class UpdateVoteView(UpdateView):
    model = Response
    #fields
    form_class = ResponseForm
    template_name = 'pages/update.html'
    pk_url_kwarg ='created_by'
    context_object_name = 'Response'
    success_url ="pages/read.html"

    #need to add form is not valid function
    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_at = timezone.now()
        post.save()
        return redirect('read')

##########
# Delete #
##########

# Class-Based View(CVB)
#  A Class-Based View extends the View class. Requests are handled inside class methods named after
#  the HTTP methods (GET, POST, PUT, HEAD ect.) offering SUPERIOR flexability.
class DeleteView(View):

    # Renders boilerplate HTML 
    def render(self, request):
        return render(request, 'pages/delete.html')

    # Renders the delete form
    def get(self, request):
        return self.render(request)


    def post(self, request):

        #Delete the existing users previous entry upon delete.
        Response.objects.filter(created_by=self.request.user).delete()

        #return self.render(request)
        return render(request, 'pages/read.html',  {'response': Response})

# Generic Class Based View (GCVB) DeleteView is NOT yet functional. 
# The Class Based View (CVB) implementation of a DeleteView functional.
class ResponseDeleteView(DeleteView):
    model = Response
    success_url ="pages/read.html"