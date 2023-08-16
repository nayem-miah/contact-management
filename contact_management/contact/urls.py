from django.urls import path
from . import views
urlpatterns = [ 

    path('', views.contact, name = 'contact'),
    path('notes/', views.user_notes, name='user_notes'),
    path('add-contact/',views.add_contact, name='add_contact'),
    path('edit-contact/<int:pk>/',views.edit_contact, name='edit_contact'),
    path('delete-contact/<int:pk>/',views.delete_contact, name='delete_contact'),
    path('login/',views._login,name='login'),
    path('sign-up/',views.sign_up,name='sign_up'),
    path('log-out/',views.log_out,name='log_out'),
    path('search-contacts/',views.search_contacts,name='search_contacts'),

]
