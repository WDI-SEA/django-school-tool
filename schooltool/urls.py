from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
<<<<<<< HEAD
    url(r'^courses$', views.courses, name="courses")
=======
    url(r'^profile$', views.profile, name="profile"),
>>>>>>> 3dd47cc3beeb170caf7ebdb473668dd9e29293ea
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name="details"),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name="results"),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote")
]
