from django.urls import path
from .views import *

app_name = 'publications'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('publications/create', PublicationCreateView.as_view(), name='create'),
    path('publications/<int:publication_pk>', PublicationView.as_view(), name='detail'),
    path('like/<int:pk>', like_publication, name='like_publication'), 
    path('publications/delete/<int:pk>', PublicationDelete.as_view(), name='delete'),
    path('publications/edit/<int:pk>', PublicationEdit.as_view(), name='publication_edit')
]

