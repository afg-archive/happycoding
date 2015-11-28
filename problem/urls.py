from django_fsu import url
from . import views


urlpatterns = [
    url('<int:oj_id>', views.problem, name='problem'),
    url('<int:oj_id>/share', views.problem_share, name='share'),
    url('upvote/<int:pk>', views.code_upvote, name='code-upvote')
]
