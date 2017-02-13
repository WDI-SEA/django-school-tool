from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^profile$', views.profile, name="profile"),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name="details"),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name="results"),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote")
]
