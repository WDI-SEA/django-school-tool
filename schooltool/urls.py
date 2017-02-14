from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create_course$', views.create_course, name="create_course"),
    url(r'^login$', views.login, name="login"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^profile$', views.profile, name="profile"),
    url(r'^courses$', views.courses, name="courses"),
    url(r'^courses/(?P<course_id>[0-9]+)/edit$', views.edit_course, name="edit_course"),
]
