from django.urls import path
from .views import index
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create', PetCreate.as_view(), name='create'),
    path('create_post', PostCreate.as_view(), name='create_post'),
    path('view_post/<int:pk>', PostView.as_view(), name='view'),
]