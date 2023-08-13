from django.urls import path
from . import views
urlpatterns = [ 

    path('', views.contact, name = 'contact'),
    path('notes/', views.user_notes, name='user_notes'),

]
