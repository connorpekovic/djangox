from django.views.generic import TemplateView,  CreateView
from .forms import ResponseForm
from django.urls import reverse_lazy, reverse

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    # This is the view where we are going to receive responces.
class VoteView(CreateView):
    form_class = ResponseForm
    template_name = 'pages/vote.html'
    #success_url = reverse_lazy('HomePageView')

    # Specifying the page to load on submission. The argument of reverse refrences urls.py
    def get_success_url(self):
        return reverse('vote')
  
    # Make more data models known to the template!. Hint, the Question objectwould appears in the HTML Template called 'question_list'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["question_list"] = Question.objects.all()
    #     return context

    # User information attached. https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(VoteView, self).form_valid(form)