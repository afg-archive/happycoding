from django_fsu import url
from . import views


urlpatterns = [
    url('<int:oj_id>', views.problem, name='problem'),
    url('<int:oj_id>/share', views.problem_share, name='share'),
    url('upvote/<int:pk>', views.code_upvote, name='code-upvote'),
    url('<int:oj_id>/share_hint', views.hint_share, name='share-hint'),
    url('hint-upvote/<int:pk>', views.hint_upvote, name='hint-upvote')
]
