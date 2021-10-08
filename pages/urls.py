from django.urls import path

from .views import HomePageView, AboutPageView, VoteView, DetailView, UpdateVoteView, NewPostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('detail/', DetailView.as_view(), name='read'),
    #path('vote/', VoteView.as_view(), name='create'),
    path('vote/', NewPostView.as_view(), name='create'),
    path('update/<str>/', UpdateVoteView.as_view(), name='update'),
    path('delete/', UpdateVoteView.as_view(), name='delete'),
]
