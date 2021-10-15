from django.urls import path

from .views import HomePageView, DetailView, NewPostView, VoteView, UpdateView, DeleteView, UserAlreadyVotedView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/', DetailView.as_view(), name='read'),
    path('voted/', UserAlreadyVotedView.as_view(), name='votecasted'),
    #path('vote/', VoteView.as_view(), name='create'),
    path('vote/', NewPostView.as_view(), name='create'),
    path('update/', UpdateView.as_view(), name='update'),
    path('delete/', DeleteView.as_view(), name='delete'),
]
