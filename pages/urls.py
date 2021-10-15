from django.urls import path

from .views import HomePageView, DetailView, CreateCBView, CreateGCBView, UpdateCBView, DeleteCBView, HasVoted

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/', DetailView.as_view(), name='read'),
    path('voted/', HasVoted.as_view(), name='votecasted'),
    #path('vote/', CreateGCBView.as_view(), name='create'),
    path('vote/', CreateCBView.as_view(), name='create'),
    path('update/', UpdateCBView.as_view(), name='update'),
    path('delete/', DeleteCBView.as_view(), name='delete'),
]
