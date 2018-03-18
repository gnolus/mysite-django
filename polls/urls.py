from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/id/
    #il nome name è quello usato quando da template richiamiamo url
    path('<int:question_id>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/id/results/
    path('<int:question_id>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/id/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
