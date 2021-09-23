from django.urls import path

from .views import HomePageView, AboutPageView, VoteView, DetailView, UpdateVoteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('detail/', DetailView.as_view(), name='read'),
    path('vote/', VoteView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateVoteView.as_view(), name='update'),
    path('delete/', UpdateVoteView.as_view(), name='delete'),
]