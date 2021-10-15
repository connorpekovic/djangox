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
#   Create 
#   Read
#   Update
#   Delete

################
# Static Pages #
################
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/home.html'


class NoVoteView(TemplateView):
    template_name = 'pages/home.html'


##########
# Create #
##########

# Class-Based View(CVB) example
# A Class-Based View(CVB) is a view that extends the View class. Requests are handled inside class methods 
# named after the HTTP methods, such as get, post, put, head, etc, offering superior flexability.

class NewPostView(View):

    def render(self, request):
        return render(request, 'pages/create_vote.html',  {'form': ResponseForm})

    def post(self, request):

        self.form = ResponseForm(request.POST)

        if self.form.is_valid():
            self.form = self.form.save(commit=False) #This is the trick to saving the current user data.
            self.form.created_by = self.request.user
            self.form.save()
            return redirect('read')
            
        return self.render(request)


    #This function retrieves the initial form itself and brings it to the page.
    def get(self, request):
        self.form = ResponseForm()

        return self.render(request)

# Generic Class-Based View example of a CreateView.  Fully functional
class VoteView(CreateView):
    model = Response
    form_class = ResponseForm
    template_name = 'pages/create_vote.html'
    #success_url = reverse_lazy('HomePageView')


    # Specifying the page to load on submission. The argument of reverse refrences urls.py
    def get_success_url(self):
        return reverse('create')


    # User information attached. https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(VoteView, self).form_valid(form)

    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    # Make more data models known to the template!. Hint, the Question objectwould appears in the HTML Template called 'question_list'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["question_list"] = Question.objects.all()
    #     return context



########
# Read #
########
class DetailView(ListView):
    model = Response
    context_object_name = 'responce_list'
    template_name = 'pages/detail.html'


##########
# Update #
##########

# Class-Based View(CVB)
#  A CBV is a view that extends the View class. Requests are handled inside class methods 
#  named after the HTTP methods, such as get, post, put, head, etc, offering superior flexability.
class UpdateView(View):

    def render(self, request):
        return render(request, 'pages/update_form.html',  {'form': ResponseForm})

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

# Generic Class Based View (GCVB) Update View. I havn't gotten UpdateView to work yet. 
# My workaround is implementing the same Class-Based View(CVB) for Create form, but I delete
# the requesting users Response before saving their new Response.  
class UpdateVoteView(UpdateView):
    model = Response
    #fields
    form_class = ResponseForm
    template_name = 'pages/update_form.html'
    pk_url_kwarg ='created_by'
    context_object_name = 'Response'
    success_url ="pages/detail.html"

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
#  A CBV is a view that extends the View class. Requests are handled inside class methods 
#  named after the HTTP methods, such as get, post, put, head, etc, offering superior flexability.
class DeleteView(View):

    def render(self, request):
        return render(request, 'pages/response_confirm_delete.html')

    def post(self, request):

        #Delete the existing users previous entry.
        Response.objects.filter(created_by=self.request.user).delete()

        #return self.render(request)
        return render(request, 'pages/detail.html',  {'response': Response})

    #This function retrieves the initial form itself and brings it to the page.
    def get(self, request):
        return self.render(request)

class ResponseDeleteView(DeleteView):
    # specify the model you want to use
    model = Response
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="pages/detail.html"