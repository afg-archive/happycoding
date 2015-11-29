from django_fsu import url
from . import views


urlpatterns = [
    url('login/', views.login, name='login'),
    url('logout/', views.logout, name='logout'),
    url('profile/<int:pk>', views.profile, name='profile'),
]
