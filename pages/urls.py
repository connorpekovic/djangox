from django.urls import path

from .views import HomePageView, AboutPageView, ResumePageView, DiplomaPageView, CertsPageView, DemoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('resume/', ResumePageView.as_view(), name='resume'),
    path('diploma/', DiplomaPageView.as_view(), name='diploma'),
    path('certs/', CertsPageView.as_view(), name='certs'),
    path('demo/', DemoPageView.as_view(), name='demo'),
]
