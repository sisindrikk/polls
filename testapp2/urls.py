from django.urls import path
from.import views

app_name="testapp2"

urlpatterns = [
path('home/', views.home, name='home'),
path('details/', views.details, name='details'),
path('create/', views.create, name='create'),
path('recipe_list', views.recipe_list, name='recipe_list'),
path('data/', views.data, name='data'),

]