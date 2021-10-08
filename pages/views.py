from django.views.generic import View, TemplateView,  CreateView, ListView
from django.views.generic.edit import UpdateView
from .forms import ResponseForm
from .models import Response
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/home.html'

#Class-Based View(CVB)
#A CBV is a view that extends the View class. Requests are handled inside class methods 
# named after the HTTP methods, such as get, post, put, head, etc, offering superior 
# flexability.
class NewPostView(View):

    def render(self, request):
        return render(request, 'pages/create_vote.html',  {'form': ResponseForm})

    def post(self, request):

        self.form = ResponseForm(request.POST)

        # Need to make a query that identifies of the current user already exist in the 
        # Responce table. If they do exist, redirect to the pages/novote.html web page.

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


class NoVoteView(TemplateView):
    template_name = 'pages/home.html'

# Input Responce objects from models.py.
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


#List View
#Read View
class DetailView(ListView):
    model = Response
    context_object_name = 'responce_list'
    template_name = 'pages/detail.html'


class UpdateVoteView(UpdateView):
    model = Response
    template_name = 'pages/update_form.html'
    pk_url_kwarg ='created_by'
    success_url ="pages/detail.html"

    #need to add form is not valid function