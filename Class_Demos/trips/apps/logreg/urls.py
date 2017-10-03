# FOR APPS
from django.conf.urls import include, url
from . import views
from views import LandingView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name='landing'),
    # url(r'^$', views.index, name='index'),
    # url(r'^login$', views.login, name='login'),
    # url(r'^logout$', views.logout, {'next_page': '/login/'}, name='logout'),
    # url(r'^register$', views.register, name='register'),
    # url(r'^success$', views.success, name='success'),
]
