from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='home'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
]