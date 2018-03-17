from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('',                           views.index,  name='index'),
    # ex: /polls/id/
    path('<int:question_id>/',         view.detail,  name='detail'),
    # ex: /polls/id/results/
    path('<int:question_id>/results/', view.results, name='results'),
    # ex: /polls/id/vote/
    path('<int:question_id>/vote/',    view.note,    name='vote'),
]
