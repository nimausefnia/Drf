from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('one/', views.one, name='one'),
    # path('persons/',views.persons),
    # path('person/<str:name>/',views.person),
    # path('person_create/',views.person_create),


]
