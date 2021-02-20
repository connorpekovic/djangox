from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ResumePageView(TemplateView):
    template_name = 'pages/resume.html'

class DiplomaPageView(TemplateView):
    template_name = 'pages/diploma.html'

class CertsPageView(TemplateView):
    template_name = 'pages/certs.html'

class DemoPageView(TemplateView):
    template_name = 'pages/demo.html'