from django.conf.urls import url
from oauth import views

app_name = 'oauth'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.CustomerFormView.as_view(), name='register'),
]