from django.urls import path

from .views import HomePageView, AboutPageView, VoteView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', VoteView.as_view(), name='vote'),
]