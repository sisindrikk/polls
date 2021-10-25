
from django.urls import path

from . import views

app_name = 'testapp1'
urlpatterns = [
    path('', views.index, name='index'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /testapp1/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /testapp1/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    ]

